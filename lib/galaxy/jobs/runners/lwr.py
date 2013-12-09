import logging

from galaxy import model
from galaxy.jobs.runners import AsynchronousJobState, AsynchronousJobRunner
from galaxy.jobs import JobDestination

import errno
from time import sleep
import os

from lwr_client import FileStager, Client, url_to_destination_params

log = logging.getLogger( __name__ )

__all__ = [ 'LwrJobRunner' ]


class LwrJobRunner( AsynchronousJobRunner ):
    """
    LWR Job Runner
    """
    runner_name = "LWRRunner"

    def __init__( self, app, nworkers, transport=None ):
        """Start the job runner """
        super( LwrJobRunner, self ).__init__( app, nworkers )
        self._init_monitor_thread()
        self._init_worker_threads()
        self.transport_type = transport

    def url_to_destination( self, url ):
        """Convert a legacy URL to a job destination"""
        return JobDestination( runner="lwr", params=url_to_destination_params( url ) )

    def check_watched_item(self, job_state):
        try:
            client = self.get_client_from_state(job_state)
            status = client.get_status()
        except Exception:
            # An orphaned job was put into the queue at app startup, so remote server went down
            # either way we are done I guess.
            self.mark_as_finished(job_state)
            return None
        if status == "complete":
            self.mark_as_finished(job_state)
            return None
        if status == "running" and not job_state.running:
            job_state.running = True
            job_state.job_wrapper.change_state( model.Job.states.RUNNING )
        return job_state

    def queue_job(self, job_wrapper):
        command_line = ''
        job_destination = job_wrapper.job_destination

        try:
            job_wrapper.prepare()
            if hasattr(job_wrapper, 'prepare_input_files_cmds') and job_wrapper.prepare_input_files_cmds is not None:
                for cmd in job_wrapper.prepare_input_files_cmds:  # run the commands to stage the input files
                    #log.debug( 'executing: %s' % cmd )
                    if 0 != os.system(cmd):
                        raise Exception('Error running file staging command: %s' % cmd)
                job_wrapper.prepare_input_files_cmds = None  # prevent them from being used in-line
            command_line = self.build_command_line( job_wrapper, include_metadata=False, include_work_dir_outputs=False )
        except:
            job_wrapper.fail( "failure preparing job", exception=True )
            log.exception("failure running job %d" % job_wrapper.job_id)
            return

        # If we were able to get a command line, run the job
        if not command_line:
            job_wrapper.finish( '', '' )
            return

        try:
            client = self.get_client_from_wrapper(job_wrapper)
            output_files = self.get_output_files(job_wrapper)
            input_files = job_wrapper.get_input_fnames()
            working_directory = job_wrapper.working_directory
            tool = job_wrapper.tool
            file_stager = FileStager(client, tool, command_line, job_wrapper.extra_filenames, input_files, output_files, working_directory)
            rebuilt_command_line = file_stager.get_rewritten_command_line()
            job_id = file_stager.job_id
            client.launch( rebuilt_command_line )
            job_wrapper.set_job_destination( job_destination, job_id )
            job_wrapper.change_state( model.Job.states.QUEUED )
        except:
            job_wrapper.fail( "failure running job", exception=True )
            log.exception("failure running job %d" % job_wrapper.job_id)
            return

        lwr_job_state = AsynchronousJobState()
        lwr_job_state.job_wrapper = job_wrapper
        lwr_job_state.job_id = job_id
        lwr_job_state.old_state = True
        lwr_job_state.running = False
        lwr_job_state.job_destination = job_destination
        self.monitor_job(lwr_job_state)

    def get_output_files(self, job_wrapper):
        output_fnames = job_wrapper.get_output_fnames()
        return [ str( o ) for o in output_fnames ]

    def get_client_from_wrapper(self, job_wrapper):
        job_id = job_wrapper.job_id
        if hasattr(job_wrapper, 'task_id'):
            job_id = "%s_%s" % (job_id, job_wrapper.task_id)
        return self.get_client( job_wrapper.job_destination.params, job_id )

    def get_client_from_state(self, job_state):
        job_destination_params = job_state.job_destination.params
        job_id = job_state.job_id
        return self.get_client( job_destination_params, job_id )

    def get_client( self, job_destination_params, job_id ):
        return Client( job_destination_params, job_id, transport_type=self.transport_type )

    def finish_job( self, job_state ):
        stderr = stdout = command_line = ''
        job_wrapper = job_state.job_wrapper
        try:
            client = self.get_client_from_state(job_state)

            run_results = client.raw_check_complete()
            stdout = run_results['stdout']
            stderr = run_results['stderr']

            download_failure_exceptions = []
            if job_wrapper.get_state() not in [ model.Job.states.ERROR, model.Job.states.DELETED ]:
                work_dir_outputs = self.get_work_dir_outputs(job_wrapper)
                output_files = self.get_output_files(job_wrapper)
                for source_file, output_file in work_dir_outputs:
                    try:
                        client.download_work_dir_output(source_file, job_wrapper.working_directory, output_file)
                    except Exception, e:
                        download_failure_exceptions.append(e)
                    # Remove from full output_files list so don't try to download directly.
                    output_files.remove(output_file)
                for output_file in output_files:
                    try:
                        client.download_output(output_file, working_directory=job_wrapper.working_directory)
                    except Exception, e:
                        download_failure_exceptions.append(e)
            if download_failure_exceptions or self.app.config.cleanup_job == "always":
                try:
                    client.clean()
                except:
                    log.warn("Failed to cleanup remote LWR job")
            if download_failure_exceptions:
                job_wrapper.fail("Failed to find or download one or more job outputs from remote server.", exception=True)
            log.debug('execution finished: %s' % command_line)
        except:
            message = "Failed to communicate with remote job server."
            job_wrapper.fail( message, exception=True )
            log.exception("failure running job %d" % job_wrapper.job_id)
            return
        self._handle_metadata_externally( job_wrapper )
        # Finish the job
        try:
            job_wrapper.finish( stdout, stderr )
        except:
            log.exception("Job wrapper finish method failed")
            job_wrapper.fail("Unable to finish job", exception=True)

    def fail_job( self, job_state ):
        """
        Seperated out so we can use the worker threads for it.
        """
        self.stop_job( self.sa_session.query( self.app.model.Job ).get( job_state.job_wrapper.job_id ) )
        job_state.job_wrapper.fail( job_state.fail_message )

    def check_pid( self, pid ):
        try:
            os.kill( pid, 0 )
            return True
        except OSError, e:
            if e.errno == errno.ESRCH:
                log.debug( "check_pid(): PID %d is dead" % pid )
            else:
                log.warning( "check_pid(): Got errno %s when attempting to check PID %d: %s" % ( errno.errorcode[e.errno], pid, e.strerror ) )
            return False

    def stop_job( self, job ):
        #if our local job has JobExternalOutputMetadata associated, then our primary job has to have already finished
        job_ext_output_metadata = job.get_external_output_metadata()
        if job_ext_output_metadata:
            pid = job_ext_output_metadata[0].job_runner_external_pid  # every JobExternalOutputMetadata has a pid set, we just need to take from one of them
            if pid in [ None, '' ]:
                log.warning( "stop_job(): %s: no PID in database for job, unable to stop" % job.id )
                return
            pid = int( pid )
            if not self.check_pid( pid ):
                log.warning( "stop_job(): %s: PID %d was already dead or can't be signaled" % ( job.id, pid ) )
                return
            for sig in [ 15, 9 ]:
                try:
                    os.killpg( pid, sig )
                except OSError, e:
                    log.warning( "stop_job(): %s: Got errno %s when attempting to signal %d to PID %d: %s" % ( job.id, errno.errorcode[e.errno], sig, pid, e.strerror ) )
                    return  # give up
                sleep( 2 )
                if not self.check_pid( pid ):
                    log.debug( "stop_job(): %s: PID %d successfully killed with signal %d" % ( job.id, pid, sig ) )
                    return
                else:
                    log.warning( "stop_job(): %s: PID %d refuses to die after signaling TERM/KILL" % ( job.id, pid ) )
        else:
            # Remote kill
            lwr_url = job.job_runner_name
            job_id = job.job_runner_external_id
            log.debug("Attempt remote lwr kill of job with url %s and id %s" % (lwr_url, job_id))
            client = self.get_client(job.destination_params, job_id)
            client.kill()

    def recover( self, job, job_wrapper ):
        """Recovers jobs stuck in the queued/running state when Galaxy started"""
        job_state = AsynchronousJobState()
        job_state.job_id = str( job.get_job_runner_external_id() )
        job_state.runner_url = job_wrapper.get_job_runner_url()
        job_state.job_destination = job_wrapper.job_destination
        job_wrapper.command_line = job.get_command_line()
        job_state.job_wrapper = job_wrapper
        state = job.get_state()
        if state in [model.Job.states.RUNNING, model.Job.states.QUEUED]:
            log.debug( "(LWR/%s) is still in running state, adding to the LWR queue" % ( job.get_id()) )
            job_state.old_state = True
            job_state.running = state == model.Job.states.RUNNING
            self.monitor_queue.put( job_state )
