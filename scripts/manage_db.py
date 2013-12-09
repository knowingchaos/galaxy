import sys, os.path, logging

new_path = [ os.path.join( os.getcwd(), "lib" ) ]
new_path.extend( sys.path[1:] ) # remove scripts/ from the path
sys.path = new_path

from galaxy import eggs

eggs.require( "decorator" )
eggs.require( "Tempita" )
eggs.require( "SQLAlchemy" )
eggs.require( "sqlalchemy_migrate" )

from migrate.versioning.shell import main
from ConfigParser import SafeConfigParser

from galaxy.model.orm import dialect_to_egg

log = logging.getLogger( __name__ )

if sys.argv[-1] in [ 'tool_shed' ]:
    # Need to pop the last arg so the command line args will be correct
    # for sqlalchemy-migrate 
    webapp = sys.argv.pop()
    config_file = 'tool_shed_wsgi.ini'
    repo = 'lib/galaxy/webapps/tool_shed/model/migrate'
else:
    # Poor man's optparse
    config_file = 'universe_wsgi.ini'
    if '-c' in sys.argv:
        pos = sys.argv.index( '-c' )
        sys.argv.pop(pos)
        config_file = sys.argv.pop( pos )
    if not os.path.exists( config_file ):
        print "Galaxy config file does not exist (hint: use '-c config.ini' for non-standard locations): %s" % config_file
        sys.exit( 1 )
    repo = 'lib/galaxy/model/migrate'

cp = SafeConfigParser()
cp.read( config_file )

if cp.has_option( "app:main", "database_connection" ):
    db_url = cp.get( "app:main", "database_connection" )
elif cp.has_option( "app:main", "database_file" ):
    db_url = "sqlite:///%s?isolation_level=IMMEDIATE" % cp.get( "app:main", "database_file" )
else:
    db_url = "sqlite:///./database/universe.sqlite?isolation_level=IMMEDIATE"

dialect = ( db_url.split( ':', 1 ) )[0]
try:
    egg = dialect_to_egg[dialect]
    try:
        eggs.require( egg )
        log.debug( "%s egg successfully loaded for %s dialect" % ( egg, dialect ) )
    except:
        # If the module is in the path elsewhere (i.e. non-egg), it'll still load.
        log.warning( "%s egg not found, but an attempt will be made to use %s anyway" % ( egg, dialect ) )
except KeyError:
    # Let this go, it could possibly work with db's we don't support
    log.error( "database_connection contains an unknown SQLAlchemy database dialect: %s" % dialect )

main( repository=repo, url=db_url )
