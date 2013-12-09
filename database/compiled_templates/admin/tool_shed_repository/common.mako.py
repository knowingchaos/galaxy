# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384082586.5432169
_template_filename=u'templates/admin/tool_shed_repository/common.mako'
_template_uri=u'/admin/tool_shed_repository/common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['repository_installation_status_updater', 'render_readme_section', 'browse_files', 'tool_dependency_installation_updater', 'repository_installation_updater', 'dependency_status_updater', 'render_dependencies_section']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7f1ba011f050', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba011f050')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba011f050')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 70
        __M_writer(u'\n\n')
        # SOURCE LINE 163
        __M_writer(u'\n\n')
        # SOURCE LINE 186
        __M_writer(u'\n\n')
        # SOURCE LINE 237
        __M_writer(u'\n\n')
        # SOURCE LINE 295
        __M_writer(u'\n\n')
        # SOURCE LINE 312
        __M_writer(u'\n\n')
        # SOURCE LINE 332
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_repository_installation_status_updater(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba011f050')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 239
        __M_writer(u'\n    <script type="text/javascript">\n        // Tool shed repository status updater - used to update the installation status on the Repository Installation Grid. \n        // Looks for changes in repository installation status using an async request. Keeps calling itself (via setTimeout) until\n        // repository installation status is not one of: \'New\', \'Cloning\', \'Setting tool versions\', \'Installing tool dependencies\',\n        // \'Loading proprietary datatypes\'.\n        var tool_shed_repository_status_updater = function( repository_status_list ) {\n            // See if there are any items left to track\n            //alert( "repository_status_list start " + repository_status_list.toSource() );\n            var empty = true;\n            for ( var item in repository_status_list ) {\n                //alert( "item" + item.toSource() );\n                //alert( "repository_status_list[item] " + repository_status_list[item].toSource() );\n                //alert( "repository_status_list[item][\'status\']" + repository_status_list[item][\'status\'] );\n                if (repository_status_list[item][\'status\'] != \'Installed\'){\n                    empty = false;\n                    break;\n                }\n            }\n            if ( ! empty ) {\n                setTimeout( function() { tool_shed_repository_status_updater_callback( repository_status_list ) }, 3000 );\n            }\n        };\n        var tool_shed_repository_status_updater_callback = function( repository_status_list ) {\n            //alert( repository_status_list );\n            //alert( repository_status_list.toSource() );\n            var ids = [];\n            var status_list = [];\n            $.each( repository_status_list, function( index, repository_status ) {\n                //alert(\'repository_status \'+ repository_status.toSource() );\n                //alert(\'id \'+ repository_status[\'id\'] );\n                //alert( \'status\'+ repository_status[\'status\'] );\n                ids.push( repository_status[ \'id\' ] );\n                status_list.push( repository_status[ \'status\' ] );\n            });\n            // Make ajax call\n            $.ajax( {\n                type: "POST",\n                url: "')
        # SOURCE LINE 277
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='repository_installation_status_updates' )))
        __M_writer(u'",\n                dataType: "json",\n                data: { ids: ids.join( "," ), status_list: status_list.join( "," ) },\n                success : function( data ) {\n                    $.each( data, function( index, val ) {\n                        // Replace HTML\n                        var cell1 = $( "#RepositoryStatus-" + val[ \'id\' ] );\n                        cell1.html( val[ \'html_status\' ] );\n                        repository_status_list[ index ] = val;\n                    });\n                    tool_shed_repository_status_updater( repository_status_list ); \n                },\n                error: function() {\n                    alert( "tool_shed_repository_status_updater_callback failed..." );\n                }\n            });\n        };\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_readme_section(context,containers_dict):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba011f050')._populate(_import_ns, [u'*'])
        render_folder = _import_ns.get('render_folder', context.get('render_folder', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 165
        __M_writer(u'\n    ')
        # SOURCE LINE 166

        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
        
        readme_files_root_folder = containers_dict.get( 'readme_files', None )
            
        
        # SOURCE LINE 176
        __M_writer(u'\n')
        # SOURCE LINE 177
        if readme_files_root_folder:
            # SOURCE LINE 178
            __M_writer(u'        <p/>\n        <div class="form-row">\n            ')
            # SOURCE LINE 180
            row_counter = RowCounter() 
            
            __M_writer(u'\n            <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table">\n                ')
            # SOURCE LINE 182
            __M_writer(unicode(render_folder( readme_files_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
            __M_writer(u'\n            </table>\n        </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_browse_files(context,title_text,directory_path):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba011f050')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            $("#tree").ajaxComplete(function(event, XMLHttpRequest, ajaxOptions) {\n                _log("debug", "ajaxComplete: %o", this); // dom element listening\n            });\n            // --- Initialize sample trees\n            $("#tree").dynatree({\n                title: "')
        # SOURCE LINE 11
        __M_writer(unicode(title_text))
        __M_writer(u'",\n                rootVisible: true,\n                minExpandLevel: 0, // 1: root node is not collapsible\n                persist: false,\n                checkbox: true,\n                selectMode: 3,\n                onPostInit: function(isReloading, isError) {\n                    //alert("reloading: "+isReloading+", error:"+isError);\n                    logMsg("onPostInit(%o, %o) - %o", isReloading, isError, this);\n                    // Re-fire onActivate, so the text is updated\n                    this.reactivate();\n                }, \n                fx: { height: "toggle", duration: 200 },\n                // initAjax is hard to fake, so we pass the children as object array:\n                initAjax: {url: "')
        # SOURCE LINE 25
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='open_folder' )))
        __M_writer(u'",\n                           dataType: "json", \n                           data: { folder_path: "')
        # SOURCE LINE 27
        __M_writer(unicode(directory_path))
        __M_writer(u'" },\n                },\n                onLazyRead: function(dtnode){\n                    dtnode.appendAjax({\n                        url: "')
        # SOURCE LINE 31
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='open_folder' )))
        __M_writer(u'", \n                        dataType: "json",\n                        data: { folder_path: dtnode.data.key },\n                    });\n                },\n                onSelect: function(select, dtnode) {\n                    // Display list of selected nodes\n                    var selNodes = dtnode.tree.getSelectedNodes();\n                    // convert to title/key array\n                    var selKeys = $.map(selNodes, function(node) {\n                        return node.data.key;\n                    });\n                },\n                onActivate: function(dtnode) {\n                    var cell = $("#file_contents");\n                    var selected_value;\n                     if (dtnode.data.key == \'root\') {\n                        selected_value = "')
        # SOURCE LINE 48
        __M_writer(unicode(directory_path))
        __M_writer(u'/";\n                    } else {\n                        selected_value = dtnode.data.key;\n                    };\n                    if (selected_value.charAt(selected_value.length-1) != \'/\') {\n                        // Make ajax call\n                        $.ajax( {\n                            type: "POST",\n                            url: "')
        # SOURCE LINE 56
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='get_file_contents' )))
        __M_writer(u'",\n                            dataType: "json",\n                            data: { file_path: selected_value },\n                            success : function( data ) {\n                                cell.html( \'<label>\'+data+\'</label>\' )\n                            }\n                        });\n                    } else {\n                        cell.html( \'\' );\n                    };\n                },\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tool_dependency_installation_updater(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba011f050')._populate(_import_ns, [u'*'])
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 297
        __M_writer(u'\n    ')
        # SOURCE LINE 298
 
        can_update = False
        if query.count():
            # Get the first tool dependency to get to the tool shed repository.
            tool_dependency = query[0]
            tool_shed_repository = tool_dependency.tool_shed_repository
            can_update = tool_shed_repository.tool_dependencies_being_installed or tool_shed_repository.missing_tool_dependencies
            
        
        # SOURCE LINE 305
        __M_writer(u'\n')
        # SOURCE LINE 306
        if can_update:
            # SOURCE LINE 307
            __M_writer(u'        <script type="text/javascript">\n            // Tool dependency installation status updater\n            tool_dependency_status_updater( [')
            # SOURCE LINE 309
            __M_writer(unicode( ",".join( [ '{"id" : "%s", "status" : "%s"}' % ( trans.security.encode_id( td.id ), td.status ) for td in query ] ) ))
            __M_writer(u' ] );\n        </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_repository_installation_updater(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba011f050')._populate(_import_ns, [u'*'])
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 314
        __M_writer(u'\n    ')
        # SOURCE LINE 315

        can_update = False
        if query.count():
            for tool_shed_repository in query:
                if tool_shed_repository.status not in [ trans.model.ToolShedRepository.installation_status.INSTALLED,
                                                        trans.model.ToolShedRepository.installation_status.ERROR,
                                                        trans.model.ToolShedRepository.installation_status.DEACTIVATED,
                                                        trans.model.ToolShedRepository.installation_status.UNINSTALLED ]:
                    can_update = True
                    break
            
        
        # SOURCE LINE 325
        __M_writer(u'\n')
        # SOURCE LINE 326
        if can_update:
            # SOURCE LINE 327
            __M_writer(u'        <script type="text/javascript">\n            // Tool shed repository installation status updater\n            tool_shed_repository_status_updater( [')
            # SOURCE LINE 329
            __M_writer(unicode( ",".join( [ '{"id" : "%s", "status" : "%s"}' % ( trans.security.encode_id( tsr.id ), tsr.status ) for tsr in query ] ) ))
            __M_writer(u' ] );\n        </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dependency_status_updater(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba011f050')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 188
        __M_writer(u'\n    <script type="text/javascript">\n        // Tool dependency status updater - used to update the installation status on the Tool Dependencies Grid. \n        // Looks for changes in tool dependency installation status using an async request. Keeps calling itself \n        // (via setTimeout) until dependency installation status is neither \'Installing\' nor \'Building\'.\n        var tool_dependency_status_updater = function( dependency_status_list ) {\n            // See if there are any items left to track\n            var empty = true;\n            for ( var item in dependency_status_list ) {\n                //alert( "item" + item.toSource() );\n                //alert( "dependency_status_list[item] " + dependency_status_list[item].toSource() );\n                //alert( "dependency_status_list[item][\'status\']" + dependency_status_list[item][\'status\'] );\n                if ( dependency_status_list[item][\'status\'] != \'Installed\' ) {\n                    empty = false;\n                    break;\n                }\n            }\n            if ( ! empty ) {\n                setTimeout( function() { tool_dependency_status_updater_callback( dependency_status_list ) }, 3000 );\n            }\n        };\n        var tool_dependency_status_updater_callback = function( dependency_status_list ) {\n            var ids = [];\n            var status_list = [];\n            $.each( dependency_status_list, function( index, dependency_status ) {\n                ids.push( dependency_status[ \'id\' ] );\n                status_list.push( dependency_status[ \'status\' ] );\n            });\n            // Make ajax call\n            $.ajax( {\n                type: "POST",\n                url: "')
        # SOURCE LINE 219
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='tool_dependency_status_updates' )))
        __M_writer(u'",\n                dataType: "json",\n                data: { ids: ids.join( "," ), status_list: status_list.join( "," ) },\n                success : function( data ) {\n                    $.each( data, function( index, val ) {\n                        // Replace HTML\n                        var cell1 = $( "#ToolDependencyStatus-" + val[ \'id\' ] );\n                        cell1.html( val[ \'html_status\' ] );\n                        dependency_status_list[ index ] = val;\n                    });\n                    tool_dependency_status_updater( dependency_status_list ); \n                },\n                error: function() {\n                    alert( "tool_dependency_status_updater_callback failed..." );\n                }\n            });\n        };\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_dependencies_section(context,install_repository_dependencies_check_box,install_tool_dependencies_check_box,containers_dict):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba011f050')._populate(_import_ns, [u'*'])
        render_folder = _import_ns.get('render_folder', context.get('render_folder', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 72
        __M_writer(u'\n    <style type="text/css">\n        #dependency_table{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px; \n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n    </style>\n    ')
        # SOURCE LINE 83

        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
        
        repository_dependencies_root_folder = containers_dict[ 'repository_dependencies' ]
        tool_dependencies_root_folder = containers_dict[ 'tool_dependencies' ]
        missing_tool_dependencies_root_folder = containers_dict[ 'missing_tool_dependencies' ]
        env_settings_heaader_row_displayed = False
        package_header_row_displayed = False
            
        
        # SOURCE LINE 97
        __M_writer(u'\n    <div class="form-row">\n        <div class="toolParamHelp" style="clear: both;">\n            <p>\n                These dependencies can be automatically handled with the installed repository, providing significant benefits, and \n                Galaxy includes various features to manage them.\n            </p>\n        </div>\n    </div>\n')
        # SOURCE LINE 106
        if repository_dependencies_root_folder:
            # SOURCE LINE 107
            if install_repository_dependencies_check_box is not None:
                # SOURCE LINE 108
                __M_writer(u'            <div class="form-row">\n                <label>Handle repository dependencies?</label>\n                ')
                # SOURCE LINE 110
                __M_writer(unicode(install_repository_dependencies_check_box.get_html()))
                __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n                    Un-check to skip automatic installation of these additional repositories required by this repository.\n                </div>\n            </div>\n            <div style="clear: both"></div>\n')
                pass
            # SOURCE LINE 117
            __M_writer(u'        <div class="form-row">\n            <p/>\n            ')
            # SOURCE LINE 119
            row_counter = RowCounter() 
            
            __M_writer(u'\n            <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table">\n                ')
            # SOURCE LINE 121
            __M_writer(unicode(render_folder( repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
            __M_writer(u'\n            </table>\n            <div style="clear: both"></div>\n        </div>\n')
            pass
        # SOURCE LINE 126
        if tool_dependencies_root_folder or missing_tool_dependencies_root_folder:
            # SOURCE LINE 127
            if install_tool_dependencies_check_box is not None:
                # SOURCE LINE 128
                __M_writer(u'            <div class="form-row">\n                <label>Handle tool dependencies?</label>\n                ')
                # SOURCE LINE 130
                disabled = trans.app.config.tool_dependency_dir is None 
                
                __M_writer(u'\n                ')
                # SOURCE LINE 131
                __M_writer(unicode(install_tool_dependencies_check_box.get_html( disabled=disabled )))
                __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n')
                # SOURCE LINE 133
                if disabled:
                    # SOURCE LINE 134
                    __M_writer(u'                        Set the tool_dependency_dir configuration value in your Galaxy config to automatically handle tool dependencies.\n')
                    # SOURCE LINE 135
                else:
                    # SOURCE LINE 136
                    __M_writer(u'                        Un-check to skip automatic handling of these tool dependencies.\n')
                    pass
                # SOURCE LINE 138
                __M_writer(u'                </div>\n            </div>\n            <div style="clear: both"></div>\n')
                pass
            # SOURCE LINE 142
            if tool_dependencies_root_folder:
                # SOURCE LINE 143
                __M_writer(u'            <div class="form-row">\n                <p/>\n                ')
                # SOURCE LINE 145
                row_counter = RowCounter() 
                
                __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="dependency_table">\n                    ')
                # SOURCE LINE 147
                __M_writer(unicode(render_folder( tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                </table>\n                <div style="clear: both"></div>\n            </div>\n')
                pass
            # SOURCE LINE 152
            if missing_tool_dependencies_root_folder:
                # SOURCE LINE 153
                __M_writer(u'            <div class="form-row">\n                <p/>\n                ')
                # SOURCE LINE 155
                row_counter = RowCounter() 
                
                __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="dependency_table">\n                    ')
                # SOURCE LINE 157
                __M_writer(unicode(render_folder( missing_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                </table>\n                <div style="clear: both"></div>\n            </div>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


