admin_user = None
admin_user_private_role = None
admin_email = 'admin@hygenomics.com'
admin_username = 'admin'

test_user_1 = None
test_user_1_private_role = None
test_user_1_email = 'test-1@bx.psu.edu'
test_user_1_name = 'user1'

test_user_2 = None
test_user_2_private_role = None
test_user_2_email = 'test-2@bx.psu.edu'
test_user_2_name = 'user2'

test_user_3 = None
test_user_3_private_role = None
test_user_3_email = 'test-3@bx.psu.edu'
test_user_3_name = 'user3'

complex_repository_dependency_template = '''<?xml version="1.0"?>
<tool_dependency>
    <package name="${package}" version="${version}">
${dependency_lines}
    </package>
</tool_dependency>
'''

new_repository_dependencies_xml = '''<?xml version="1.0"?>
<repositories${description}>
${dependency_lines}
</repositories>
'''

new_repository_dependencies_line = '''    <repository toolshed="${toolshed_url}" name="${repository_name}" owner="${owner}" changeset_revision="${changeset_revision}"${prior_installation_required} />'''

# Set a 3 minute timeout for repository installation. This should be sufficient, since we're not installing tool dependencies.
repository_installation_timeout = 180
