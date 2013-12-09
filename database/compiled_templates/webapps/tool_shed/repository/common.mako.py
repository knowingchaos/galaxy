# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384082586.7687681
_template_filename=u'templates/webapps/tool_shed/repository/common.mako'
_template_uri=u'/webapps/tool_shed/repository/common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_tool_dependency', 'render_not_tested', 'render_missing_test_component', 'render_folder', 'render_tool', 'render_clone_str', 'render_test_environment', 'container_javascripts', 'render_readme', 'render_tool_dependency_installation_error', 'render_repository_dependency', 'render_tool_test_results_css', 'render_datatype', 'render_failed_test', 'common_javascripts', 'render_valid_data_manager', 'render_repository_installation_error', 'render_invalid_repository_dependency', 'render_invalid_tool', 'render_workflow', 'render_repository_type_select_field', 'render_passed_test', 'render_repository_items', 'render_invalid_data_manager', 'render_sharable_str', 'render_invalid_tool_dependency']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 77
        __M_writer(u'\n\n')
        # SOURCE LINE 164
        __M_writer(u'\n\n')
        # SOURCE LINE 204
        __M_writer(u'         \n            \n')
        # SOURCE LINE 212
        __M_writer(u'\n\n')
        # SOURCE LINE 220
        __M_writer(u'\n\n')
        # SOURCE LINE 415
        __M_writer(u'\n\n')
        # SOURCE LINE 439
        __M_writer(u'\n\n')
        # SOURCE LINE 462
        __M_writer(u'\n\n')
        # SOURCE LINE 484
        __M_writer(u'\n\n')
        # SOURCE LINE 503
        __M_writer(u'\n\n')
        # SOURCE LINE 526
        __M_writer(u'\n\n')
        # SOURCE LINE 557
        __M_writer(u'\n\n')
        # SOURCE LINE 579
        __M_writer(u'\n\n')
        # SOURCE LINE 617
        __M_writer(u'\n\n')
        # SOURCE LINE 684
        __M_writer(u'\n\n')
        # SOURCE LINE 697
        __M_writer(u'\n\n')
        # SOURCE LINE 725
        __M_writer(u'\n\n')
        # SOURCE LINE 756
        __M_writer(u'\n\n')
        # SOURCE LINE 775
        __M_writer(u'\n\n')
        # SOURCE LINE 796
        __M_writer(u'\n\n')
        # SOURCE LINE 843
        __M_writer(u'\n\n')
        # SOURCE LINE 915
        __M_writer(u'\n\n')
        # SOURCE LINE 942
        __M_writer(u'\n\n')
        # SOURCE LINE 965
        __M_writer(u'\n\n')
        # SOURCE LINE 1007
        __M_writer(u'\n\n')
        # SOURCE LINE 1175
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency(context,tool_dependency,pad,parent,row_counter,row_is_header):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 845
        __M_writer(u'\n    ')
        # SOURCE LINE 846

        from galaxy.util import string_as_bool
        encoded_id = trans.security.encode_id( tool_dependency.id )
        is_missing = tool_dependency.installation_status not in [ 'Installed' ]
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 854
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 856
        if parent is not None:
            # SOURCE LINE 857
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 859
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 860
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        # SOURCE LINE 861
        if row_is_header:
            # SOURCE LINE 862
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.name )))
            __M_writer(u'\n')
            # SOURCE LINE 863
        elif trans.webapp.name == 'galaxy' and tool_dependency.tool_dependency_id:
            # SOURCE LINE 864
            if tool_dependency.repository_id and tool_dependency.installation_status in [ trans.model.ToolDependency.installation_status.INSTALLED ]:
                # SOURCE LINE 865
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_dependency', id=trans.security.encode_id( tool_dependency.tool_dependency_id ) )))
                __M_writer(u'">\n                        ')
                # SOURCE LINE 866
                __M_writer(filters.html_escape(unicode(tool_dependency.name )))
                __M_writer(u'\n                    </a>\n')
                # SOURCE LINE 868
            elif tool_dependency.installation_status not in [ trans.model.ToolDependency.installation_status.UNINSTALLED ]:
                # SOURCE LINE 869
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository_tool_dependencies', tool_dependency_ids=trans.security.encode_id( tool_dependency.tool_dependency_id ) )))
                __M_writer(u'">\n                        ')
                # SOURCE LINE 870
                __M_writer(unicode(tool_dependency.name))
                __M_writer(u'\n                    </a>\n')
                # SOURCE LINE 872
            else:
                # SOURCE LINE 873
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool_dependency.name )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 875
        else:
            # SOURCE LINE 876
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.name )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 878
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 879
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n            ')
        # SOURCE LINE 880

        if tool_dependency.version:
            version_str = tool_dependency.version
        else:
            version_str = ''
                    
        
        # SOURCE LINE 885
        __M_writer(u'\n            ')
        # SOURCE LINE 886
        __M_writer(filters.html_escape(unicode(version_str )))
        __M_writer(u'\n        </')
        # SOURCE LINE 887
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 888
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool_dependency.type )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 889
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n')
        # SOURCE LINE 890
        if trans.webapp.name == 'galaxy':
            # SOURCE LINE 891
            if is_missing:
                # SOURCE LINE 892
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool_dependency.installation_status )))
                __M_writer(u'\n')
                # SOURCE LINE 893
            elif tool_dependency.install_dir:
                # SOURCE LINE 894
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool_dependency.install_dir )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 896
        else:
            # SOURCE LINE 897
            if row_is_header:
                # SOURCE LINE 898
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool_dependency.is_orphan )))
                __M_writer(u'\n')
                # SOURCE LINE 899
            else:
                # SOURCE LINE 900
                __M_writer(u'                    ')

                if string_as_bool( str( tool_dependency.is_orphan ) ):
                    is_orphan = 'yes'
                else:
                    is_orphan = 'no'
                                    
                
                # SOURCE LINE 905
                __M_writer(u'\n                    ')
                # SOURCE LINE 906
                __M_writer(filters.html_escape(unicode(is_orphan )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 909
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 911

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 914
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_not_tested(context,not_tested,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 758
        __M_writer(u'\n    ')
        # SOURCE LINE 759
        encoded_id = trans.security.encode_id( not_tested.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 761
        if parent is not None:
            # SOURCE LINE 762
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 764
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 765
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="not_tested_table" class="tool_test_results">\n                <tr><td>')
        # SOURCE LINE 767
        __M_writer(filters.html_escape(unicode(not_tested.reason )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 771

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 774
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_missing_test_component(context,missing_test_component,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 559
        __M_writer(u'\n    ')
        # SOURCE LINE 560
        encoded_id = trans.security.encode_id( missing_test_component.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 562
        if parent is not None:
            # SOURCE LINE 563
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 565
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 566
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="missing_table" class="tool_test_results">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        # SOURCE LINE 568
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        # SOURCE LINE 569
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool guid:</b> ')
        # SOURCE LINE 570
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_guid )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Missing components:</b> <br/>')
        # SOURCE LINE 571
        __M_writer(filters.html_escape(unicode(missing_test_component.missing_components )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 575

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 578
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_folder(context,folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        enumerate = context.get('enumerate', UNDEFINED)
        def render_tool_dependency(tool_dependency,pad,parent,row_counter,row_is_header):
            return render_render_tool_dependency(context,tool_dependency,pad,parent,row_counter,row_is_header)
        def render_not_tested(not_tested,pad,parent,row_counter,row_is_header=False):
            return render_render_not_tested(context,not_tested,pad,parent,row_counter,row_is_header)
        def render_missing_test_component(missing_test_component,pad,parent,row_counter,row_is_header=False):
            return render_render_missing_test_component(context,missing_test_component,pad,parent,row_counter,row_is_header)
        def render_folder(folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
            return render_render_folder(context,folder,folder_pad,parent,row_counter,is_root_folder,render_repository_actions_for)
        def render_tool(tool,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
            return render_render_tool(context,tool,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_test_environment(test_environment,pad,parent,row_counter,row_is_header=False):
            return render_render_test_environment(context,test_environment,pad,parent,row_counter,row_is_header)
        def render_datatype(datatype,pad,parent,row_counter,row_is_header=False):
            return render_render_datatype(context,datatype,pad,parent,row_counter,row_is_header)
        def render_tool_dependency_installation_error(installation_error,pad,parent,row_counter,row_is_header=False):
            return render_render_tool_dependency_installation_error(context,installation_error,pad,parent,row_counter,row_is_header)
        def render_repository_dependency(repository_dependency,pad,parent,row_counter,row_is_header=False):
            return render_render_repository_dependency(context,repository_dependency,pad,parent,row_counter,row_is_header)
        def render_readme(readme,pad,parent,row_counter):
            return render_render_readme(context,readme,pad,parent,row_counter)
        def render_failed_test(failed_test,pad,parent,row_counter,row_is_header=False):
            return render_render_failed_test(context,failed_test,pad,parent,row_counter,row_is_header)
        def render_valid_data_manager(data_manager,pad,parent,row_counter,row_is_header=False):
            return render_render_valid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header)
        def render_repository_installation_error(installation_error,pad,parent,row_counter,row_is_header=False,is_current_repository=False):
            return render_render_repository_installation_error(context,installation_error,pad,parent,row_counter,row_is_header,is_current_repository)
        def render_invalid_repository_dependency(invalid_repository_dependency,pad,parent,row_counter):
            return render_render_invalid_repository_dependency(context,invalid_repository_dependency,pad,parent,row_counter)
        def render_invalid_tool(invalid_tool,pad,parent,row_counter,valid=True,render_repository_actions_for='tool_shed'):
            return render_render_invalid_tool(context,invalid_tool,pad,parent,row_counter,valid,render_repository_actions_for)
        def render_workflow(workflow,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_workflow(context,workflow,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        h = context.get('h', UNDEFINED)
        def render_passed_test(passed_test,pad,parent,row_counter,row_is_header=False):
            return render_render_passed_test(context,passed_test,pad,parent,row_counter,row_is_header)
        def render_invalid_data_manager(data_manager,pad,parent,row_counter,row_is_header=False):
            return render_render_invalid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header)
        str = context.get('str', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        def render_invalid_tool_dependency(invalid_tool_dependency,pad,parent,row_counter):
            return render_render_invalid_tool_dependency(context,invalid_tool_dependency,pad,parent,row_counter)
        __M_writer = context.writer()
        # SOURCE LINE 222
        __M_writer(u'\n    ')
        # SOURCE LINE 223

        encoded_id = trans.security.encode_id( folder.id )
        
        if is_root_folder:
            pad = folder_pad
            expander = h.url_for("/static/images/silk/resultset_bottom.png")
            folder_img = h.url_for("/static/images/silk/folder_page.png")
        else:
            pad = folder_pad + 20
            expander = h.url_for("/static/images/silk/resultset_next.png")
            folder_img = h.url_for("/static/images/silk/folder.png")
        my_row = None
            
        
        # SOURCE LINE 235
        __M_writer(u'\n')
        # SOURCE LINE 236
        if not is_root_folder:
            # SOURCE LINE 237
            __M_writer(u'        ')

            if parent is None:
                bg_str = 'bgcolor="#D8D8D8"'
            else:
                bg_str = ''
                    
            
            # SOURCE LINE 242
            __M_writer(u'\n        <tr id="folder-')
            # SOURCE LINE 243
            __M_writer(unicode(encoded_id))
            __M_writer(u'" ')
            __M_writer(unicode(bg_str))
            __M_writer(u' class="folderRow libraryOrFolderRow"\n')
            # SOURCE LINE 244
            if parent is not None:
                # SOURCE LINE 245
                __M_writer(u'                parent="')
                __M_writer(unicode(parent))
                __M_writer(u'"\n                style="display: none;"\n')
                pass
            # SOURCE LINE 248
            __M_writer(u'            >\n            ')
            # SOURCE LINE 249

            col_span_str = ''
            folder_label = str( folder.label )
            if folder.datatypes:
                col_span_str = 'colspan="4"'
            elif folder.label == 'Missing tool dependencies':
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - repository tools require handling of these missing dependencies</i>" % folder_label
                col_span_str = 'colspan="5"'
            elif folder.label in [ 'Installed repository dependencies', 'Repository dependencies', 'Missing repository dependencies' ]:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                elif folder.label not in [ 'Installed repository dependencies' ] and folder.parent.label not in [ 'Installation errors' ]:
                    folder_label = "%s<i> - installation of these additional repositories is required</i>" % folder_label
                if trans.webapp.name == 'galaxy':
                    col_span_str = 'colspan="4"'
            elif folder.label == 'Installation errors':
                folder_label = "%s<i> - no functional tests were run for any tools in this changeset revision</i>" % folder_label
            elif folder.label == 'Invalid repository dependencies':
                folder_label = "%s<i> - click the repository dependency to see why it is invalid</i>" % folder_label
            elif folder.label == 'Invalid tool dependencies':
                folder_label = "%s<i> - click the tool dependency to see why it is invalid</i>" % folder_label
            elif folder.label == 'Valid tools':
                col_span_str = 'colspan="3"'
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - click the name to preview the tool and use the pop-up menu to inspect all metadata</i>" % folder_label
            elif folder.invalid_tools:
                folder_label = "%s<i> - click the tool config file name to see why the tool is invalid</i>" % folder_label
            elif folder.tool_dependencies:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - repository tools require handling of these dependencies</i>" % folder_label
                col_span_str = 'colspan="4"'
            elif folder.workflows:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - click the name to view an SVG image of the workflow</i>" % folder_label
                col_span_str = 'colspan="4"'
            elif folder.valid_data_managers:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                col_span_str = 'colspan="3"'
            elif folder.invalid_data_managers:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                col_span_str = 'colspan="2"'
                        
            
            # SOURCE LINE 301
            __M_writer(u'\n            <td ')
            # SOURCE LINE 302
            __M_writer(unicode(col_span_str))
            __M_writer(u' style="padding-left: ')
            __M_writer(unicode(folder_pad))
            __M_writer(u'px;">\n                <span class="expandLink folder-')
            # SOURCE LINE 303
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                    <div style="float: left; margin-left: 2px;" class="expandLink folder-')
            # SOURCE LINE 304
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                        <a class="folder-')
            # SOURCE LINE 305
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click" href="javascript:void(0);">\n                            ')
            # SOURCE LINE 306
            __M_writer(unicode(folder_label))
            __M_writer(u'\n                        </a>\n                    </div>\n                </span>\n            </td>\n        </tr>\n        ')
            # SOURCE LINE 312

            my_row = row_counter.count
            row_counter.increment()  
                    
            
            # SOURCE LINE 315
            __M_writer(u'\n')
            pass
        # SOURCE LINE 317
        for sub_folder in folder.folders:
            # SOURCE LINE 318
            __M_writer(u'        ')
            __M_writer(unicode(render_folder( sub_folder, pad, parent=my_row, row_counter=row_counter, is_root_folder=False, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 320
        for readme in folder.readme_files:
            # SOURCE LINE 321
            __M_writer(u'        ')
            __M_writer(unicode(render_readme( readme, pad, my_row, row_counter )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 323
        for invalid_repository_dependency in folder.invalid_repository_dependencies:
            # SOURCE LINE 324
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_repository_dependency( invalid_repository_dependency, pad, my_row, row_counter )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 326
        for index, repository_dependency in enumerate( folder.repository_dependencies ):
            # SOURCE LINE 327
            __M_writer(u'        ')
            row_is_header = index == 0 
            
            __M_writer(u'\n        ')
            # SOURCE LINE 328
            __M_writer(unicode(render_repository_dependency( repository_dependency, pad, my_row, row_counter, row_is_header )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 330
        for invalid_tool_dependency in folder.invalid_tool_dependencies:
            # SOURCE LINE 331
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_tool_dependency( invalid_tool_dependency, pad, my_row, row_counter )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 333
        for index, tool_dependency in enumerate( folder.tool_dependencies ):
            # SOURCE LINE 334
            __M_writer(u'        ')
            row_is_header = index == 0 
            
            __M_writer(u'\n        ')
            # SOURCE LINE 335
            __M_writer(unicode(render_tool_dependency( tool_dependency, pad, my_row, row_counter, row_is_header )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 337
        if folder.valid_tools:
            # SOURCE LINE 338
            for index, tool in enumerate( folder.valid_tools ):
                # SOURCE LINE 339
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 340
                __M_writer(unicode(render_tool( tool, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 343
        for invalid_tool in folder.invalid_tools:
            # SOURCE LINE 344
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_tool( invalid_tool, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 346
        if folder.workflows:
            # SOURCE LINE 347
            for index, workflow in enumerate( folder.workflows ):
                # SOURCE LINE 348
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 349
                __M_writer(unicode(render_workflow( workflow, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 352
        if folder.datatypes:
            # SOURCE LINE 353
            for index, datatype in enumerate( folder.datatypes ):
                # SOURCE LINE 354
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 355
                __M_writer(unicode(render_datatype( datatype, pad, my_row, row_counter, row_is_header )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 358
        if folder.valid_data_managers:
            # SOURCE LINE 359
            for index, data_manager in enumerate( folder.valid_data_managers ):
                # SOURCE LINE 360
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 361
                __M_writer(unicode(render_valid_data_manager( data_manager, pad, my_row, row_counter, row_is_header )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 364
        if folder.invalid_data_managers:
            # SOURCE LINE 365
            for index, data_manager in enumerate( folder.invalid_data_managers ):
                # SOURCE LINE 366
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 367
                __M_writer(unicode(render_invalid_data_manager( data_manager, pad, my_row, row_counter, row_is_header )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 370
        if folder.test_environments:
            # SOURCE LINE 371
            for test_environment in folder.test_environments:
                # SOURCE LINE 372
                __M_writer(u'            ')
                __M_writer(unicode(render_test_environment( test_environment, pad, my_row, row_counter )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 375
        if folder.failed_tests:
            # SOURCE LINE 376
            for failed_test in folder.failed_tests:
                # SOURCE LINE 377
                __M_writer(u'            ')
                __M_writer(unicode(render_failed_test( failed_test, pad, my_row, row_counter )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 380
        if folder.not_tested:
            # SOURCE LINE 381
            for not_tested in folder.not_tested:
                # SOURCE LINE 382
                __M_writer(u'            ')
                __M_writer(unicode(render_not_tested( not_tested, pad, my_row, row_counter )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 385
        if folder.passed_tests:
            # SOURCE LINE 386
            for passed_test in folder.passed_tests:
                # SOURCE LINE 387
                __M_writer(u'            ')
                __M_writer(unicode(render_passed_test( passed_test, pad, my_row, row_counter )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 390
        if folder.missing_test_components:
            # SOURCE LINE 391
            for missing_test_component in folder.missing_test_components:
                # SOURCE LINE 392
                __M_writer(u'            ')
                __M_writer(unicode(render_missing_test_component( missing_test_component, pad, my_row, row_counter )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 395
        if folder.installation_errors:
            # SOURCE LINE 396
            for installation_error in folder.installation_errors:
                # SOURCE LINE 397
                __M_writer(u'            ')
                __M_writer(unicode(render_folder( installation_error, pad, my_row, row_counter )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 400
        if folder.tool_dependency_installation_errors:
            # SOURCE LINE 401
            for tool_dependency_installation_error in folder.tool_dependency_installation_errors:
                # SOURCE LINE 402
                __M_writer(u'            ')
                __M_writer(unicode(render_tool_dependency_installation_error( tool_dependency_installation_error, pad, my_row, row_counter )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 405
        if folder.repository_installation_errors:
            # SOURCE LINE 406
            for repository_installation_error in folder.repository_installation_errors:
                # SOURCE LINE 407
                __M_writer(u'            ')
                __M_writer(unicode(render_repository_installation_error( repository_installation_error, pad, my_row, row_counter, is_current_repository=False )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 410
        if folder.current_repository_installation_errors:
            # SOURCE LINE 411
            for repository_installation_error in folder.current_repository_installation_errors:
                # SOURCE LINE 412
                __M_writer(u'            ')
                __M_writer(unicode(render_repository_installation_error( repository_installation_error, pad, my_row, row_counter, is_current_repository=True )))
                __M_writer(u'\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool(context,tool,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 798
        __M_writer(u'\n    ')
        # SOURCE LINE 799

        encoded_id = trans.security.encode_id( tool.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 805
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 807
        if parent is not None:
            # SOURCE LINE 808
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 810
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n')
        # SOURCE LINE 811
        if row_is_header:
            # SOURCE LINE 812
            __M_writer(u'            <th style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">')
            __M_writer(filters.html_escape(unicode(tool.name )))
            __M_writer(u'</th>\n')
            # SOURCE LINE 813
        else:
            # SOURCE LINE 814
            __M_writer(u'            <td style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            # SOURCE LINE 815
            if tool.repository_id:
                # SOURCE LINE 816
                if trans.webapp.name == 'tool_shed':
                    # SOURCE LINE 817
                    __M_writer(u'                        <div style="float:left;" class="menubutton split popup" id="tool-')
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'-popup">\n                            <a class="view-info" href="')
                    # SOURCE LINE 818
                    __M_writer(unicode(h.url_for( controller='repository', action='display_tool', repository_id=trans.security.encode_id( tool.repository_id ), tool_config=tool.tool_config, changeset_revision=tool.changeset_revision, render_repository_actions_for=render_repository_actions_for )))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(unicode(tool.name )))
                    __M_writer(u'</a>\n                        </div>\n                        <div popupmenu="tool-')
                    # SOURCE LINE 820
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'-popup">\n                            <a class="action-button" href="')
                    # SOURCE LINE 821
                    __M_writer(unicode(h.url_for( controller='repository', action='view_tool_metadata', repository_id=trans.security.encode_id( tool.repository_id ), changeset_revision=tool.changeset_revision, tool_id=tool.tool_id, render_repository_actions_for=render_repository_actions_for )))
                    __M_writer(u'">View tool metadata</a>\n                        </div>\n')
                    # SOURCE LINE 823
                else:
                    # SOURCE LINE 824
                    if tool.repository_installation_status == trans.model.ToolShedRepository.installation_status.INSTALLED:
                        # SOURCE LINE 825
                        __M_writer(u'                            <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='view_tool_metadata', repository_id=trans.security.encode_id( tool.repository_id ), changeset_revision=tool.changeset_revision, tool_id=tool.tool_id )))
                        __M_writer(u'">')
                        __M_writer(filters.html_escape(unicode(tool.name )))
                        __M_writer(u'</a>\n')
                        # SOURCE LINE 826
                    else:
                        # SOURCE LINE 827
                        __M_writer(u'                            ')
                        __M_writer(filters.html_escape(unicode(tool.name )))
                        __M_writer(u'\n')
                        pass
                    pass
                # SOURCE LINE 830
            else:
                # SOURCE LINE 831
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool.name )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 833
            __M_writer(u'            </td>\n')
            pass
        # SOURCE LINE 835
        __M_writer(u'        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool.description )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 836
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool.version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n')
        # SOURCE LINE 838
        __M_writer(u'    </tr>\n    ')
        # SOURCE LINE 839

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 842
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_clone_str(context,repository):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 214
        __M_writer(u'\n    ')
        # SOURCE LINE 215

        from tool_shed.util.shed_util_common import generate_clone_url_for_repository_in_tool_shed
        clone_str = generate_clone_url_for_repository_in_tool_shed( trans, repository )
            
        
        # SOURCE LINE 218
        __M_writer(u'\n    hg clone <a href="')
        # SOURCE LINE 219
        __M_writer(unicode(clone_str))
        __M_writer(u'">')
        __M_writer(unicode(clone_str))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_test_environment(context,test_environment,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 917
        __M_writer(u'\n    ')
        # SOURCE LINE 918
        encoded_id = trans.security.encode_id( test_environment.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 920
        if parent is not None:
            # SOURCE LINE 921
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 923
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 924
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table class="grid" id="readme_table">\n                <tr><td><b>Time tested:</b> ')
        # SOURCE LINE 926
        __M_writer(filters.html_escape(unicode(test_environment.time_last_tested )))
        __M_writer(u'</td></tr>\n                <tr><td><b>System:</b> ')
        # SOURCE LINE 927
        __M_writer(filters.html_escape(unicode(test_environment.system )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Architecture:</b> ')
        # SOURCE LINE 928
        __M_writer(filters.html_escape(unicode(test_environment.architecture )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Python version:</b> ')
        # SOURCE LINE 929
        __M_writer(filters.html_escape(unicode(test_environment.python_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Galaxy revision:</b> ')
        # SOURCE LINE 930
        __M_writer(filters.html_escape(unicode(test_environment.galaxy_revision )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Galaxy database version:</b> ')
        # SOURCE LINE 931
        __M_writer(filters.html_escape(unicode(test_environment.galaxy_database_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed revision:</b> ')
        # SOURCE LINE 932
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_revision )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed database version:</b> ')
        # SOURCE LINE 933
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_database_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed mercurial version:</b> ')
        # SOURCE LINE 934
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_mercurial_version )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 938

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 941
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container_javascripts(context):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n    <script type="text/javascript">\n        var init_dependencies = function() {\n            var storage_id = "library-expand-state-')
        # SOURCE LINE 82
        __M_writer(unicode(trans.security.encode_id(10000)))
        __M_writer(u'";\n            var restore_folder_state = function() {\n                var state = $.jStorage.get(storage_id);\n                if (state) {\n                    for (var id in state) {\n                        if (state[id] === true) {\n                            var row = $("#" + id),\n                                index = row.parent().children().index(row);\n                            row.addClass("expanded").show();\n                            row.siblings().filter("tr[parent=\'" + index + "\']").show();\n                        }\n                    }\n                }\n            };\n            var save_folder_state = function() {\n                var state = {};\n                $("tr.folderRow").each( function() {\n                    var folder = $(this);\n                    state[folder.attr("id")] = folder.hasClass("expanded");\n                });\n                $.jStorage.set(storage_id, state);\n            };\n            $(".container-table").each(function() {\n                //var container_id = this.id.split( "-" )[0];\n                //alert( container_id );\n                var child_of_parent_cache = {};\n                // Recursively fill in children and descendants of each row\n                var process_row = function(q, parents) {\n                    // Find my index\n                    var parent = q.parent(),\n                        this_level = child_of_parent_cache[parent] || (child_of_parent_cache[parent] = parent.children());\n                    var index = this_level.index(q);\n                    // Find my immediate children\n                    var children = $(par_child_dict[index]);\n                    // Recursively handle them\n                    var descendants = children;\n                    children.each( function() {\n                        child_descendants = process_row( $(this), parents.add(q) );\n                        descendants = descendants.add(child_descendants);\n                    });\n                    // Set up expand / hide link\n                    var expand_fn = function() {\n                        if ( q.hasClass("expanded") ) {\n                            descendants.hide();\n                            descendants.removeClass("expanded");\n                            q.removeClass("expanded");\n                        } else {\n                            children.show();\n                            q.addClass("expanded");\n                        }\n                        save_folder_state();\n                    };\n                    $("." + q.attr("id") + "-click").click(expand_fn);\n                    // return descendants for use by parent\n                    return descendants;\n                }\n                // Initialize dict[parent_id] = rows_which_have_that_parent_id_as_parent_attr\n                var par_child_dict = {},\n                    no_parent = [];\n                $(this).find("tbody tr").each( function() {\n                    if ( $(this).attr("parent")) {\n                        var parent = $(this).attr("parent");\n                        if (par_child_dict[parent] !== undefined) {\n                            par_child_dict[parent].push(this);\n                        } else {\n                            par_child_dict[parent] = [this];\n                        }\n                    } else {\n                        no_parent.push(this);\n                    }                        \n                });\n                $(no_parent).each( function() {\n                    descendants = process_row( $(this), $([]) );\n                    descendants.hide();\n               });\n            });\n            restore_folder_state();\n        };\n        $(function() {\n            init_dependencies();\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_readme(context,readme,pad,parent,row_counter):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 581
        __M_writer(u'\n    ')
        # SOURCE LINE 582

        from tool_shed.util.shed_util_common import to_safe_string
        from galaxy.util import rst_to_html
        encoded_id = trans.security.encode_id( readme.id )
        render_rst = readme.name.endswith( '.rst' )
            
        
        # SOURCE LINE 587
        __M_writer(u'\n    <style type="text/css">\n        #readme_table{ table-layout:fixed;\n                       width:100%;\n                       overflow-wrap:normal;\n                       overflow:hidden;\n                       border:0px; \n                       word-break:keep-all;\n                       word-wrap:break-word;\n                       line-break:strict; }\n    </style>\n    <tr class="datasetRow"\n')
        # SOURCE LINE 599
        if parent is not None:
            # SOURCE LINE 600
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 602
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 603
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="readme_table">\n')
        # SOURCE LINE 605
        if render_rst:
            # SOURCE LINE 606
            __M_writer(u'                    <tr><td>')
            __M_writer(unicode( rst_to_html( readme.text ) ))
            __M_writer(u'</td></tr>\n')
            # SOURCE LINE 607
        else:
            # SOURCE LINE 608
            __M_writer(u'                    <tr><td>')
            __M_writer(unicode(readme.name))
            __M_writer(u'<br/>')
            __M_writer(unicode( to_safe_string( readme.text, to_html=True ) ))
            __M_writer(u'</td></tr>\n')
            pass
        # SOURCE LINE 610
        __M_writer(u'            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 613

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 616
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_installation_error(context,installation_error,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 699
        __M_writer(u'\n    ')
        # SOURCE LINE 700
        encoded_id = trans.security.encode_id( installation_error.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 702
        if parent is not None:
            # SOURCE LINE 703
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 705
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 706
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="td_install_error_table" class="tool_test_results">\n                <tr bgcolor="#FFFFCC">\n                    <th>Type</th><th>Name</th><th>Version</th>\n                </tr>\n                <tr>\n                    <td>')
        # SOURCE LINE 712
        __M_writer(filters.html_escape(unicode(installation_error.name )))
        __M_writer(u'</td>\n                    <td>')
        # SOURCE LINE 713
        __M_writer(filters.html_escape(unicode(installation_error.type )))
        __M_writer(u'</td>\n                    <td>')
        # SOURCE LINE 714
        __M_writer(filters.html_escape(unicode(installation_error.version )))
        __M_writer(u'</td>\n                </tr>\n                <tr><th>Error</th></tr>\n                <tr><td colspan="3">')
        # SOURCE LINE 717
        __M_writer(filters.html_escape(unicode(installation_error.error_message )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 721

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 724
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_dependency(context,repository_dependency,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 619
        __M_writer(u'\n                \n    ')
        # SOURCE LINE 621

        from galaxy.util import string_as_bool
        encoded_id = trans.security.encode_id( repository_dependency.id )
        if trans.webapp.name == 'galaxy':
            if repository_dependency.tool_shed_repository_id:
                encoded_required_repository_id = trans.security.encode_id( repository_dependency.tool_shed_repository_id )
            else:
                encoded_required_repository_id = None
            if repository_dependency.installation_status:
                installation_status = str( repository_dependency.installation_status )
            else:
                installation_status = None
        repository_name = str( repository_dependency.repository_name )
        repository_owner = str( repository_dependency.repository_owner )
        changeset_revision = str( repository_dependency.changeset_revision )
        prior_installation_required = string_as_bool( str( repository_dependency.prior_installation_required ) ) 
        if prior_installation_required:
            prior_installation_required_str = " <i>(prior install required)</i>"
        else:
            prior_installation_required_str = ""
        
        if trans.webapp.name == 'galaxy':
            if row_is_header:
                cell_type = 'th'
            else:
                cell_type = 'td'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 649
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 651
        if parent is not None:
            # SOURCE LINE 652
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 654
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n')
        # SOURCE LINE 655
        if trans.webapp.name == 'galaxy':
            # SOURCE LINE 656
            __M_writer(u'            <')
            __M_writer(unicode(cell_type))
            __M_writer(u' style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            # SOURCE LINE 657
            if row_is_header:
                # SOURCE LINE 658
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'\n')
                # SOURCE LINE 659
            elif encoded_required_repository_id:
                # SOURCE LINE 660
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=encoded_required_repository_id )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</a>\n')
                # SOURCE LINE 661
            else:
                # SOURCE LINE 662
                __M_writer(u'                   ')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u' \n')
                pass
            # SOURCE LINE 664
            __M_writer(u'            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            # SOURCE LINE 665
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            # SOURCE LINE 666
            __M_writer(filters.html_escape(unicode(changeset_revision )))
            __M_writer(u'\n            </')
            # SOURCE LINE 667
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            # SOURCE LINE 668
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            # SOURCE LINE 669
            __M_writer(filters.html_escape(unicode(repository_owner )))
            __M_writer(u'\n            </')
            # SOURCE LINE 670
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            # SOURCE LINE 671
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            # SOURCE LINE 672
            __M_writer(unicode(installation_status))
            __M_writer(u'\n            </')
            # SOURCE LINE 673
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n')
            # SOURCE LINE 674
        else:
            # SOURCE LINE 675
            __M_writer(u'            <td style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n                Repository <b>')
            # SOURCE LINE 676
            __M_writer(filters.html_escape(unicode(repository_name )))
            __M_writer(u'</b> revision <b>')
            __M_writer(filters.html_escape(unicode(changeset_revision )))
            __M_writer(u'</b> owned by <b>')
            __M_writer(filters.html_escape(unicode(repository_owner )))
            __M_writer(u'</b>')
            __M_writer(unicode(prior_installation_required_str))
            __M_writer(u'\n            </td>\n')
            pass
        # SOURCE LINE 679
        __M_writer(u'    </tr>\n    ')
        # SOURCE LINE 680

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 683
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_test_results_css(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 686
        __M_writer(u'\n    <style type="text/css">\n        table.tool_test_results{ table-layout:fixed;\n                                 width:100%;\n                                 overflow-wrap:normal;\n                                 overflow:hidden;\n                                 border:0px; \n                                 word-break:keep-all;\n                                 word-wrap:break-word;\n                                 line-break:strict; }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_datatype(context,datatype,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 417
        __M_writer(u'\n    ')
        # SOURCE LINE 418

        encoded_id = trans.security.encode_id( datatype.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 424
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 426
        if parent is not None:
            # SOURCE LINE 427
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 429
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 430
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(datatype.extension )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 431
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.type )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 432
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.mimetype )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 433
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.subclass )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 435

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 438
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_failed_test(context,failed_test,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 441
        __M_writer(u'\n    ')
        # SOURCE LINE 442
        encoded_id = trans.security.encode_id( failed_test.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 444
        if parent is not None:
            # SOURCE LINE 445
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 447
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 448
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="failed_test_table" class="tool_test_results">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        # SOURCE LINE 450
        __M_writer(filters.html_escape(unicode(failed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        # SOURCE LINE 451
        __M_writer(filters.html_escape(unicode(failed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Test:</b> ')
        # SOURCE LINE 452
        __M_writer(filters.html_escape(unicode(failed_test.test_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Stderr:</b> <br/>')
        # SOURCE LINE 453
        __M_writer(filters.html_escape(unicode(failed_test.stderr )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Traceback:</b> <br/>')
        # SOURCE LINE 454
        __M_writer(filters.html_escape(unicode(failed_test.traceback )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 458

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 461
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_common_javascripts(context,repository):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            $("#tree").ajaxComplete(function(event, XMLHttpRequest, ajaxOptions) {\n                _log("debug", "ajaxComplete: %o", this); // dom element listening\n            });\n            // --- Initialize sample trees\n            $("#tree").dynatree({\n                title: "')
        # SOURCE LINE 10
        __M_writer(unicode(repository.name))
        __M_writer(u'",\n                rootVisible: true,\n                minExpandLevel: 0, // 1: root node is not collapsible\n                persist: false,\n                checkbox: true,\n                selectMode: 3,\n                onPostInit: function(isReloading, isError) {\n                    //alert("reloading: "+isReloading+", error:"+isError);\n                    logMsg("onPostInit(%o, %o) - %o", isReloading, isError, this);\n                    // Re-fire onActivate, so the text is updated\n                    this.reactivate();\n                }, \n                fx: { height: "toggle", duration: 200 },\n                // initAjax is hard to fake, so we pass the children as object array:\n                initAjax: {url: "')
        # SOURCE LINE 24
        __M_writer(unicode(h.url_for( controller='repository', action='open_folder' )))
        __M_writer(u'",\n                           dataType: "json", \n                           data: { folder_path: "')
        # SOURCE LINE 26
        __M_writer(unicode(repository.repo_path( trans.app )))
        __M_writer(u'" },\n                },\n                onLazyRead: function(dtnode){\n                    dtnode.appendAjax({\n                        url: "')
        # SOURCE LINE 30
        __M_writer(unicode(h.url_for( controller='repository', action='open_folder' )))
        __M_writer(u'", \n                        dataType: "json",\n                        data: { folder_path: dtnode.data.key },\n                    });\n                },\n                onSelect: function(select, dtnode) {\n                    // Display list of selected nodes\n                    var selNodes = dtnode.tree.getSelectedNodes();\n                    // convert to title/key array\n                    var selKeys = $.map(selNodes, function(node) {\n                        return node.data.key;\n                    });\n                    if (document.forms["select_files_to_delete"]) {\n                        // The following is used only ~/templates/webapps/tool_shed/repository/browse_repository.mako.\n                        document.select_files_to_delete.selected_files_to_delete.value = selKeys.join(",");\n                    }\n                    // The following is used only in ~/templates/webapps/tool_shed/repository/upload.mako.\n                    if (document.forms["upload_form"]) {\n                        document.upload_form.upload_point.value = selKeys.slice(-1);\n                    }\n                },\n                onActivate: function(dtnode) {\n                    var cell = $("#file_contents");\n                    var selected_value;\n                     if (dtnode.data.key == \'root\') {\n                        selected_value = "')
        # SOURCE LINE 55
        __M_writer(unicode(repository.repo_path( trans.app )))
        __M_writer(u'/";\n                    } else {\n                        selected_value = dtnode.data.key;\n                    };\n                    if (selected_value.charAt(selected_value.length-1) != \'/\') {\n                        // Make ajax call\n                        $.ajax( {\n                            type: "POST",\n                            url: "')
        # SOURCE LINE 63
        __M_writer(unicode(h.url_for( controller='repository', action='get_file_contents' )))
        __M_writer(u'",\n                            dataType: "json",\n                            data: { file_path: selected_value },\n                            success : function ( data ) {\n                                cell.html( \'<label>\'+data+\'</label>\' )\n                            }\n                        });\n                    } else {\n                        cell.html( \'\' );\n                    };\n                },\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_valid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 944
        __M_writer(u'\n    ')
        # SOURCE LINE 945

        encoded_id = trans.security.encode_id( data_manager.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 951
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 953
        if parent is not None:
            # SOURCE LINE 954
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 956
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 957
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(data_manager.name )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 958
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 959
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.data_tables )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 961

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 964
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_installation_error(context,installation_error,pad,parent,row_counter,row_is_header=False,is_current_repository=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 727
        __M_writer(u'\n    ')
        # SOURCE LINE 728
        encoded_id = trans.security.encode_id( installation_error.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 730
        if parent is not None:
            # SOURCE LINE 731
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 733
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 734
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="rd_install_error_table" class="tool_test_results">\n')
        # SOURCE LINE 736
        if not is_current_repository:
            # SOURCE LINE 737
            __M_writer(u'                    <tr bgcolor="#FFFFCC">\n                        <th>Tool shed</th><th>Name</th><th>Owner</th><th>Changeset revision</th>\n                    </tr>\n                    <tr>\n                        <td>')
            # SOURCE LINE 741
            __M_writer(filters.html_escape(unicode(installation_error.tool_shed )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 742
            __M_writer(filters.html_escape(unicode(installation_error.name )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 743
            __M_writer(filters.html_escape(unicode(installation_error.owner )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 744
            __M_writer(filters.html_escape(unicode(installation_error.changeset_revision )))
            __M_writer(u'</td>\n                    </tr>\n')
            pass
        # SOURCE LINE 747
        __M_writer(u'                <tr><th>Error</th></tr>\n                <tr><td colspan="4">')
        # SOURCE LINE 748
        __M_writer(filters.html_escape(unicode(installation_error.error_message )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 752

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 755
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_repository_dependency(context,invalid_repository_dependency,pad,parent,row_counter):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 486
        __M_writer(u'\n    ')
        # SOURCE LINE 487

        encoded_id = trans.security.encode_id( invalid_repository_dependency.id )
            
        
        # SOURCE LINE 489
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 491
        if parent is not None:
            # SOURCE LINE 492
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 494
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 495
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            ')
        # SOURCE LINE 496
        __M_writer(filters.html_escape(unicode( invalid_repository_dependency.error )))
        __M_writer(u'\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 499

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 502
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_tool(context,invalid_tool,pad,parent,row_counter,valid=True,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 505
        __M_writer(u'\n    ')
        # SOURCE LINE 506
        encoded_id = trans.security.encode_id( invalid_tool.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 508
        if parent is not None:
            # SOURCE LINE 509
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 511
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 512
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        # SOURCE LINE 513
        if trans.webapp.name == 'tool_shed' and invalid_tool.repository_id and invalid_tool.tool_config and invalid_tool.changeset_revision:
            # SOURCE LINE 514
            __M_writer(u'                <a class="view-info" href="')
            __M_writer(unicode(h.url_for( controller='repository', action='load_invalid_tool', repository_id=trans.security.encode_id( invalid_tool.repository_id ), tool_config=invalid_tool.tool_config, changeset_revision=invalid_tool.changeset_revision, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'">\n                    ')
            # SOURCE LINE 515
            __M_writer(filters.html_escape(unicode(invalid_tool.tool_config )))
            __M_writer(u'\n                </a>\n')
            # SOURCE LINE 517
        else:
            # SOURCE LINE 518
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(invalid_tool.tool_config )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 520
        __M_writer(u'        </td>\n    </tr>\n    ')
        # SOURCE LINE 522

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 525
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_workflow(context,workflow,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 967
        __M_writer(u'\n    ')
        # SOURCE LINE 968

        from tool_shed.util.encoding_util import tool_shed_encode
        encoded_id = trans.security.encode_id( workflow.id )
        encoded_workflow_name = tool_shed_encode( workflow.workflow_name )
        if trans.webapp.name == 'tool_shed':
            encoded_repository_metadata_id = trans.security.encode_id( workflow.repository_metadata_id )
            encoded_repository_id = None
        else:
            encoded_repository_metadata_id = None
            encoded_repository_id = trans.security.encode_id( workflow.repository_id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 982
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 984
        if parent is not None:
            # SOURCE LINE 985
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 987
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 988
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        # SOURCE LINE 989
        if row_is_header:
            # SOURCE LINE 990
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'\n')
            # SOURCE LINE 991
        elif trans.webapp.name == 'tool_shed' and encoded_repository_metadata_id:
            # SOURCE LINE 992
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='repository', action='view_workflow', workflow_name=encoded_workflow_name, repository_metadata_id=encoded_repository_metadata_id, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'</a>\n')
            # SOURCE LINE 993
        elif trans.webapp.name == 'galaxy' and encoded_repository_id:
            # SOURCE LINE 994
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='view_workflow', workflow_name=encoded_workflow_name, repository_id=encoded_repository_id )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'</a>\n')
            # SOURCE LINE 995
        else:
            # SOURCE LINE 996
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 998
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 999
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.steps )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 1000
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.format_version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 1001
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.annotation )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 1003

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 1006
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_type_select_field(context,repository_type_select_field,render_help=True):
    context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 166
        __M_writer(u'\n    <div class="form-row">\n        <label>Repository type:</label>\n        ')
        # SOURCE LINE 169

        from tool_shed.repository_types import util
        options = repository_type_select_field.options
        repository_types = []
        for option_tup in options:
            repository_types.append( option_tup[ 1 ] )
        render_as_text = len( options ) == 1
        if render_as_text:
            repository_type = options[ 0 ][ 0 ]
                
        
        # SOURCE LINE 178
        __M_writer(u'\n')
        # SOURCE LINE 179
        if render_as_text:
            # SOURCE LINE 180
            __M_writer(u'            ')
            __M_writer(filters.html_escape(unicode(repository_type )))
            __M_writer(u'\n')
            # SOURCE LINE 181
            if render_help:
                # SOURCE LINE 182
                __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    This repository\'s type cannot be changed because it\'s contents are valid only for it\'s current type or it has been cloned.\n                </div>\n')
                pass
            # SOURCE LINE 186
        else:
            # SOURCE LINE 187
            __M_writer(u'            ')
            __M_writer(unicode(repository_type_select_field.get_html()))
            __M_writer(u'\n')
            # SOURCE LINE 188
            if render_help:
                # SOURCE LINE 189
                __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    Select the repository type based on the following criteria.\n                    <ul>\n')
                # SOURCE LINE 192
                if util.UNRESTRICTED in repository_types:
                    # SOURCE LINE 193
                    __M_writer(u'                            <li><b>Unrestricted</b> - contents can be any set of valid Galaxy utilities or files\n')
                    pass
                # SOURCE LINE 195
                if util.TOOL_DEPENDENCY_DEFINITION in repository_types:
                    # SOURCE LINE 196
                    __M_writer(u'                            <li><b>Tool dependency definition</b> - contents will always be restricted to one file named tool_dependencies.xml\n')
                    pass
                # SOURCE LINE 198
                __M_writer(u'                    </ul>\n                </div>\n')
                pass
            pass
        # SOURCE LINE 202
        __M_writer(u'        <div style="clear: both"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_passed_test(context,passed_test,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 777
        __M_writer(u'\n    ')
        # SOURCE LINE 778
        encoded_id = trans.security.encode_id( passed_test.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 780
        if parent is not None:
            # SOURCE LINE 781
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 783
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 784
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="passed_tests_table" class="tool_test_results">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        # SOURCE LINE 786
        __M_writer(filters.html_escape(unicode(passed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        # SOURCE LINE 787
        __M_writer(filters.html_escape(unicode(passed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Test:</b> ')
        # SOURCE LINE 788
        __M_writer(filters.html_escape(unicode(passed_test.test_id )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 792

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 795
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_items(context,metadata,containers_dict,can_set_metadata=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        def render_folder(folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
            return render_render_folder(context,folder,folder_pad,parent,row_counter,is_root_folder,render_repository_actions_for)
        def render_tool_test_results_css():
            return render_render_tool_test_results_css(context)
        __M_writer = context.writer()
        # SOURCE LINE 1009
        __M_writer(u'\n    ')
        # SOURCE LINE 1010

        from tool_shed.util.encoding_util import tool_shed_encode
        
        has_datatypes = metadata and 'datatypes' in metadata
        has_readme_files = metadata and 'readme_files' in metadata
        has_workflows = metadata and 'workflows' in metadata
        
        datatypes_root_folder = containers_dict.get( 'datatypes', None )
        invalid_data_managers_root_folder = containers_dict.get( 'invalid_data_managers', None )
        invalid_repository_dependencies_root_folder = containers_dict.get( 'invalid_repository_dependencies', None )
        invalid_tool_dependencies_root_folder = containers_dict.get( 'invalid_tool_dependencies', None )
        invalid_tools_root_folder = containers_dict.get( 'invalid_tools', None )
        missing_repository_dependencies_root_folder = containers_dict.get( 'missing_repository_dependencies', None )
        missing_tool_dependencies_root_folder = containers_dict.get( 'missing_tool_dependencies', None )
        readme_files_root_folder = containers_dict.get( 'readme_files', None )
        repository_dependencies_root_folder = containers_dict.get( 'repository_dependencies', None )
        test_environment_root_folder = containers_dict.get( 'test_environment', None )
        tool_dependencies_root_folder = containers_dict.get( 'tool_dependencies', None )
        tool_test_results_root_folder = containers_dict.get( 'tool_test_results', None )
        valid_data_managers_root_folder = containers_dict.get( 'valid_data_managers', None )
        valid_tools_root_folder = containers_dict.get( 'valid_tools', None )
        workflows_root_folder = containers_dict.get( 'workflows', None )
        
        has_contents = datatypes_root_folder or invalid_tools_root_folder or valid_tools_root_folder or workflows_root_folder
        has_dependencies = \
            invalid_repository_dependencies_root_folder or \
            invalid_tool_dependencies_root_folder or \
            missing_repository_dependencies_root_folder or \
            repository_dependencies_root_folder or \
            tool_dependencies_root_folder or \
            missing_tool_dependencies_root_folder
        
        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
            
        
        # SOURCE LINE 1049
        __M_writer(u'\n')
        # SOURCE LINE 1050
        if readme_files_root_folder:
            # SOURCE LINE 1051
            __M_writer(u'        <div class="toolForm">\n            <div class="toolFormTitle">Repository README files - may contain important installation or license information</div>\n            <div class="toolFormBody">\n                <p/>\n                ')
            # SOURCE LINE 1055
            row_counter = RowCounter() 
            
            __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="readme_files">\n                    ')
            # SOURCE LINE 1057
            __M_writer(unicode(render_folder( readme_files_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
            pass
        # SOURCE LINE 1062
        if has_dependencies:
            # SOURCE LINE 1063
            __M_writer(u'        <div class="toolForm">\n            <div class="toolFormTitle">Dependencies of this repository</div>\n            <div class="toolFormBody">\n')
            # SOURCE LINE 1066
            if invalid_repository_dependencies_root_folder:
                # SOURCE LINE 1067
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1068
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_repository_dependencies">\n                        ')
                # SOURCE LINE 1070
                __M_writer(unicode(render_folder( invalid_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1073
            if missing_repository_dependencies_root_folder:
                # SOURCE LINE 1074
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1075
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="missing_repository_dependencies">\n                        ')
                # SOURCE LINE 1077
                __M_writer(unicode(render_folder( missing_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1080
            if repository_dependencies_root_folder:
                # SOURCE LINE 1081
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1082
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="repository_dependencies">\n                        ')
                # SOURCE LINE 1084
                __M_writer(unicode(render_folder( repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1087
            if invalid_tool_dependencies_root_folder:
                # SOURCE LINE 1088
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1089
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tool_dependencies">\n                        ')
                # SOURCE LINE 1091
                __M_writer(unicode(render_folder( invalid_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1094
            if tool_dependencies_root_folder:
                # SOURCE LINE 1095
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1096
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="tool_dependencies">\n                        ')
                # SOURCE LINE 1098
                __M_writer(unicode(render_folder( tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1101
            if missing_tool_dependencies_root_folder:
                # SOURCE LINE 1102
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1103
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="missing_tool_dependencies">\n                        ')
                # SOURCE LINE 1105
                __M_writer(unicode(render_folder( missing_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1108
            __M_writer(u'            </div>\n        </div>\n')
            pass
        # SOURCE LINE 1111
        if has_contents:
            # SOURCE LINE 1112
            __M_writer(u'        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Contents of this repository</div>\n            <div class="toolFormBody">\n')
            # SOURCE LINE 1116
            if valid_tools_root_folder:
                # SOURCE LINE 1117
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1118
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="valid_tools">\n                        ')
                # SOURCE LINE 1120
                __M_writer(unicode(render_folder( valid_tools_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1123
            if invalid_tools_root_folder:
                # SOURCE LINE 1124
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1125
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tools">\n                        ')
                # SOURCE LINE 1127
                __M_writer(unicode(render_folder( invalid_tools_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1130
            if valid_data_managers_root_folder:
                # SOURCE LINE 1131
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1132
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="valid_tools">\n                        ')
                # SOURCE LINE 1134
                __M_writer(unicode(render_folder( valid_data_managers_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1137
            if invalid_data_managers_root_folder:
                # SOURCE LINE 1138
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1139
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tools">\n                        ')
                # SOURCE LINE 1141
                __M_writer(unicode(render_folder( invalid_data_managers_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1144
            if workflows_root_folder:
                # SOURCE LINE 1145
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1146
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="workflows">\n                        ')
                # SOURCE LINE 1148
                __M_writer(unicode(render_folder( workflows_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1151
            if datatypes_root_folder:
                # SOURCE LINE 1152
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1153
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="datatypes">\n                        ')
                # SOURCE LINE 1155
                __M_writer(unicode(render_folder( datatypes_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1158
            __M_writer(u'            </div>\n        </div>\n')
            pass
        # SOURCE LINE 1161
        if tool_test_results_root_folder:
            # SOURCE LINE 1162
            __M_writer(u'        ')
            __M_writer(unicode(render_tool_test_results_css()))
            __M_writer(u'\n        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Automated tool test results</div>\n            <div class="toolFormBody">\n                    <p/>\n                    ')
            # SOURCE LINE 1168
            row_counter = RowCounter() 
            
            __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="test_environment">\n                        ')
            # SOURCE LINE 1170
            __M_writer(unicode(render_folder( tool_test_results_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
            __M_writer(u'\n                    </table>\n            </div>\n        </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header=False):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 464
        __M_writer(u'\n    ')
        # SOURCE LINE 465

        encoded_id = trans.security.encode_id( data_manager.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 471
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 473
        if parent is not None:
            # SOURCE LINE 474
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 476
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 477
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(data_manager.index )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 478
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.error )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 480

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 483
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_sharable_str(context,repository,changeset_revision=None):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 206
        __M_writer(u'\n    ')
        # SOURCE LINE 207

        from tool_shed.util.shed_util_common import generate_sharable_link_for_repository_in_tool_shed
        sharable_link = generate_sharable_link_for_repository_in_tool_shed( trans, repository, changeset_revision=changeset_revision )
            
        
        # SOURCE LINE 210
        __M_writer(u'\n    ')
        # SOURCE LINE 211
        __M_writer(unicode(sharable_link))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_tool_dependency(context,invalid_tool_dependency,pad,parent,row_counter):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 528
        __M_writer(u'\n    ')
        # SOURCE LINE 529

        encoded_id = trans.security.encode_id( invalid_tool_dependency.id )
            
        
        # SOURCE LINE 531
        __M_writer(u'\n    <style type="text/css">\n        #invalid_td_table{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px; \n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n    </style>\n    <tr class="datasetRow"\n')
        # SOURCE LINE 543
        if parent is not None:
            # SOURCE LINE 544
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 546
        __M_writer(u'        id="libraryItem-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 547
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="invalid_td_table">\n                <tr><td>')
        # SOURCE LINE 549
        __M_writer(filters.html_escape(unicode( invalid_tool_dependency.error )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 553

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 556
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


