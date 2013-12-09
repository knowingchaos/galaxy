from __future__ import absolute_import

"""
API operations for Workflows
"""

import logging
from sqlalchemy import desc
from galaxy import util
from galaxy import web
from galaxy import model
from galaxy.tools.parameters import visit_input_values, DataToolParameter, RuntimeValue
from galaxy.web.base.controller import BaseAPIController, url_for
from galaxy.workflow.modules import module_factory, ToolModule
from galaxy.jobs.actions.post import ActionBox
from galaxy.model.item_attrs import UsesAnnotations

from ..controllers.workflow import attach_ordered_steps

log = logging.getLogger(__name__)

class WorkflowsAPIController(BaseAPIController, UsesAnnotations):
    @web.expose_api
    def index(self, trans, **kwd):
        """
        GET /api/workflows

        Displays a collection of workflows.
        """
        rval = []
        for wf in trans.sa_session.query(trans.app.model.StoredWorkflow).filter_by(
                user=trans.user, deleted=False).order_by(
                desc(trans.app.model.StoredWorkflow.table.c.update_time)).all():
            item = wf.get_api_value(value_mapper={'id':trans.security.encode_id})
            encoded_id = trans.security.encode_id(wf.id)
            item['url'] = url_for('workflow', id=encoded_id)
            rval.append(item)
        for wf_sa in trans.sa_session.query( trans.app.model.StoredWorkflowUserShareAssociation ).filter_by(
                user=trans.user ).join( 'stored_workflow' ).filter(
                trans.app.model.StoredWorkflow.deleted == False ).order_by(
                desc( trans.app.model.StoredWorkflow.update_time ) ).all():
            item = wf_sa.stored_workflow.get_api_value(value_mapper={'id':trans.security.encode_id})
            encoded_id = trans.security.encode_id(wf_sa.stored_workflow.id)
            item['url'] = url_for('workflow', id=encoded_id)
            rval.append(item)
        return rval

    @web.expose_api
    def show(self, trans, id, **kwd):
        """
        GET /api/workflows/{encoded_workflow_id}

        Displays information needed to run a workflow from the command line.
        """
        workflow_id = id
        try:
            decoded_workflow_id = trans.security.decode_id(workflow_id)
        except TypeError:
            trans.response.status = 400
            return "Malformed workflow id ( %s ) specified, unable to decode." % str(workflow_id)
        try:
            stored_workflow = trans.sa_session.query(trans.app.model.StoredWorkflow).get(decoded_workflow_id)
            if stored_workflow.user != trans.user and not trans.user_is_admin():
                if trans.sa_session.query(trans.app.model.StoredWorkflowUserShareAssociation).filter_by(user=trans.user, stored_workflow=stored_workflow).count() == 0:
                    trans.response.status = 400
                    return("Workflow is not owned by or shared with current user")
        except:
            trans.response.status = 400
            return "That workflow does not exist."
        item = stored_workflow.get_api_value(view='element', value_mapper={'id':trans.security.encode_id})
        item['url'] = url_for('workflow', id=workflow_id)
        latest_workflow = stored_workflow.latest_workflow
        inputs = {}
        for step in latest_workflow.steps:
            if step.type == 'data_input':
                inputs[step.id] = {'label':step.tool_inputs['name'], 'value':""}
            else:
                pass
                # Eventually, allow regular tool parameters to be inserted and modified at runtime.
                # p = step.get_required_parameters()
        item['inputs'] = inputs
        steps = {}
        for step in latest_workflow.steps:
            steps[step.id] = {'id': step.id,
                              'type': step.type,
                              'tool_id': step.tool_id,
                              'input_steps': {}}
            for conn in step.input_connections:
                steps[step.id]['input_steps'][conn.input_name] = {'source_step': conn.output_step_id,
                                                                  'step_output': conn.output_name}
        item['steps'] = steps
        return item

    @web.expose_api
    def create(self, trans, payload, **kwd):
        """
        POST /api/workflows

        We're not creating workflows from the api.  Just execute for now.

        However, we will import them if installed_repository_file is specified
        """

        # ------------------------------------------------------------------------------- #
        ### RPARK: dictionary containing which workflows to change and edit ###
        param_map = {};
        if (payload.has_key('parameters') ):
            param_map = payload['parameters'];
        # ------------------------------------------------------------------------------- #




        if 'workflow_id' not in payload:
            # create new
            if 'installed_repository_file' in payload:
                workflow_controller = trans.webapp.controllers[ 'workflow' ]
                result = workflow_controller.import_workflow( trans=trans,
                                                              cntrller='api',
                                                              **payload)
                return result
            trans.response.status = 403
            return "Either workflow_id or installed_repository_file must be specified"
        if 'installed_repository_file' in payload:
            trans.response.status = 403
            return "installed_repository_file may not be specified with workflow_id"
        stored_workflow = trans.sa_session.query(self.app.model.StoredWorkflow).get(
                        trans.security.decode_id(payload['workflow_id']))
        if stored_workflow.user != trans.user and not trans.user_is_admin():
            if trans.sa_session.query(trans.app.model.StoredWorkflowUserShareAssociation).filter_by(user=trans.user, stored_workflow=stored_workflow).count() == 0:
                trans.response.status = 400
                return("Workflow is not owned by or shared with current user")
        workflow = stored_workflow.latest_workflow
        if payload['history'].startswith('hist_id='):
            #Passing an existing history to use.
            history = trans.sa_session.query(self.app.model.History).get(
                    trans.security.decode_id(payload['history'][8:]))
            if history.user != trans.user and not trans.user_is_admin():
                trans.response.status = 400
                return "Invalid History specified."
        else:
            history = self.app.model.History(name=payload['history'], user=trans.user)
            trans.sa_session.add(history)
            trans.sa_session.flush()
        ds_map = payload['ds_map']
        add_to_history = 'no_add_to_history' not in payload
        for k in ds_map:
            try:
                if ds_map[k]['src'] == 'ldda':
                    ldda = trans.sa_session.query(self.app.model.LibraryDatasetDatasetAssociation).get(
                            trans.security.decode_id(ds_map[k]['id']))
                    assert trans.user_is_admin() or trans.app.security_agent.can_access_dataset( trans.get_current_user_roles(), ldda.dataset )
                    hda = ldda.to_history_dataset_association(history, add_to_history=add_to_history)
                elif ds_map[k]['src'] == 'ld':
                    ldda = trans.sa_session.query(self.app.model.LibraryDataset).get(
                            trans.security.decode_id(ds_map[k]['id'])).library_dataset_dataset_association
                    assert trans.user_is_admin() or trans.app.security_agent.can_access_dataset( trans.get_current_user_roles(), ldda.dataset )
                    hda = ldda.to_history_dataset_association(history, add_to_history=add_to_history)
                elif ds_map[k]['src'] == 'hda':
                    # Get dataset handle, add to dict and history if necessary
                    hda = trans.sa_session.query(self.app.model.HistoryDatasetAssociation).get(
                            trans.security.decode_id(ds_map[k]['id']))
                    assert trans.user_is_admin() or trans.app.security_agent.can_access_dataset( trans.get_current_user_roles(), hda.dataset )
                else:
                    trans.response.status = 400
                    return "Unknown dataset source '%s' specified." % ds_map[k]['src']
                if add_to_history and  hda.history != history:
                    hda = hda.copy()
                    history.add_dataset(hda)
                ds_map[k]['hda'] = hda
            except AssertionError:
                trans.response.status = 400
                return "Invalid Dataset '%s' Specified" % ds_map[k]['id']
        if not workflow:
            trans.response.status = 400
            return "Workflow not found."
        if len( workflow.steps ) == 0:
            trans.response.status = 400
            return "Workflow cannot be run because it does not have any steps"
        if workflow.has_cycles:
            trans.response.status = 400
            return "Workflow cannot be run because it contains cycles"
        if workflow.has_errors:
            trans.response.status = 400
            return "Workflow cannot be run because of validation errors in some steps"
        # Build the state for each step
        rval = {}
        for step in workflow.steps:
            step_errors = None
            if step.type == 'tool' or step.type is None:
                step.module = module_factory.from_workflow_step( trans, step )
                # Check for missing parameters
                step.upgrade_messages = step.module.check_and_update_state()
                # Any connected input needs to have value DummyDataset (these
                # are not persisted so we need to do it every time)
                step.module.add_dummy_datasets( connections=step.input_connections )
                step.state = step.module.state

                ####################################################
                ####################################################
                # RPARK: IF TOOL_NAME IN PARAMETER MAP #
                if step.tool_id in param_map:
                    change_param = param_map[step.tool_id]['param'];
                    change_value = param_map[step.tool_id]['value'];
                    step.state.inputs[change_param] = change_value;
                ####################################################
                ####################################################

                if step.tool_errors:
                    trans.response.status = 400
                    return "Workflow cannot be run because of validation errors in some steps: %s" % step_errors
                if step.upgrade_messages:
                    trans.response.status = 400
                    return "Workflow cannot be run because of step upgrade messages: %s" % step.upgrade_messages
            else:
                # This is an input step.  Make sure we have an available input.
                if step.type == 'data_input' and str(step.id) not in ds_map:
                    trans.response.status = 400
                    return "Workflow cannot be run because an expected input step '%s' has no input dataset." % step.id
                step.module = module_factory.from_workflow_step( trans, step )
                step.state = step.module.get_runtime_state()
            step.input_connections_by_name = dict( ( conn.input_name, conn ) for conn in step.input_connections )
        # Run each step, connecting outputs to inputs
        workflow_invocation = self.app.model.WorkflowInvocation()
        workflow_invocation.workflow = workflow
        outputs = util.odict.odict()
        rval['history'] = trans.security.encode_id(history.id)
        rval['outputs'] = []
        for i, step in enumerate( workflow.steps ):
            job = None
            if step.type == 'tool' or step.type is None:
                tool = self.app.toolbox.get_tool( step.tool_id )
                def callback( input, value, prefixed_name, prefixed_label ):
                    if isinstance( input, DataToolParameter ):
                        if prefixed_name in step.input_connections_by_name:
                            conn = step.input_connections_by_name[ prefixed_name ]
                            return outputs[ conn.output_step.id ][ conn.output_name ]
                visit_input_values( tool.inputs, step.state.inputs, callback )
                job, out_data = tool.execute( trans, step.state.inputs, history=history)
                outputs[ step.id ] = out_data
                for pja in step.post_job_actions:
                    if pja.action_type in ActionBox.immediate_actions:
                        ActionBox.execute(self.app, trans.sa_session, pja, job, replacement_dict=None)
                    else:
                        job.add_post_job_action(pja)
                for v in out_data.itervalues():
                    rval['outputs'].append(trans.security.encode_id(v.id))
            else:
                #This is an input step.  Use the dataset inputs from ds_map.
                job, out_data = step.module.execute( trans, step.state)
                outputs[step.id] = out_data
                outputs[step.id]['output'] = ds_map[str(step.id)]['hda']
            workflow_invocation_step = self.app.model.WorkflowInvocationStep()
            workflow_invocation_step.workflow_invocation = workflow_invocation
            workflow_invocation_step.workflow_step = step
            workflow_invocation_step.job = job
        trans.sa_session.add( workflow_invocation )
        trans.sa_session.flush()
        return rval

    @web.expose_api
    def workflow_dict( self, trans, workflow_id, **kwd ):
        """
        GET /api/workflows/{encoded_workflow_id}/download
        Returns a selected workflow as a json dictionary.
        """
        try:
            stored_workflow = trans.sa_session.query(self.app.model.StoredWorkflow).get(trans.security.decode_id(workflow_id))
        except Exception,e:
            return ("Workflow with ID='%s' can not be found\n Exception: %s") % (workflow_id, str( e ))
        # check to see if user has permissions to selected workflow
        if stored_workflow.user != trans.user and not trans.user_is_admin():
            if trans.sa_session.query(trans.app.model.StoredWorkflowUserShareAssociation).filter_by(user=trans.user, stored_workflow=stored_workflow).count() == 0:
                trans.response.status = 400
                return("Workflow is not owned by or shared with current user")

        ret_dict = self._workflow_to_dict( trans, stored_workflow );
        return ret_dict

    @web.expose_api
    def delete( self, trans, id, **kwd ):
        """
        DELETE /api/workflows/{encoded_workflow_id}
        Deletes a specified workflow
        Author: rpark

        copied from galaxy.web.controllers.workflows.py (delete)
        """
        workflow_id = id;

        try:
            stored_workflow = trans.sa_session.query(self.app.model.StoredWorkflow).get(trans.security.decode_id(workflow_id))
        except Exception, e:
            trans.response.status = 400
            return ("Workflow with ID='%s' can not be found\n Exception: %s") % (workflow_id, str( e ))

        # check to see if user has permissions to selected workflow
        if stored_workflow.user != trans.user and not trans.user_is_admin():
            if trans.sa_session.query(trans.app.model.StoredWorkflowUserShareAssociation).filter_by(user=trans.user, stored_workflow=stored_workflow).count() == 0:
                trans.response.status = 403
                return("Workflow is not owned by or shared with current user")

        #Mark a workflow as deleted
        stored_workflow.deleted = True
        trans.sa_session.flush()

        # TODO: Unsure of response message to let api know that a workflow was successfully deleted
        #return 'OK'
        return ( "Workflow '%s' successfully deleted" % stored_workflow.name )

    @web.expose_api
    def import_new_workflow(self, trans, payload, **kwd):
        """
        POST /api/workflows/upload
        Importing dynamic workflows from the api. Return newly generated workflow id.
        Author: rpark

        # currently assumes payload['workflow'] is a json representation of a workflow to be inserted into the database
        """

        data = payload['workflow'];
        workflow, missing_tool_tups = self._workflow_from_dict( trans, data, source="API" )

        # galaxy workflow newly created id
        workflow_id = workflow.id;
        # api encoded, id
        encoded_id = trans.security.encode_id(workflow_id);

        # return list
        rval= [];

        item = workflow.get_api_value(value_mapper={'id':trans.security.encode_id})
        item['url'] = url_for('workflow', id=encoded_id)

        rval.append(item);

        return item;

    def _workflow_from_dict( self, trans, data, source=None ):
        """
        RPARK: copied from galaxy.webapps.galaxy.controllers.workflows.py
        Creates a workflow from a dict. Created workflow is stored in the database and returned.
        """
        # Put parameters in workflow mode
        trans.workflow_building_mode = True
        # Create new workflow from incoming dict
        workflow = model.Workflow()
        # If there's a source, put it in the workflow name.
        if source:
            name = "%s (imported from %s)" % ( data['name'], source )
        else:
            name = data['name']
        workflow.name = name
        # Assume no errors until we find a step that has some
        workflow.has_errors = False
        # Create each step
        steps = []
        # The editor will provide ids for each step that we don't need to save,
        # but do need to use to make connections
        steps_by_external_id = {}
        # Keep track of tools required by the workflow that are not available in
        # the local Galaxy instance.  Each tuple in the list of missing_tool_tups
        # will be ( tool_id, tool_name, tool_version ).
        missing_tool_tups = []
        # First pass to build step objects and populate basic values
        for key, step_dict in data[ 'steps' ].iteritems():
            # Create the model class for the step
            step = model.WorkflowStep()
            steps.append( step )
            steps_by_external_id[ step_dict['id' ] ] = step
            # FIXME: Position should be handled inside module
            step.position = step_dict['position']
            module = module_factory.from_dict( trans, step_dict, secure=False )
            if module.type == 'tool' and module.tool is None:
                # A required tool is not available in the local Galaxy instance.
                missing_tool_tup = ( step_dict[ 'tool_id' ], step_dict[ 'name' ], step_dict[ 'tool_version' ] )
                if missing_tool_tup not in missing_tool_tups:
                    missing_tool_tups.append( missing_tool_tup )
            module.save_to_step( step )
            if step.tool_errors:
                workflow.has_errors = True
            # Stick this in the step temporarily
            step.temp_input_connections = step_dict['input_connections']
            # Save step annotation.
            #annotation = step_dict[ 'annotation' ]
            #if annotation:
                #annotation = sanitize_html( annotation, 'utf-8', 'text/html' )
                # ------------------------------------------ #
                # RPARK REMOVING: user annotation b/c of API
                #self.add_item_annotation( trans.sa_session, trans.get_user(), step, annotation )
                # ------------------------------------------ #
            # Unpack and add post-job actions.
            post_job_actions = step_dict.get( 'post_job_actions', {} )
            for name, pja_dict in post_job_actions.items():
                model.PostJobAction( pja_dict[ 'action_type' ],
                                     step, pja_dict[ 'output_name' ],
                                     pja_dict[ 'action_arguments' ] )
        # Second pass to deal with connections between steps
        for step in steps:
            # Input connections
            for input_name, conn_dict in step.temp_input_connections.iteritems():
                if conn_dict:
                    conn = model.WorkflowStepConnection()
                    conn.input_step = step
                    conn.input_name = input_name
                    conn.output_name = conn_dict['output_name']
                    conn.output_step = steps_by_external_id[ conn_dict['id'] ]
            del step.temp_input_connections
        # Order the steps if possible
        attach_ordered_steps( workflow, steps )
        # Connect up
        stored = model.StoredWorkflow()
        stored.name = workflow.name
        workflow.stored_workflow = stored
        stored.latest_workflow = workflow
        stored.user = trans.user
        # Persist
        trans.sa_session.add( stored )
        trans.sa_session.flush()
        return stored, missing_tool_tups

    def _workflow_to_dict( self, trans, stored ):
        """
        RPARK: copied from galaxy.web.controllers.workflows.py
        Converts a workflow to a dict of attributes suitable for exporting.
        """
        workflow = stored.latest_workflow

        ### ----------------------------------- ###
        ## RPARK EDIT ##
        workflow_annotation = self.get_item_annotation_obj( trans.sa_session, trans.user, stored )
        annotation_str = ""
        if workflow_annotation:
            annotation_str = workflow_annotation.annotation
        ### ----------------------------------- ###


        # Pack workflow data into a dictionary and return
        data = {}
        data['a_galaxy_workflow'] = 'true' # Placeholder for identifying galaxy workflow
        data['format-version'] = "0.1"
        data['name'] = workflow.name
        ### ----------------------------------- ###
        ## RPARK EDIT ##
        data['annotation'] = annotation_str
        ### ----------------------------------- ###

        data['steps'] = {}
        # For each step, rebuild the form and encode the state
        for step in workflow.steps:
            # Load from database representation
            module = module_factory.from_workflow_step( trans, step )

            ### ----------------------------------- ###
            ## RPARK EDIT ##
            # Get user annotation.
            step_annotation = self.get_item_annotation_obj(trans.sa_session, trans.user, step )
            annotation_str = ""
            if step_annotation:
                annotation_str = step_annotation.annotation
            ### ----------------------------------- ###

            # Step info
            step_dict = {
                'id': step.order_index,
                'type': module.type,
                'tool_id': module.get_tool_id(),
                'tool_version' : step.tool_version,
                'name': module.get_name(),
                'tool_state': module.get_state( secure=False ),
                'tool_errors': module.get_errors(),
                ## 'data_inputs': module.get_data_inputs(),
                ## 'data_outputs': module.get_data_outputs(),

                ### ----------------------------------- ###
                ## RPARK EDIT ##
                'annotation' : annotation_str
                ### ----------------------------------- ###

            }
            # Add post-job actions to step dict.
            if module.type == 'tool':
                pja_dict = {}
                for pja in step.post_job_actions:
                    pja_dict[pja.action_type+pja.output_name] = dict( action_type = pja.action_type,
                                                                      output_name = pja.output_name,
                                                                      action_arguments = pja.action_arguments )
                step_dict[ 'post_job_actions' ] = pja_dict
            # Data inputs
            step_dict['inputs'] = []
            if module.type == "data_input":
                # Get input dataset name; default to 'Input Dataset'
                name = module.state.get( 'name', 'Input Dataset')
                step_dict['inputs'].append( { "name" : name, "description" : annotation_str } )
            else:
                # Step is a tool and may have runtime inputs.
                for name, val in module.state.inputs.items():
                    input_type = type( val )
                    if input_type == RuntimeValue:
                        step_dict['inputs'].append( { "name" : name, "description" : "runtime parameter for tool %s" % module.get_name() } )
                    elif input_type == dict:
                        # Input type is described by a dict, e.g. indexed parameters.
                        for partname, partval in val.items():
                            if type( partval ) == RuntimeValue:
                                step_dict['inputs'].append( { "name" : name, "description" : "runtime parameter for tool %s" % module.get_name() } )
            # User outputs
            step_dict['user_outputs'] = []
            """
            module_outputs = module.get_data_outputs()
            step_outputs = trans.sa_session.query( WorkflowOutput ).filter( step=step )
            for output in step_outputs:
                name = output.output_name
                annotation = ""
                for module_output in module_outputs:
                    if module_output.get( 'name', None ) == name:
                        output_type = module_output.get( 'extension', '' )
                        break
                data['outputs'][name] = { 'name' : name, 'annotation' : annotation, 'type' : output_type }
            """

            # All step outputs
            step_dict['outputs'] = []
            if type( module ) is ToolModule:
                for output in module.get_data_outputs():
                    step_dict['outputs'].append( { 'name' : output['name'], 'type' : output['extensions'][0] } )
            # Connections
            input_connections = step.input_connections
            if step.type is None or step.type == 'tool':
                # Determine full (prefixed) names of valid input datasets
                data_input_names = {}
                def callback( input, value, prefixed_name, prefixed_label ):
                    if isinstance( input, DataToolParameter ):
                        data_input_names[ prefixed_name ] = True
                visit_input_values( module.tool.inputs, module.state.inputs, callback )
                # Filter
                # FIXME: this removes connection without displaying a message currently!
                input_connections = [ conn for conn in input_connections if conn.input_name in data_input_names ]
            # Encode input connections as dictionary
            input_conn_dict = {}
            for conn in input_connections:
                input_conn_dict[ conn.input_name ] = \
                    dict( id=conn.output_step.order_index, output_name=conn.output_name )
            step_dict['input_connections'] = input_conn_dict
            # Position
            step_dict['position'] = step.position
            # Add to return value
            data['steps'][step.order_index] = step_dict
        return data

