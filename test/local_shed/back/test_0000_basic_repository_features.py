from local_shed.base.twilltestcase import ShedTwillTestCase, common, os
import local_shed.base.test_db_util as test_db_util
from local_shed.hy_tools.create_category import insertCategoryInfo
from local_shed.hy_tools.repositories import repositories

repository_name = 'filtering_0000'
repository_description = "Galaxy's filtering tool for test 0000"
repository_long_description = "Long description of Galaxy's filtering tool for test 0000"


class TestBasicRepositoryFeatures( ShedTwillTestCase ):
    '''Test core repository features.'''
    
    def test_0000_initiate_users( self ):
        """Create necessary user accounts and login as an admin user."""
        self.logout()
        self.login( email=common.admin_email, username=common.admin_username )
        admin_user = test_db_util.get_user( common.admin_email )
        assert admin_user is not None, 'Problem retrieving user with email %s from the database' % common.admin_email
        admin_user_private_role = test_db_util.get_private_role( admin_user )
        
    def test_0005_create_categories( self ):
        """Create categories for this test suite"""
        category_list = insertCategoryInfo()
        for key in category_list:
            self.create_category(name = key, description = category_list[key])
        
    def test_0010_create_repository( self ):
        """Create the repositories"""
        self.logout()
        self.login( email=common.admin_email, username=common.admin_username )
        category = test_db_util.get_category_by_name( 'Assembly' )
        for info in repositories[:5]:
            strings_displayed = [ 'Repository %s' % "'%s'" % info["name"],
                                  'Repository %s has been created' % "'%s'" % info["name"]]
            self.get_or_create_repository( name=info["name"],
                                       description=info["description"], 
                                       long_description=info["long_description"], 
                                       owner=common.admin_username,
                                       category_id=self.security.encode_id( category.id ), 
                                       #category_id=1,
                                       strings_displayed=strings_displayed)
        
    def test_0015_edit_repository( self ):
        """Edit the repository name, description, and long description"""
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        new_name = "renamed_filtering"
        new_description = "Edited filtering tool"
        new_long_description = "Edited long description"
        self.edit_repository_information( repository, repo_name=new_name, description=new_description, long_description=new_long_description )
        
    def test_0020_change_repository_category( self ):
        """Change the categories associated with the filtering repository"""
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.edit_repository_categories( repository, 
                                         categories_to_add=[ "Test 0000 Basic Repository Features 2" ], 
                                         categories_to_remove=[ "Test 0000 Basic Repository Features 1" ] )
        
    def test_0025_grant_write_access( self ):
        '''Grant write access to another user'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.grant_write_access( repository, usernames=[ common.test_user_2_name ] )
        self.revoke_write_access( repository, common.test_user_2_name )
        
    def test_0030_upload_filtering_1_1_0( self ):
        """Upload filtering_1.1.0.tar to the repository"""
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.upload_file( repository, 
                          filename='filtering/filtering_1.1.0.tar', 
                          filepath=None,
                          valid_tools_only=True,
                          uncompress_file=True,
                          remove_repo_files_not_in_tar=True,
                          commit_message="Uploaded filtering 1.1.0",
                          strings_displayed=[], 
                          strings_not_displayed=[] )
        
    def test_0035_verify_repository( self ):
        '''Display basic repository pages'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        latest_changeset_revision = self.get_repository_tip( repository )
        self.check_for_valid_tools( repository, strings_displayed=[ 'Filter1' ] )
        self.check_count_of_metadata_revisions_associated_with_repository( repository, metadata_count=1 )
        tip = self.get_repository_tip( repository )
        tool_guid = '%s/repos/user1/filtering_0000/Filter1/1.1.0' % self.url.replace( 'http://', '' ).rstrip( '/' )
        tool_metadata_strings_displayed = [ tool_guid,
                                            '1.1.0', # The tool version.
                                            'Filter1', # The tool ID.
                                            'Filter', # The tool name.
                                            'data on any column using simple expressions' ] # The tool description.
        tool_page_strings_displayed = [ 'Filter (version 1.1.0)' ]
        self.check_repository_tools_for_changeset_revision( repository,
                                                            tip,
                                                            tool_metadata_strings_displayed=tool_metadata_strings_displayed,
                                                            tool_page_strings_displayed=tool_page_strings_displayed )
        self.check_repository_metadata( repository, tip_only=False )
        self.browse_repository( repository, strings_displayed=[ "Repository '%s' revision" % repository.name, '(repository tip)' ] )
        self.display_repository_clone_page( common.test_user_1_name, 
                                            repository_name, 
                                            strings_displayed=[ 'Uploaded filtering 1.1.0', latest_changeset_revision ] )
        
    def test_0040_alter_repository_states( self ):
        '''Test toggling the malicious and deprecated repository flags.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.logout()
        self.login( email=common.admin_email, username=common.admin_username )
        self.set_repository_malicious( repository, 
                                       set_malicious=True, 
                                       strings_displayed=[ 'The repository tip has been defined as malicious.' ] )
        self.set_repository_malicious( repository, 
                                       set_malicious=False, 
                                       strings_displayed=[ 'The repository tip has been defined as <b>not</b> malicious.' ] )
        self.logout()
        self.login( email=common.test_user_1_email, username=common.test_user_1_name )
        self.set_repository_deprecated( repository, 
                                        strings_displayed=[ 'has been marked as deprecated' ] )
        strings_displayed = [ 'This repository has been marked as deprecated', 'Mark repository as not deprecated' ]
        self.display_manage_repository_page( repository, 
                                             strings_displayed=strings_displayed,
                                             strings_not_displayed=[ 'Upload files', 'Reset all repository metadata' ] )
        self.browse_repository( repository, strings_not_displayed=[ 'Upload files' ] )
        self.set_repository_deprecated( repository, 
                                        strings_displayed=[ 'has been marked as not deprecated' ],
                                        set_deprecated=False )
        strings_displayed = [ 'Mark repository as deprecated', 'Upload files', 'Reset all repository metadata' ]
        self.display_manage_repository_page( repository, strings_displayed=strings_displayed )
        
    def test_0045_display_repository_tip_file( self ):
        '''Display the contents of filtering.xml in the repository tip revision'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.display_repository_file_contents( repository=repository,
                                               filename='filtering.xml',
                                               filepath=None,
                                               strings_displayed=[ '1.1.0' ],
                                               strings_not_displayed=[] )
        
    def test_0050_upload_filtering_txt_file( self ):
        '''Upload filtering.txt file associated with tool version 1.1.0.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.upload_file( repository, 
                          filename='filtering/filtering_0000.txt', 
                          filepath=None,
                          valid_tools_only=True,
                          uncompress_file=False,
                          remove_repo_files_not_in_tar=False,
                          commit_message="Uploaded filtering.txt",
                          strings_displayed=[], 
                          strings_not_displayed=[] )
        self.display_manage_repository_page( repository, strings_displayed=[ 'Readme&nbsp;file&nbsp;for&nbsp;filtering&nbsp;1.1.0' ] )
        
    def test_0055_upload_filtering_test_data( self ):
        '''Upload filtering test data.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.upload_file( repository, 
                          filename='filtering/filtering_test_data.tar', 
                          filepath=None,
                          valid_tools_only=True,
                          uncompress_file=True,
                          remove_repo_files_not_in_tar=False,
                          commit_message="Uploaded filtering test data",
                          strings_displayed=[], 
                          strings_not_displayed=[] )
        self.display_repository_file_contents( repository=repository,
                                               filename='1.bed',
                                               filepath='test-data',
                                               strings_displayed=[],
                                               strings_not_displayed=[] )
        self.check_repository_metadata( repository, tip_only=True )
        
    def test_0060_upload_filtering_2_2_0( self ):
        '''Upload filtering version 2.2.0'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.upload_file( repository, 
                          filename='filtering/filtering_2.2.0.tar', 
                          filepath=None,
                          valid_tools_only=True,
                          uncompress_file=True,
                          remove_repo_files_not_in_tar=False,
                          commit_message="Uploaded filtering 2.2.0",
                          strings_displayed=[], 
                          strings_not_displayed=[] )
        
    def test_0065_verify_filtering_repository( self ):
        '''Verify the new tool versions and repository metadata.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        category = test_db_util.get_category_by_name( 'Test 0000 Basic Repository Features 1' )
        tip = self.get_repository_tip( repository )
        self.check_for_valid_tools( repository )
        strings_displayed = [ 'Select a revision' ]
        self.display_manage_repository_page( repository, strings_displayed=strings_displayed )
        self.check_count_of_metadata_revisions_associated_with_repository( repository, metadata_count=2 )
        tool_guid = '%s/repos/user1/filtering_0000/Filter1/2.2.0' % self.url.replace( 'http://', '' ).rstrip( '/' )
        tool_metadata_strings_displayed = [ tool_guid,
                                            '2.2.0', # The tool version.
                                            'Filter1', # The tool ID.
                                            'Filter', # The tool name.
                                            'data on any column using simple expressions' ] # The tool description.
        tool_page_strings_displayed = [ 'Filter (version 2.2.0)' ]
        self.check_repository_tools_for_changeset_revision( repository,
                                                            tip,
                                                            tool_metadata_strings_displayed=tool_metadata_strings_displayed,
                                                            tool_page_strings_displayed=tool_page_strings_displayed )
        self.check_repository_metadata( repository, tip_only=False )
        
    def test_0070_upload_readme_txt_file( self ):
        '''Upload readme.txt file associated with tool version 2.2.0.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.upload_file( repository, 
                          filename='readme.txt', 
                          filepath=None,
                          valid_tools_only=True,
                          uncompress_file=False,
                          remove_repo_files_not_in_tar=False,
                          commit_message="Uploaded readme.txt",
                          strings_displayed=[], 
                          strings_not_displayed=[] )
        self.display_manage_repository_page( repository, strings_displayed=[ 'This&nbsp;is&nbsp;a&nbsp;readme&nbsp;file.' ] )
        # Verify that there is a different readme file for each metadata revision.
        metadata_revisions = self.get_repository_metadata_revisions( repository )
        self.display_manage_repository_page( repository, 
                                             strings_displayed=[ 'Readme&nbsp;file&nbsp;for&nbsp;filtering&nbsp;1.1.0', 
                                                                 'This&nbsp;is&nbsp;a&nbsp;readme&nbsp;file.' ] )
        
    def test_0075_delete_readme_txt_file( self ):
        '''Delete the readme.txt file.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.delete_files_from_repository( repository, filenames=[ 'readme.txt' ] )
        self.check_count_of_metadata_revisions_associated_with_repository( repository, metadata_count=2 )
        self.display_manage_repository_page( repository, strings_displayed=[ 'Readme&nbsp;file&nbsp;for&nbsp;filtering&nbsp;1.1.0' ] )
        
    def test_0080_search_for_valid_filter_tool( self ):
        '''Search for the filtering tool by tool ID, name, and version.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        tip_changeset = self.get_repository_tip( repository )
        search_fields = dict( tool_id='Filter1', tool_name='filter', tool_version='2.2.0' )
        self.search_for_valid_tools( search_fields=search_fields, strings_displayed=[ tip_changeset ], strings_not_displayed=[] )
        
    def test_0085_verify_repository_metadata( self ):
        '''Verify that resetting the metadata does not change it.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.verify_unchanged_repository_metadata( repository )
        
    def test_0090_verify_reserved_repository_name_handling( self ):
        '''Check that reserved repository names are handled correctly.'''
        category = test_db_util.get_category_by_name( 'Test 0000 Basic Repository Features 1' )
        error_message = 'The term <b>repos</b> is a reserved word in the tool shed, so it cannot be used as a repository name.'
        self.get_or_create_repository( name='repos', 
                                       description=repository_description, 
                                       long_description=repository_long_description, 
                                       owner=common.test_user_1_name,
                                       category_id=self.security.encode_id( category.id ), 
                                       strings_displayed=[ error_message ] )
        
    def test_0100_verify_reserved_username_handling( self ):
        '''Check that reserved usernames are handled correctly.'''
        self.logout()
        self.login( email='baduser@bx.psu.edu', username='repos' )
        test_user_1 = test_db_util.get_user( 'baduser@bx.psu.edu' )
        assert test_user_1 is None, 'Creating user with public name "repos" succeeded.'
        error_message = 'The term <b>repos</b> is a reserved word in the tool shed, so it cannot be used as a public user name.'
        self.check_for_strings( strings_displayed=[ error_message ] )
        
    def test_0105_contact_repository_owner( self ):
        '''Fill out and submit the form to contact the owner of a repository.'''
        '''
        This test should not actually send the email, since functional tests are designed to function without
        any external network connection. The embedded tool shed server these tests are running against has been configured
        with an SMTP server address that will not and should not resolve correctly. However, since the successful sending of
        the email is the last step in the process, this will verify functional correctness of all preceding steps.
        '''
        self.logout()
        self.login( email=common.test_user_2_email, username=common.test_user_2_name )
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        message = 'This is a test message.'
        strings_displayed = [ 'Contact the owner of the repository named', repository.name, 'streamline appropriate communication' ]
        post_submit_strings_displayed = [ 'An error occurred sending your message by email' ]
        self.send_message_to_repository_owner( repository=repository, 
                                               message=message, 
                                               strings_displayed=strings_displayed,
                                               post_submit_strings_displayed=post_submit_strings_displayed )
        
    def test_0110_delete_filtering_repository( self ):
        '''Delete the filtering_0000 repository and verify that it no longer has any downloadable revisions.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.logout()
        self.login( email=common.admin_email, username=common.admin_username )
        self.delete_repository( repository )
        # Explicitly reload all metadata revisions from the database, to ensure that we have the current status of the downloadable flag.
        for metadata_revision in repository.metadata_revisions:
            test_db_util.refresh( metadata_revision )
        # Marking a repository as deleted should result in no metadata revisions being downloadable.
        assert True not in [ metadata.downloadable for metadata in repository.metadata_revisions ]
    
    def test_0115_undelete_filtering_repository( self ):
        '''Undelete the filtering_0000 repository and verify that it now has two downloadable revisions.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        self.logout()
        self.login( email=common.admin_email, username=common.admin_username )
        self.undelete_repository( repository )
        # Explicitly reload all metadata revisions from the database, to ensure that we have the current status of the downloadable flag.
        for metadata_revision in repository.metadata_revisions:
            test_db_util.refresh( metadata_revision )
        # Marking a repository as undeleted should result in all previously downloadable metadata revisions being downloadable again.
        # In this case, there should be two downloadable revisions, one for filtering 1.1.0 and one for filtering 2.2.0.
        assert True in [ metadata.downloadable for metadata in repository.metadata_revisions ]
        assert len( repository.downloadable_revisions ) == 2
        
    def test_0120_enable_email_notifications( self ):
        '''Enable email notifications for test user 2 on filtering_0000.'''
        # Log in as test_user_2
        self.logout()
        self.login( email=common.test_user_2_email, username=common.test_user_2_name )
        # Get the repository, so we can pass the encoded repository id and browse_repositories method to the set_email_alerts method.
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        strings_displayed = [ 'Total alerts added: 1, total alerts removed: 0' ]
        self.enable_email_alerts( repository, strings_displayed=strings_displayed )
        
    def test_0125_upload_new_readme_file( self ):
        '''Upload a new readme file to the filtering_0000 repository and verify that there is no error.'''
        self.logout()
        self.login( email=common.test_user_1_email, username=common.test_user_1_name )
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        # Upload readme.txt to the filtering_0000 repository and verify that it is now displayed.
        self.upload_file( repository, 
                          filename='filtering/readme.txt', 
                          filepath=None,
                          valid_tools_only=True,
                          uncompress_file=False,
                          remove_repo_files_not_in_tar=False,
                          commit_message="Uploaded new readme.txt with invalid ascii characters.",
                          strings_displayed=[], 
                          strings_not_displayed=[] )
        self.display_manage_repository_page( repository, strings_displayed=[ 'These&nbsp;characters&nbsp;should&nbsp;not' ] )
        
    def test_0130_verify_handling_of_invalid_characters( self ):
        '''Load the above changeset in the change log and confirm that there is no server error displayed.'''
        repository = test_db_util.get_repository_by_name_and_owner( repository_name, common.test_user_1_name )
        changeset_revision = self.get_repository_tip( repository )
        repository_id = self.security.encode_id( repository.id )
        changelog_tuples = self.get_repository_changelog_tuples( repository )
        revision_number = -1
        revision_hash = '000000000000'
        for numeric_changeset, changeset_hash in changelog_tuples:
            if str( changeset_hash ) == str( changeset_revision ):
                revision_number = numeric_changeset
                revision_hash = changeset_hash
                break 
        # Check for the changeset revision, repository name, owner username, 'repos' in the clone url, and the captured
        # unicode decoding error message. 
        strings_displayed = [ 'Changeset %d:%s' % ( revision_number, revision_hash ), 'filtering_0000', 'user1', 'repos', 'added:',
                              '+These&nbsp;characters&nbsp;should&nbsp;not' ]
        self.load_changeset_in_tool_shed( repository_id, changeset_revision, strings_displayed=strings_displayed )
