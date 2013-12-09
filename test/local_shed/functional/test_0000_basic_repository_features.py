from local_shed.base.twilltestcase import ShedTwillTestCase, common, os
import local_shed.base.test_db_util as test_db_util
from local_shed.hy_tools.create_category import insertCategoryInfo
from local_shed.hy_tools.repositories import repositories, changeSets

repository_name = 'filtering_0000'
repository_description = "Galaxy's filtering tool for test 0000"
repository_long_description = "Long description of Galaxy's filtering tool for test 0000"
tmail = "@test.com"


class TestBasicRepositoryFeatures( ShedTwillTestCase ):
    '''Test core repository features.'''
    
    def test_0000_initiate_users( self ):
        """Create necessary user accounts and login as an admin user."""
        for info in repositories:
            email = info["owner"]+tmail
            username = info["owner"]
            self.logout()
            self.login( email=email, username=username )
            tmp_user = test_db_util.get_user( email )
            tmp_user_private_role = test_db_util.get_private_role( tmp_user )
        self.logout()
        self.login( email=common.admin_email, username=common.admin_username )
        admin_user = test_db_util.get_user( common.admin_email )
        assert admin_user is not None, 'Problem retrieving user with email %s from the database' % common.admin_email
        admin_user_private_role = test_db_util.get_private_role( admin_user )
        
    def test_0005_create_categories( self ):
        """Create categories for this test suite"""
        #category_list = insertCategoryInfo()
        #for key in category_list:
        #    self.create_category(name = key, description = category_list[key])
        self.create_category(name = "demo", description = "huayi test")

        
    def test_0010_create_repository( self ):
        """Create the repositories"""
        category = test_db_util.get_category_by_name( 'demo' )
        for info in repositories[:]:
            self.logout()
            email = info["owner"]+tmail
            username = info["owner"]
            self.login( email=email, username=username )
            #if info["name"] =="abyss_tool":
                #continue
            #strings_displayed = [ 'Repository %s' % "'%s'" % info["name"],
                                  #'Repository %s has been created' % "'%s'" % info["name"]]
            self.get_or_create_repository( name=info["name"],
                                           description=info["description"], 
                                           long_description="hg",
                                           owner=username,
                                           category_id=self.security.encode_id( category.id ), 
                                           strings_displayed=[])
            repository = test_db_util.get_repository_by_name_and_owner( info["name"], username )
            if changeSets[info["id"]] != []:
                try:
                    self.upload_file( repository, 
                                      filename='../hy_tools/repo/%s/%s/%s_%s%s'%(info["owner"],info["name"],info["name"],changeSets[info["id"]],".tar.gz"), 
                                      filepath=None,
                                      valid_tools_only=True,
                                      uncompress_file=True,
                                      remove_repo_files_not_in_tar=True,
                                      commit_message="add "+info["name"],
                                      strings_displayed=[], 
                                      strings_not_displayed=[] )
                except:
                    #import commands
                    #commands.getstatus("echo \""+e.value+"\">lei")
                    continue
        
        
    #def test_0030_upload_filtering_1_1_0( self ):
        #"""Upload filtering_1.1.0.tar to the repository"""

