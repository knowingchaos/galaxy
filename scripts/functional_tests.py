#!/usr/bin/env python

import os, sys, shutil, tempfile, re
from ConfigParser import SafeConfigParser

# Assume we are run from the galaxy root directory, add lib to the python path
cwd = os.getcwd()
new_path = [ os.path.join( cwd, "lib" ), os.path.join( cwd, "test" ) ]
new_path.extend( sys.path[1:] )
sys.path = new_path

from base.util import parse_tool_panel_config

from galaxy import eggs

eggs.require( "nose" )
eggs.require( "NoseHTML" )
eggs.require( "NoseTestDiff" )
eggs.require( "twill==0.9" )
eggs.require( "Paste" )
eggs.require( "PasteDeploy" )
eggs.require( "Cheetah" )

# this should not be required, but it is under certain conditions, thanks to this bug:
# http://code.google.com/p/python-nose/issues/detail?id=284
eggs.require( "pysqlite" )

import atexit, logging, os, os.path, sys, tempfile
import twill, unittest, time
import subprocess, sys, threading, random
import httplib, socket
from paste import httpserver
import galaxy.app
from galaxy.app import UniverseApplication
from galaxy.web import buildapp
from galaxy import tools
from galaxy.util import bunch
from galaxy import util
from galaxy.util.json import to_json_string

import nose.core
import nose.config
import nose.loader
import nose.plugins.manager

log = logging.getLogger( "functional_tests.py" )

default_galaxy_test_host = "localhost"
default_galaxy_test_port_min = 8000
default_galaxy_test_port_max = 9999
default_galaxy_locales = 'en'
default_galaxy_test_file_dir = "test-data"
migrated_tool_panel_config = 'migrated_tools_conf.xml'
installed_tool_panel_configs = [ 'shed_tool_conf.xml' ]

# should this serve static resources (scripts, images, styles, etc.)
STATIC_ENABLED = True

def get_static_settings():
    """Returns dictionary of the settings necessary for a galaxy App
    to be wrapped in the static middleware.

    This mainly consists of the filesystem locations of url-mapped
    static resources.
    """
    cwd = os.getcwd()
    static_dir = os.path.join( cwd, 'static' )
    #TODO: these should be copied from universe_wsgi.ini
    return dict(
        #TODO: static_enabled needed here?
        static_enabled      = True,
        static_cache_time   = 360,
        static_dir          = static_dir,
        static_images_dir   = os.path.join( static_dir, 'images', '' ),
        static_favicon_dir  = os.path.join( static_dir, 'favicon.ico' ),
        static_scripts_dir  = os.path.join( static_dir, 'scripts', '' ),
        static_style_dir    = os.path.join( static_dir, 'june_2007_style', 'blue' ),
        static_robots_txt   = os.path.join( static_dir, 'robots.txt' ),
    )

def get_webapp_global_conf():
    """Get the global_conf dictionary sent as the first argument to app_factory.
    """
    # (was originally sent 'dict()') - nothing here for now except static settings
    global_conf = dict()
    if STATIC_ENABLED:
        global_conf.update( get_static_settings() )
    return global_conf

def generate_config_file( input_filename, output_filename, config_items ):
    '''
    Generate a config file with the configuration that has been defined for the embedded web application.
    This is mostly relevant when setting metadata externally, since the script for doing that does not
    have access to app.config.
    ''' 
    cp = SafeConfigParser()
    cp.read( input_filename )
    config_items_by_section = []
    for label, value in config_items:
        found = False
        # Attempt to determine the correct section for this configuration option.
        for section in cp.sections():
            if cp.has_option( section, label ):
                config_tuple = section, label, value
                config_items_by_section.append( config_tuple )
                found = True
                continue
        # Default to app:main if no section was found.
        if not found:
            config_tuple = 'app:main', label, value
            config_items_by_section.append( config_tuple )
    print( config_items_by_section )
    # Replace the default values with the provided configuration.
    for section, label, value in config_items_by_section:
        
        if cp.has_option( section, label ):
            cp.remove_option( section, label )
        cp.set( section, label, str( value ) )
    fh = open( output_filename, 'w' )
    cp.write( fh )
    fh.close()

def run_tests( test_config ):
    loader = nose.loader.TestLoader( config=test_config )
    plug_loader = test_config.plugins.prepareTestLoader( loader )
    if plug_loader is not None:
        loader = plug_loader
    tests = loader.loadTestsFromNames( test_config.testNames )
    test_runner = nose.core.TextTestRunner( stream=test_config.stream,
                                            verbosity=test_config.verbosity,
                                            config=test_config )
    plug_runner = test_config.plugins.prepareTestRunner( test_runner )
    if plug_runner is not None:
        test_runner = plug_runner
    return test_runner.run( tests )

def main():    
    # ---- Configuration ------------------------------------------------------
    galaxy_test_host = os.environ.get( 'GALAXY_TEST_HOST', default_galaxy_test_host )
    galaxy_test_port = os.environ.get( 'GALAXY_TEST_PORT', None )
    galaxy_test_save = os.environ.get( 'GALAXY_TEST_SAVE', None)
    tool_path = os.environ.get( 'GALAXY_TEST_TOOL_PATH', 'tools' )
    if 'HTTP_ACCEPT_LANGUAGE' not in os.environ:
        os.environ[ 'HTTP_ACCEPT_LANGUAGE' ] = default_galaxy_locales
    testing_migrated_tools = '-migrated' in sys.argv
    testing_installed_tools = '-installed' in sys.argv

    if testing_migrated_tools or testing_installed_tools:
        sys.argv.pop()
        # Store a jsonified dictionary of tool_id : GALAXY_TEST_FILE_DIR pairs.
        galaxy_tool_shed_test_file = 'shed_tools_dict'
        # We need the upload tool for functional tests, so we'll create a temporary tool panel config that defines it.
        fd, tmp_tool_panel_conf = tempfile.mkstemp()
        os.write( fd, '<?xml version="1.0"?>\n' )
        os.write( fd, '<toolbox>\n' )
        os.write( fd, '<tool file="data_source/upload.xml"/>\n' )
        os.write( fd, '</toolbox>\n' )
        os.close( fd )
        tool_config_file = tmp_tool_panel_conf
        galaxy_test_file_dir = None
        library_import_dir = None
        user_library_import_dir = None
        # Exclude all files except test_toolbox.py.
        ignore_files = ( re.compile( r'^test_[adghlmsu]*' ), re.compile( r'^test_ta*' ) )
    else:
        tool_config_file = os.environ.get( 'GALAXY_TEST_TOOL_CONF', 'tool_conf.xml' )
        galaxy_test_file_dir = os.environ.get( 'GALAXY_TEST_FILE_DIR', default_galaxy_test_file_dir )
        if not os.path.isabs( galaxy_test_file_dir ):
            galaxy_test_file_dir = os.path.join( os.getcwd(), galaxy_test_file_dir )
        library_import_dir = galaxy_test_file_dir
        user_library_import_dir = os.path.join( galaxy_test_file_dir, 'users' )
        ignore_files = ()

    start_server = 'GALAXY_TEST_EXTERNAL' not in os.environ
    if os.path.exists( 'tool_data_table_conf.test.xml' ):
        tool_data_table_config_path = 'tool_data_table_conf.test.xml'
    else:    
        tool_data_table_config_path = 'tool_data_table_conf.xml'
    shed_tool_data_table_config = 'shed_tool_data_table_conf.xml'
    tool_dependency_dir = os.environ.get( 'GALAXY_TOOL_DEPENDENCY_DIR', None )
    use_distributed_object_store = os.environ.get( 'GALAXY_USE_DISTRIBUTED_OBJECT_STORE', False )
    galaxy_test_tmp_dir = os.environ.get( 'GALAXY_TEST_TMP_DIR', None )
    if galaxy_test_tmp_dir is None:
        galaxy_test_tmp_dir = tempfile.mkdtemp()
    
    if start_server:
        psu_production = False
        galaxy_test_proxy_port = None
        if 'GALAXY_TEST_PSU_PRODUCTION' in os.environ:
            if not galaxy_test_port:
                raise Exception( 'Please set GALAXY_TEST_PORT to the port to which the proxy server will proxy' )
            galaxy_test_proxy_port = os.environ.get( 'GALAXY_TEST_PROXY_PORT', None )
            if not galaxy_test_proxy_port:
                raise Exception( 'Please set GALAXY_TEST_PROXY_PORT to the port on which the proxy server is listening' )
            base_file_path = os.environ.get( 'GALAXY_TEST_BASE_FILE_PATH', None )
            if not base_file_path:
                raise Exception( 'Please set GALAXY_TEST_BASE_FILE_PATH to the directory which will contain the dataset files directory' )
            base_new_file_path = os.environ.get( 'GALAXY_TEST_BASE_NEW_FILE_PATH', None )
            if not base_new_file_path:
                raise Exception( 'Please set GALAXY_TEST_BASE_NEW_FILE_PATH to the directory which will contain the temporary directory' )
            database_connection = os.environ.get( 'GALAXY_TEST_DBURI', None )
            if not database_connection:
                raise Exception( 'Please set GALAXY_TEST_DBURI to the URI of the database to be used for tests' )
            nginx_upload_store = os.environ.get( 'GALAXY_TEST_NGINX_UPLOAD_STORE', None )
            if not nginx_upload_store:
                raise Exception( 'Please set GALAXY_TEST_NGINX_UPLOAD_STORE to the path where the nginx upload module places uploaded files' )
            tool_config_file = 'tool_conf.xml.main'
            default_cluster_job_runner = os.environ.get( 'GALAXY_TEST_DEFAULT_CLUSTER_JOB_RUNNER', 'pbs:///' )
            file_path = tempfile.mkdtemp( dir=base_file_path )
            new_file_path = tempfile.mkdtemp( dir=base_new_file_path )
            cluster_files_directory = os.path.join( new_file_path, 'pbs' )
            job_working_directory = os.path.join( new_file_path, 'job_working_directory' )
            os.mkdir( cluster_files_directory )
            os.mkdir( job_working_directory )
            kwargs = dict( database_engine_option_pool_size = '10',
                           database_engine_option_max_overflow = '20',
                           database_engine_option_strategy = 'threadlocal',
                           nginx_x_accel_redirect_base = '/_x_accel_redirect',
                           nginx_upload_store = nginx_upload_store,
                           nginx_upload_path = '/_upload',
                           allow_library_path_paste = 'True',
                           cluster_files_directory = cluster_files_directory,
                           job_working_directory = job_working_directory,
                           outputs_to_working_directory = 'True',
                           static_enabled = 'False',
                           debug = 'False',
                           track_jobs_in_database = 'True',
                           job_scheduler_policy = 'FIFO',
                           start_job_runners = 'pbs',
                           default_cluster_job_runner = default_cluster_job_runner )
            psu_production = True
        else:
            # Configure the database path.
            if 'GALAXY_TEST_DBPATH' in os.environ:
                galaxy_db_path = os.environ[ 'GALAXY_TEST_DBPATH' ]
            else: 
                tempdir = tempfile.mkdtemp( dir=galaxy_test_tmp_dir )
                galaxy_db_path = os.path.join( tempdir, 'database' )
            # Configure the paths Galaxy needs to  test tools.
            file_path = os.path.join( galaxy_db_path, 'files' )
            new_file_path = tempfile.mkdtemp( prefix='new_files_path_', dir=tempdir )
            job_working_directory = tempfile.mkdtemp( prefix='job_working_directory_', dir=tempdir )
            if 'GALAXY_TEST_DBURI' in os.environ:
                database_connection = os.environ['GALAXY_TEST_DBURI']
            else:
                database_connection = 'sqlite:///' + os.path.join( db_path, 'universe.sqlite' )
            kwargs = {}
        for dir in file_path, new_file_path:
            try:
                if not os.path.exists( dir ):
                    os.makedirs( dir )
            except OSError:
                pass

    # ---- Build Application -------------------------------------------------- 
    app = None 
    if start_server:
        kwargs = dict( admin_users = 'test@bx.psu.edu',
                       allow_library_path_paste = True,
                       allow_user_creation = True,
                       allow_user_deletion = True,
                       database_connection = database_connection,
                       datatype_converters_config_file = "datatype_converters_conf.xml.sample",
                       file_path = file_path,
                       id_secret = 'changethisinproductiontoo',
                       job_queue_workers = 5,
                       job_working_directory = job_working_directory,
                       library_import_dir = library_import_dir,
                       log_destination = "stdout",
                       new_file_path = new_file_path,
                       running_functional_tests = True,
                       shed_tool_data_table_config = shed_tool_data_table_config,
                       template_path = "templates",
                       test_conf = "test.conf",
                       tool_config_file = tool_config_file,
                       tool_data_table_config_path = tool_data_table_config_path,
                       tool_path = tool_path,
                       tool_parse_help = False,
                       update_integrated_tool_panel = False,
                       use_heartbeat = False,
                       user_library_import_dir = user_library_import_dir )
        if psu_production:
            kwargs[ 'global_conf' ] = None
        if not database_connection.startswith( 'sqlite://' ):
            kwargs[ 'database_engine_option_max_overflow' ] = '20'
            kwargs[ 'database_engine_option_pool_size' ] = '10'
        if tool_dependency_dir is not None:
            kwargs[ 'tool_dependency_dir' ] = tool_dependency_dir
        if use_distributed_object_store:
            kwargs[ 'object_store' ] = 'distributed'
            kwargs[ 'distributed_object_store_config_file' ] = 'distributed_object_store_conf.xml.sample'
        # If the user has passed in a path for the .ini file, do not overwrite it.
        galaxy_config_file = os.environ.get( 'GALAXY_TEST_INI_FILE', None )
        if not galaxy_config_file:
            galaxy_config_file = os.path.join( galaxy_test_tmp_dir, 'functional_tests_wsgi.ini' )
            config_items = []
            for label in kwargs:
                config_tuple = label, kwargs[ label ]
                config_items.append( config_tuple )
            # Write a temporary file, based on universe_wsgi.ini.sample, using the configuration options defined above.
            generate_config_file( 'universe_wsgi.ini.sample', galaxy_config_file, config_items )
        # Set the global_conf[ '__file__' ] option to the location of the temporary .ini file, which gets passed to set_metadata.sh.
        kwargs[ 'global_conf' ] = get_webapp_global_conf()
        kwargs[ 'global_conf' ][ '__file__' ] = galaxy_config_file
        kwargs[ 'config_file' ] = galaxy_config_file
        # Build the Universe Application
        app = UniverseApplication( **kwargs )
        log.info( "Embedded Universe application started" )

    # ---- Run webserver ------------------------------------------------------
    server = None
    
    if start_server:
        webapp = buildapp.app_factory( kwargs[ 'global_conf' ], app=app,
            use_translogger=False, static_enabled=STATIC_ENABLED )
        if galaxy_test_port is not None:
            server = httpserver.serve( webapp, host=galaxy_test_host, port=galaxy_test_port, start_loop=False )
        else:
            random.seed()
            for i in range( 0, 9 ):
                try:
                    galaxy_test_port = str( random.randint( default_galaxy_test_port_min, default_galaxy_test_port_max ) )
                    log.debug( "Attempting to serve app on randomly chosen port: %s" % galaxy_test_port )
                    server = httpserver.serve( webapp, host=galaxy_test_host, port=galaxy_test_port, start_loop=False )
                    break
                except socket.error, e:
                    if e[0] == 98:
                        continue
                    raise
            else:
                raise Exception( "Unable to open a port between %s and %s to start Galaxy server" % ( default_galaxy_test_port_min, default_galaxy_test_port_max ) )
        if galaxy_test_proxy_port:
            os.environ['GALAXY_TEST_PORT'] = galaxy_test_proxy_port
        else:
            os.environ['GALAXY_TEST_PORT'] = galaxy_test_port

        t = threading.Thread( target=server.serve_forever )
        t.start()
        # Test if the server is up
        for i in range( 10 ):
            conn = httplib.HTTPConnection( galaxy_test_host, galaxy_test_port ) # directly test the app, not the proxy
            conn.request( "GET", "/" )
            if conn.getresponse().status == 200:
                break
            time.sleep( 0.1 )
        else:
            raise Exception( "Test HTTP server did not return '200 OK' after 10 tries" )
        # Test if the proxy server is up
        if psu_production:
            conn = httplib.HTTPConnection( galaxy_test_host, galaxy_test_proxy_port ) # directly test the app, not the proxy
            conn.request( "GET", "/" )
            if not conn.getresponse().status == 200:
                raise Exception( "Test HTTP proxy server did not return '200 OK'" )
        log.info( "Embedded web server started" )
    # ---- Load toolbox for generated tests -----------------------------------
    # We don't add the tests to the path until everything is up and running
    new_path = [ os.path.join( cwd, "test" ) ]
    new_path.extend( sys.path[1:] )
    sys.path = new_path
    import functional.test_toolbox
    # ---- Find tests ---------------------------------------------------------
    if galaxy_test_proxy_port:
        log.info( "Functional tests will be run against %s:%s" % ( galaxy_test_host, galaxy_test_proxy_port ) )
    else:
        log.info( "Functional tests will be run against %s:%s" % ( galaxy_test_host, galaxy_test_port ) )
    success = False
    try:
        tool_configs = app.config.tool_configs
        # What requires these? Handy for (eg) functional tests to save outputs?        
        if galaxy_test_save:
            os.environ[ 'GALAXY_TEST_SAVE' ] = galaxy_test_save
        # Pass in through script setenv, will leave a copy of ALL test validate files        
        os.environ[ 'GALAXY_TEST_HOST' ] = galaxy_test_host
        if testing_migrated_tools or testing_installed_tools:
            shed_tools_dict = {}
            if testing_migrated_tools:
                has_test_data, shed_tools_dict = parse_tool_panel_config( migrated_tool_panel_config, shed_tools_dict )
            elif testing_installed_tools:
                for shed_tool_config in installed_tool_panel_configs:
                    has_test_data, shed_tools_dict = parse_tool_panel_config( shed_tool_config, shed_tools_dict )
            # Persist the shed_tools_dict to the galaxy_tool_shed_test_file.
            shed_tools_file = open( galaxy_tool_shed_test_file, 'w' )
            shed_tools_file.write( to_json_string( shed_tools_dict ) )
            shed_tools_file.close()
            if not os.path.isabs( galaxy_tool_shed_test_file ):
                galaxy_tool_shed_test_file = os.path.join( os.getcwd(), galaxy_tool_shed_test_file )
            os.environ[ 'GALAXY_TOOL_SHED_TEST_FILE' ] = galaxy_tool_shed_test_file
            if testing_installed_tools:
                # Eliminate the migrated_tool_panel_config from the app's tool_configs, append the list of installed_tool_panel_configs,
                # and reload the app's toolbox.
                relative_migrated_tool_panel_config = os.path.join( app.config.root, migrated_tool_panel_config )
                if relative_migrated_tool_panel_config in tool_configs:
                    tool_configs.remove( relative_migrated_tool_panel_config )
                for installed_tool_panel_config in installed_tool_panel_configs:
                    tool_configs.append( installed_tool_panel_config )
                app.toolbox = tools.ToolBox( tool_configs, app.config.tool_path, app )
            functional.test_toolbox.toolbox = app.toolbox
            functional.test_toolbox.build_tests( testing_shed_tools=True )
            test_config = nose.config.Config( env=os.environ, ignoreFiles=ignore_files, plugins=nose.plugins.manager.DefaultPluginManager() )
            test_config.configure( sys.argv )
            result = run_tests( test_config )    
            success = result.wasSuccessful()
            try:
                os.unlink( tmp_tool_panel_conf )
            except:
                log.info( "Unable to remove temporary file: %s" % tmp_tool_panel_conf )
            try:
                os.unlink( galaxy_tool_shed_test_file )
            except:
                log.info( "Unable to remove file: %s" % galaxy_tool_shed_test_file )
        else:
            functional.test_toolbox.toolbox = app.toolbox
            functional.test_toolbox.build_tests()
            if galaxy_test_file_dir:
                os.environ[ 'GALAXY_TEST_FILE_DIR' ] = galaxy_test_file_dir
            test_config = nose.config.Config( env=os.environ, ignoreFiles=ignore_files, plugins=nose.plugins.manager.DefaultPluginManager() )
            test_config.configure( sys.argv )
            result = run_tests( test_config )    
            success = result.wasSuccessful()
    except:
        log.exception( "Failure running tests" )
        
    log.info( "Shutting down" )
    # ---- Tear down -----------------------------------------------------------
    if server:
        log.info( "Shutting down embedded web server" )
        server.server_close()
        server = None
        log.info( "Embedded web server stopped" )
    if app:
        log.info( "Shutting down app" )
        app.shutdown()
        app = None
        log.info( "Embedded Universe application stopped" )
    try:
        if os.path.exists( tempdir ) and 'GALAXY_TEST_NO_CLEANUP' not in os.environ:
            log.info( "Cleaning up temporary files in %s" % tempdir )
            shutil.rmtree( tempdir )
        else:
            log.info( "GALAXY_TEST_NO_CLEANUP is on. Temporary files in %s" % tempdir )
    except:
        pass
    if psu_production and 'GALAXY_TEST_NO_CLEANUP' not in os.environ:
        for dir in ( file_path, new_file_path ):
            try:
                if os.path.exists( dir ):
                    log.info( 'Cleaning up temporary files in %s' % dir )
                    shutil.rmtree( dir )
            except:
                pass
    if success:
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit( main() )
