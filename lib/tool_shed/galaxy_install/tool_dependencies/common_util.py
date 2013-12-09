import logging
import os
import shutil
import sys
import tarfile
import traceback
import urllib2
import zipfile
import tool_shed.util.shed_util_common as suc
from galaxy.datatypes import checkers

log = logging.getLogger( __name__ )

def clean_tool_shed_url( base_url ):
    if base_url:
        protocol, base = base_url.split( '://' )
        return base.rstrip( '/' )
    return base_url

def create_env_var_dict( elem, tool_dependency_install_dir=None, tool_shed_repository_install_dir=None ):
    env_var_name = elem.get( 'name', 'PATH' )
    env_var_action = elem.get( 'action', 'prepend_to' )
    env_var_text = None
    if elem.text and elem.text.find( 'REPOSITORY_INSTALL_DIR' ) >= 0:
        if tool_shed_repository_install_dir and elem.text.find( '$REPOSITORY_INSTALL_DIR' ) != -1:
            env_var_text = elem.text.replace( '$REPOSITORY_INSTALL_DIR', tool_shed_repository_install_dir )
            return dict( name=env_var_name, action=env_var_action, value=env_var_text )
        else:
            env_var_text = elem.text.replace( '$REPOSITORY_INSTALL_DIR', tool_dependency_install_dir )
            return dict( name=env_var_name, action=env_var_action, value=env_var_text )
    if elem.text and elem.text.find( 'INSTALL_DIR' ) >= 0:
        if tool_dependency_install_dir:
            env_var_text = elem.text.replace( '$INSTALL_DIR', tool_dependency_install_dir )
            return dict( name=env_var_name, action=env_var_action, value=env_var_text )
        else:
            env_var_text = elem.text.replace( '$INSTALL_DIR', tool_shed_repository_install_dir )
            return dict( name=env_var_name, action=env_var_action, value=env_var_text )
    if elem.text:
        # Allow for environment variables that contain neither REPOSITORY_INSTALL_DIR nor INSTALL_DIR since there may be command line
        # parameters that are tuned for a Galaxy instance.  Allowing them to be set in one location rather than being hard coded into
        # each tool config is the best approach.  For example:
        # <environment_variable name="GATK2_SITE_OPTIONS" action="set_to">
        #    "--num_threads 4 --num_cpu_threads_per_data_thread 3 --phone_home STANDARD"
        # </environment_variable>
        return dict( name=env_var_name, action=env_var_action, value=elem.text)
    return None

def create_or_update_env_shell_file( install_dir, env_var_dict ):
    env_var_name = env_var_dict[ 'name' ]
    env_var_action = env_var_dict[ 'action' ]
    env_var_value = env_var_dict[ 'value' ]
    if env_var_action == 'prepend_to':
        changed_value = '%s:$%s' % ( env_var_value, env_var_name )
    elif env_var_action == 'set_to':
        changed_value = '%s' % env_var_value
    elif env_var_action == 'append_to':
        changed_value = '$%s:%s' % ( env_var_name, env_var_value )
    line = "%s=%s; export %s" % (env_var_name, changed_value, env_var_name)
    return create_or_update_env_shell_file_with_command(install_dir, line)


def create_or_update_env_shell_file_with_command( install_dir, command ):
    """
    Return a shell expression which when executed will create or update
    a Galaxy env.sh dependency file in the specified install_dir containing
    the supplied command.
    """
    env_shell_file_path = '%s/env.sh' % install_dir
    if os.path.exists( env_shell_file_path ):
        write_action = '>>'
    else:
        write_action = '>'
    cmd = "echo %s %s %s;chmod +x %s" % ( __shellquote(command),
                                          write_action,
                                          __shellquote(env_shell_file_path),
                                          __shellquote(env_shell_file_path))
    return cmd


def extract_tar( file_name, file_path ):
    if isgzip( file_name ) or isbz2( file_name ):
        # Open for reading with transparent compression.
        tar = tarfile.open( file_name, 'r:*', errorlevel=0 )
    else:
        tar = tarfile.open( file_name, errorlevel=0 )
    tar.extractall( path=file_path )
    tar.close()

def extract_zip( archive_path, extraction_path ):
    # TODO: change this method to use zipfile.Zipfile.extractall() when we stop supporting Python 2.5.
    if not zipfile_ok( archive_path ):
        return False
    zip_archive = zipfile.ZipFile( archive_path, 'r' )
    for name in zip_archive.namelist():
        uncompressed_path = os.path.join( extraction_path, name )
        if uncompressed_path.endswith( '/' ):
            if not os.path.isdir( uncompressed_path ):
                os.makedirs( uncompressed_path )
        else:
            file( uncompressed_path, 'wb' ).write( zip_archive.read( name ) )
    zip_archive.close()
    return True

def format_traceback():
    ex_type, ex, tb = sys.exc_info()
    return ''.join( traceback.format_tb( tb ) )

def get_env_shell_file_path( installation_directory ):
    env_shell_file_name = 'env.sh'
    default_location = os.path.abspath( os.path.join( installation_directory, env_shell_file_name ) )
    if os.path.exists( default_location ):
        return default_location
    for root, dirs, files in os.walk( installation_directory ):
        for name in files:
            if name == env_shell_file_name:
                return os.path.abspath( os.path.join( root, name ) )
    return None

def get_env_shell_file_paths( app, elem ):
    # Currently only the following tag set is supported.
    #    <repository toolshed="http://localhost:9009/" name="package_numpy_1_7" owner="test" changeset_revision="c84c6a8be056">
    #        <package name="numpy" version="1.7.1" />
    #    </repository>
    env_shell_file_paths = []
    toolshed = elem.get( 'toolshed', None )
    repository_name = elem.get( 'name', None )
    repository_owner = elem.get( 'owner', None )
    changeset_revision = elem.get( 'changeset_revision', None )
    if toolshed and repository_name and repository_owner and changeset_revision:
        toolshed = clean_tool_shed_url( toolshed )
        repository = suc.get_repository_for_dependency_relationship( app, toolshed, repository_name, repository_owner, changeset_revision )
        if repository:
            for sub_elem in elem:
                tool_dependency_type = sub_elem.tag
                tool_dependency_name = sub_elem.get( 'name' )
                tool_dependency_version = sub_elem.get( 'version' )
                if tool_dependency_type and tool_dependency_name and tool_dependency_version:
                    # Get the tool_dependency so we can get it's installation directory.
                    tool_dependency = None
                    for tool_dependency in repository.tool_dependencies:
                        if tool_dependency.type == tool_dependency_type and tool_dependency.name == tool_dependency_name and tool_dependency.version == tool_dependency_version:
                            break
                    if tool_dependency:
                        tool_dependency_key = '%s/%s' % ( tool_dependency_name, tool_dependency_version )
                        installation_directory = tool_dependency.installation_directory( app )
                        env_shell_file_path = get_env_shell_file_path( installation_directory )
                        if env_shell_file_path:
                            env_shell_file_paths.append( env_shell_file_path )
                        else:
                            error_message = "Skipping tool dependency definition because unable to locate env.sh file for tool dependency "
                            error_message += "type %s, name %s, version %s for repository %s" % \
                                ( str( tool_dependency_type ), str( tool_dependency_name ), str( tool_dependency_version ), str( repository.name ) )
                            log.debug( error_message )
                            continue
                    else:
                        error_message = "Skipping tool dependency definition because unable to locate tool dependency "
                        error_message += "type %s, name %s, version %s for repository %s" % \
                            ( str( tool_dependency_type ), str( tool_dependency_name ), str( tool_dependency_version ), str( repository.name ) )
                        log.debug( error_message )
                        continue
                else:
                    error_message = "Skipping invalid tool dependency definition: type %s, name %s, version %s." % \
                        ( str( tool_dependency_type ), str( tool_dependency_name ), str( tool_dependency_version ) )
                    log.debug( error_message )
                    continue
        else:
            error_message = "Skipping set_environment_for_install definition because unable to locate required installed tool shed repository: "
            error_message += "toolshed %s, name %s, owner %s, changeset_revision %s." % \
                ( str( toolshed ), str( repository_name ), str( repository_owner ), str( changeset_revision ) )
            log.debug( error_message )
    else:
        error_message = "Skipping invalid set_environment_for_install definition: toolshed %s, name %s, owner %s, changeset_revision %s." % \
            ( str( toolshed ), str( repository_name ), str( repository_owner ), str( changeset_revision ) )
        log.debug( error_message )
    return env_shell_file_paths

def get_env_var_values( install_dir ):
    env_var_dict = {}
    env_var_dict[ 'INSTALL_DIR' ] = install_dir
    env_var_dict[ 'system_install' ] = install_dir
    # If the Python interpreter is 64bit then we can safely assume that the underlying system is also 64bit.
    env_var_dict[ '__is64bit__' ] = sys.maxsize > 2**32
    return env_var_dict

def isbz2( file_path ):
    return checkers.is_bz2( file_path )

def isgzip( file_path ):
    return checkers.is_gzip( file_path )

def isjar( file_path ):
    return iszip( file_path ) and file_path.endswith( '.jar' )

def istar( file_path ):
    return tarfile.is_tarfile( file_path )

def iszip( file_path ):
    return checkers.check_zip( file_path )

def make_directory( full_path ):
    if not os.path.exists( full_path ):
        os.makedirs( full_path )

def move_directory_files( current_dir, source_dir, destination_dir ):
    source_directory = os.path.abspath( os.path.join( current_dir, source_dir ) )
    destination_directory = os.path.join( destination_dir )
    if not os.path.isdir( destination_directory ):
        os.makedirs( destination_directory )
    for file_name in os.listdir( source_directory ):
        source_file = os.path.join( source_directory, file_name )
        destination_file = os.path.join( destination_directory, file_name )
        shutil.move( source_file, destination_file )

def move_file( current_dir, source, destination_dir ):
    source_file = os.path.abspath( os.path.join( current_dir, source ) )
    destination_directory = os.path.join( destination_dir )
    if not os.path.isdir( destination_directory ):
        os.makedirs( destination_directory )
    shutil.move( source_file, destination_directory )

def tar_extraction_directory( file_path, file_name ):
    """Try to return the correct extraction directory."""
    file_name = file_name.strip()
    extensions = [ '.tar.gz', '.tgz', '.tar.bz2', '.tar', '.zip' ]
    for extension in extensions:
        if file_name.find( extension ) > 0:
            dir_name = file_name[ :-len( extension ) ]
            if os.path.exists( os.path.abspath( os.path.join( file_path, dir_name ) ) ):
                return dir_name
    if os.path.exists( os.path.abspath( os.path.join( file_path, file_name ) ) ):
        return os.path.abspath( file_path )
    raise ValueError( 'Could not find path to file %s' % os.path.abspath( os.path.join( file_path, file_name ) ) )

def url_download( install_dir, downloaded_file_name, download_url, extract=True ):
    file_path = os.path.join( install_dir, downloaded_file_name )
    src = None
    dst = None
    try:
        src = urllib2.urlopen( download_url )
        dst = open( file_path, 'wb' )
        while True:
            chunk = src.read( suc.CHUNK_SIZE )
            if chunk:
                dst.write( chunk )
            else:
                break
    except:
        raise
    finally:
        if src:
            src.close()
        if dst:
            dst.close()
    if extract:
        if istar( file_path ):
            # <action type="download_by_url">http://sourceforge.net/projects/samtools/files/samtools/0.1.18/samtools-0.1.18.tar.bz2</action>
            extract_tar( file_path, install_dir )
            dir = tar_extraction_directory( install_dir, downloaded_file_name )
        elif isjar( file_path ):
            dir = os.path.curdir
        elif iszip( file_path ):
            # <action type="download_by_url">http://downloads.sourceforge.net/project/picard/picard-tools/1.56/picard-tools-1.56.zip</action>
            zip_archive_extracted = extract_zip( file_path, install_dir )
            dir = zip_extraction_directory( install_dir, downloaded_file_name )
        else:
            dir = os.path.abspath( install_dir )
    else:
        dir = os.path.abspath( install_dir )
    return dir

def zip_extraction_directory( file_path, file_name ):
    """Try to return the correct extraction directory."""
    files = [ filename for filename in os.listdir( file_path ) if not filename.endswith( '.zip' ) ]
    if len( files ) > 1:
        return os.path.abspath( file_path )
    elif len( files ) == 1:
        # If there is only on file it should be a directory.
        if os.path.isdir( os.path.join( file_path, files[ 0 ] ) ):
            return os.path.abspath( os.path.join( file_path, files[ 0 ] ) )
    raise ValueError( 'Could not find directory for the extracted file %s' % os.path.abspath( os.path.join( file_path, file_name ) ) )

def zipfile_ok( path_to_archive ):
    """
    This function is a bit pedantic and not functionally necessary.  It checks whether there is no file pointing outside of the extraction, 
    because ZipFile.extractall() has some potential security holes.  See python zipfile documentation for more details.
    """
    basename = os.path.realpath( os.path.dirname( path_to_archive ) )
    zip_archive = zipfile.ZipFile( path_to_archive )
    for member in zip_archive.namelist():
        member_path = os.path.realpath( os.path.join( basename, member ) )
        if not member_path.startswith( basename ):
            return False
    return True


def __shellquote(s):
    """
    Quote and escape the supplied string for use in shell expressions.
    """
    return "'" + s.replace("'", "'\\''") + "'"
