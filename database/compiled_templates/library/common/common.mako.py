# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383202403.951431
_template_filename=u'templates/webapps/galaxy/library/common/common.mako'
_template_uri=u'/library/common/common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['common_javascripts', 'render_upload_form', 'render_compression_types_help', 'render_actions_on_multiple_items']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7eba090', context._clean_inheritance_tokens(), templateuri=u'/common/template_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7eba090')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7eba090')._populate(_import_ns, [u'render_template_field'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 74
        __M_writer(u'\n\n')
        # SOURCE LINE 403
        __M_writer(u'\n\n')
        # SOURCE LINE 468
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_common_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7eba090')._populate(_import_ns, [u'render_template_field'])
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <script type="text/javascript">\n        function checkAllFields()\n        {\n            var chkAll = document.getElementById(\'checkAll\');\n            var checks = document.getElementsByTagName(\'input\');\n            var boxLength = checks.length;\n            var allChecked = false;\n            var totalChecked = 0;\n            if ( chkAll.checked == true )\n            {\n                for ( i=0; i < boxLength; i++ )\n                {\n                    if ( checks[i].name.indexOf( \'ldda_ids\' ) != -1)\n                    {\n                       checks[i].checked = true;\n                    }\n                }\n            }\n            else\n            {\n                for ( i=0; i < boxLength; i++ )\n                {\n                    if ( checks[i].name.indexOf( \'ldda_ids\' ) != -1)\n                    {\n                       checks[i].checked = false\n                    }\n                }\n            }\n        }\n\n        function checkForm() {\n            if ( $("select#action_on_datasets_select option:selected").text() == "delete" ) {\n                if ( confirm( "Click OK to delete these datasets?" ) ) {\n                    return true;\n                } else {\n                    return false;\n                }\n            }\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_upload_form(context,cntrller,upload_option,action,library_id,folder_id,replace_dataset,file_formats,dbkeys,space_to_tab,link_data_only,widgets,roles_select_list,history,show_deleted):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7eba090')._populate(_import_ns, [u'render_template_field'])
        upload_option_select_list = _import_ns.get('upload_option_select_list', context.get('upload_option_select_list', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        ldda_message = _import_ns.get('ldda_message', context.get('ldda_message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        template_id = _import_ns.get('template_id', context.get('template_id', UNDEFINED))
        last_used_build = _import_ns.get('last_used_build', context.get('last_used_build', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 76
        __M_writer(u'\n    ')
        # SOURCE LINE 77

        import os, os.path
        from galaxy.web.form_builder import AddressField, CheckboxField, SelectField, TextArea, TextField, WorkflowField, WorkflowMappingField, HistoryField
            
        
        # SOURCE LINE 80
        __M_writer(u'\n')
        # SOURCE LINE 81
        if upload_option in [ 'upload_file', 'upload_directory', 'upload_paths' ]:
            # SOURCE LINE 82
            __M_writer(u'        <div class="toolForm" id="upload_library_dataset_tool_form">\n            ')
            # SOURCE LINE 83

            if upload_option == 'upload_directory':
                tool_form_title = 'Upload a directory of files'
            elif upload_option == 'upload_paths':
                tool_form_title = 'Upload files from filesystem paths'
            else:
                tool_form_title = 'Upload files'
                        
            
            # SOURCE LINE 90
            __M_writer(u'\n            <div class="toolFormTitle">')
            # SOURCE LINE 91
            __M_writer(unicode(tool_form_title))
            __M_writer(u'</div>\n            <div class="toolFormBody">\n                <form name="upload_library_dataset" id="upload_library_dataset" action="')
            # SOURCE LINE 93
            __M_writer(unicode(action))
            __M_writer(u'" enctype="multipart/form-data" method="post">\n                    <input type="hidden" name="tool_id" value="upload1"/>\n                    <input type="hidden" name="tool_state" value="None"/>\n                    <input type="hidden" name="cntrller" value="')
            # SOURCE LINE 96
            __M_writer(unicode(cntrller))
            __M_writer(u'"/>\n                    <input type="hidden" name="library_id" value="')
            # SOURCE LINE 97
            __M_writer(unicode(library_id))
            __M_writer(u'"/>\n                    <input type="hidden" name="folder_id" value="')
            # SOURCE LINE 98
            __M_writer(unicode(folder_id))
            __M_writer(u'"/>\n                    <input type="hidden" name="show_deleted" value="')
            # SOURCE LINE 99
            __M_writer(unicode(show_deleted))
            __M_writer(u'"/>\n')
            # SOURCE LINE 100
            if replace_dataset not in [ None, 'None' ]:
                # SOURCE LINE 101
                __M_writer(u'                        <input type="hidden" name="replace_id" value="')
                __M_writer(unicode(trans.security.encode_id( replace_dataset.id )))
                __M_writer(u'"/>\n                        <div class="form-row">\n                            You are currently selecting a new file to replace \'<a href="')
                # SOURCE LINE 103
                __M_writer(unicode(h.url_for( controller='library_common', action='ldda_info', cntrller=cntrller, library_id=library_id, folder_id=folder_id, id=trans.security.encode_id( replace_dataset.library_dataset_dataset_association.id ) )))
                __M_writer(u'">')
                __M_writer(unicode(util.unicodify( replace_dataset.name )))
                __M_writer(u'</a>\'.\n                            <div style="clear: both"></div>\n                        </div>\n')
                pass
            # SOURCE LINE 107
            __M_writer(u'                    <div class="form-row">\n                        <label>Upload option:</label>\n                        <div class="form-row-input">\n                            ')
            # SOURCE LINE 110
            __M_writer(unicode(upload_option_select_list.get_html()))
            __M_writer(u'\n                        </div>\n                        <div class="toolParamHelp" style="clear: both;">\n                            Choose upload option (file, directory, filesystem paths, current history).\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n                    <div class="form-row">\n                        <label>File Format:</label>\n                        <div class="form-row-input">\n                            <select name="file_type">\n                                <option value="auto" selected>Auto-detect</option>\n')
            # SOURCE LINE 122
            for file_format in file_formats:
                # SOURCE LINE 123
                __M_writer(u'                                    <option value="')
                __M_writer(unicode(file_format))
                __M_writer(u'">')
                __M_writer(unicode(file_format))
                __M_writer(u'</option>\n')
                pass
            # SOURCE LINE 125
            __M_writer(u'                            </select>\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n')
            # SOURCE LINE 129
            if upload_option == 'upload_file':
                # SOURCE LINE 130
                __M_writer(u'                        <div class="form-row">\n                            <input type="hidden" name="async_datasets" value="None"/>\n                            <div style="clear: both"></div>\n                        </div>\n                        <div class="form-row">\n                            <label>File:</label>\n                            <div class="form-row-input">\n                                <input type="file" name="files_0|file_data" galaxy-ajax-upload="true"/>\n                            </div>\n                            <div style="clear: both"></div>\n                        </div>\n                        <div class="form-row">\n                            <label>URL/Text:</label>\n                            <div class="form-row-input">\n                                <textarea name="files_0|url_paste" rows="5" cols="35"></textarea>\n                            </div>\n                            <div class="toolParamHelp" style="clear: both;">\n                                Specify a list of URLs (one per line) or paste the contents of a file.\n                            </div>\n                            <div style="clear: both"></div>\n                        </div>\n')
                # SOURCE LINE 151
            elif upload_option == 'upload_directory':
                # SOURCE LINE 152
                __M_writer(u'                        ')

                if ( trans.user_is_admin() and cntrller == 'library_admin' ):
                    import_dir = trans.app.config.library_import_dir
                else:
                    # Directories of files from the Data Libraries view are restricted to a
                    # sub-directory named the same as the current user's email address
                    # contained within the configured setting for user_library_import_dir
                    import_dir = os.path.join( trans.app.config.user_library_import_dir, trans.user.email )
                                        
                
                # SOURCE LINE 160
                __M_writer(u'\n                        <div class="form-row">\n                            ')
                # SOURCE LINE 162

                                # See if we have any contained sub-directories, if not the only option
                                # in the server_dir select list will be library_import_dir
                contains_directories = False
                for entry in os.listdir( import_dir ):
                    if os.path.isdir( os.path.join( import_dir, entry ) ):
                        contains_directories = True
                        break
                                            
                
                # SOURCE LINE 170
                __M_writer(u'\n                            <label>Server Directory</label>\n                            <div class="form-row-input">\n                                <select name="server_dir">\n')
                # SOURCE LINE 174
                if contains_directories:
                    # SOURCE LINE 175
                    __M_writer(u'                                        <option>None</option>\n')
                    # SOURCE LINE 176
                    for entry in os.listdir( import_dir ):
                        # SOURCE LINE 178
                        if os.path.isdir( os.path.join( import_dir, entry ) ):
                            # SOURCE LINE 179
                            __M_writer(u'                                                <option>')
                            __M_writer(unicode(entry))
                            __M_writer(u'</option>\n')
                            pass
                        pass
                    # SOURCE LINE 182
                else:
                    # SOURCE LINE 183
                    if ( trans.user_is_admin() and cntrller == 'library_admin' ):
                        # SOURCE LINE 184
                        __M_writer(u'                                            <option>')
                        __M_writer(unicode(import_dir))
                        __M_writer(u'</option>\n')
                        # SOURCE LINE 185
                    else:
                        # SOURCE LINE 186
                        __M_writer(u'                                            <option>')
                        __M_writer(unicode(trans.user.email))
                        __M_writer(u'</option>\n')
                        pass
                    pass
                # SOURCE LINE 189
                __M_writer(u'                                </select>\n                            </div>\n                            <div class="toolParamHelp" style="clear: both;">\n')
                # SOURCE LINE 192
                if contains_directories:
                    # SOURCE LINE 193
                    __M_writer(u'                                    Upload all files in a sub-directory of <strong>')
                    __M_writer(unicode(import_dir))
                    __M_writer(u'</strong> on the Galaxy server.\n')
                    # SOURCE LINE 194
                else:
                    # SOURCE LINE 195
                    __M_writer(u'                                    Upload all files in <strong>')
                    __M_writer(unicode(import_dir))
                    __M_writer(u'</strong> on the Galaxy server.\n')
                    pass
                # SOURCE LINE 197
                __M_writer(u'                            </div>\n                            <div style="clear: both"></div>\n                        </div>\n')
                # SOURCE LINE 200
            elif upload_option == 'upload_paths':
                # SOURCE LINE 201
                __M_writer(u'                        <div class="form-row">\n                            <label>Paths to upload</label>\n                            <div class="form-row-input">\n                                <textarea name="filesystem_paths" rows="10" cols="35"></textarea>\n                            </div>\n                            <div class="toolParamHelp" style="clear: both;">\n                                Upload all files pasted in the box.  The (recursive) contents of any pasted directories will be added as well.\n                            </div>\n                        </div>\n                        <div class="form-row">\n                            <label>Preserve directory structure?</label>\n                            <div class="form-row-input">\n                                <input type="checkbox" name="preserve_dirs" value="Yes" checked="true" />Yes\n                            </div>\n                            <div class="toolParamHelp" style="clear: both;">\n                                If checked (default), library sub-folders will be used to preserve any subdirectories on the filesystem.\n                                If unchecked, any files in subdirectories on the filesystem will be placed directly in the library folder.\n                            </div>\n                        </div>\n')
                pass
            # SOURCE LINE 221
            if upload_option in ( 'upload_directory', 'upload_paths' ):
                # SOURCE LINE 222
                __M_writer(u'                        <div class="form-row">\n                            <label>Copy data into Galaxy?</label>\n                            <div class="form-row-input">\n                                <select name="link_data_only">\n')
                # SOURCE LINE 226
                if not link_data_only or link_data_only == 'copy_files':
                    # SOURCE LINE 227
                    __M_writer(u'                                        <option value="copy_files" selected>Copy files into Galaxy\n                                        <option value="link_to_files">Link to files without copying into Galaxy\n')
                    # SOURCE LINE 229
                else:
                    # SOURCE LINE 230
                    __M_writer(u'                                        <option value="copy_files">Copy files into Galaxy\n                                        <option value="link_to_files" selected>Link to files without copying into Galaxy\n')
                    pass
                # SOURCE LINE 233
                __M_writer(u'                                </select>\n                            </div>\n                            <div class="toolParamHelp" style="clear: both;">\n                                Normally data uploaded with this tool is copied into Galaxy\'s configured "file_path" location where Galaxy\n                                has a form of control over the data files.  However, this may not be desired (especially for large NGS \n                                datasets), so using the option labeled "Link to files without copying into Galaxy" will force Galaxy to \n                                always read the data from its original path.\n')
                # SOURCE LINE 240
                if upload_option == 'upload_directory':
                    # SOURCE LINE 241
                    __M_writer(u'                                    Any symlinks encountered in the uploaded directory will be dereferenced once.  That is, Galaxy will \n                                    point directly to the file that is linked, but no other symlinks further down the line will be dereferenced.\n')
                    pass
                # SOURCE LINE 244
                __M_writer(u'                            </div>\n                        </div>\n')
                pass
            # SOURCE LINE 247
            __M_writer(u'                    <div class="form-row">\n                        <label>\n                            Convert spaces to tabs:\n                        </label>\n                        <div class="form-row-input">\n                            ')
            # SOURCE LINE 252

            if space_to_tab == 'true':
                checked = ' checked'
            else:
                checked = ''
            if upload_option == 'upload_file':
                name = 'files_0|space_to_tab'
            else:
                name = 'space_to_tab'
            space2tab = '<input type="checkbox" name="%s" value="true"%s/>Yes' % ( name, checked )
                                        
            
            # SOURCE LINE 262
            __M_writer(u'\n                            ')
            # SOURCE LINE 263
            __M_writer(unicode(space2tab))
            __M_writer(u'\n                        </div>\n                        <div class="toolParamHelp" style="clear: both;">\n                            Use this option if you are entering intervals by hand.\n                        </div>\n                    </div>\n                    <div style="clear: both"></div>\n                    <div class="form-row">\n                        <label>Genome:</label>\n                        <div class="form-row-input">\n                            <select name="dbkey" last_selected_value="?">\n                                ')
            # SOURCE LINE 274

                                    # move unspecified to the first option and set as default if not last_used_build
                                    #TODO: remove when we decide on a common dbkey selector widget
            unspecified = ('unspecified (?)', '?')
            if unspecified in dbkeys:
                dbkeys.remove( unspecified )
                dbkeys.insert( 0, unspecified )
            default_selected = last_used_build or '?'
                                            
            
            # SOURCE LINE 282
            __M_writer(u'\n')
            # SOURCE LINE 283
            for dbkey in dbkeys:
                # SOURCE LINE 284
                if dbkey[1] == default_selected:
                    # SOURCE LINE 285
                    __M_writer(u'                                        <option value="')
                    __M_writer(unicode(dbkey[1]))
                    __M_writer(u'" selected>')
                    __M_writer(unicode(dbkey[0]))
                    __M_writer(u'</option>\n')
                    # SOURCE LINE 286
                else:
                    # SOURCE LINE 287
                    __M_writer(u'                                        <option value="')
                    __M_writer(unicode(dbkey[1]))
                    __M_writer(u'">')
                    __M_writer(unicode(dbkey[0]))
                    __M_writer(u'</option>\n')
                    pass
                pass
            # SOURCE LINE 290
            __M_writer(u'                            </select>\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n                    <div class="form-row">\n                        <label>Message:</label>\n                        <div class="form-row-input">\n')
            # SOURCE LINE 297
            if ldda_message:
                # SOURCE LINE 298
                __M_writer(u'                                <textarea name="ldda_message" rows="3" cols="35">')
                __M_writer(unicode(ldda_message))
                __M_writer(u'</textarea>\n')
                # SOURCE LINE 299
            else:
                # SOURCE LINE 300
                __M_writer(u'                                <textarea name="ldda_message" rows="3" cols="35"></textarea>\n')
                pass
            # SOURCE LINE 302
            __M_writer(u'                        </div>\n                        <div class="toolParamHelp" style="clear: both;">\n                            This information will be displayed in the "Message" column for this dataset in the data library browser\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n')
            # SOURCE LINE 308
            if roles_select_list:
                # SOURCE LINE 309
                __M_writer(u'                        <div class="form-row">\n                            <label>Restrict dataset access to specific roles:</label>\n                            <div class="form-row-input">\n                                ')
                # SOURCE LINE 312
                __M_writer(unicode(roles_select_list.get_html()))
                __M_writer(u'\n                            </div>\n                            <div class="toolParamHelp" style="clear: both;">\n                                Multi-select list - hold the appropriate key while clicking to select multiple roles.  More restrictions can be applied after the upload is complete.  Selecting no roles makes a dataset public.\n                            </div>\n                        </div>\n                        <div style="clear: both"></div>\n')
                pass
            # SOURCE LINE 320
            if widgets:
                # SOURCE LINE 321
                for i, field in enumerate( widgets ):
                    # SOURCE LINE 322
                    __M_writer(u'                            <div class="form-row">\n                                <label>')
                    # SOURCE LINE 323
                    __M_writer(unicode(field[ 'label' ]))
                    __M_writer(u'</label>\n                                <div class="form-row-input">\n                                    ')
                    # SOURCE LINE 325
                    __M_writer(unicode(field[ 'widget' ].get_html()))
                    __M_writer(u'\n                                </div>\n                                <div class="toolParamHelp" style="clear: both;">\n')
                    # SOURCE LINE 328
                    if field[ 'helptext' ]:
                        # SOURCE LINE 329
                        __M_writer(u'                                        ')
                        __M_writer(unicode(field[ 'helptext' ]))
                        __M_writer(u'<br/>\n')
                        pass
                    # SOURCE LINE 331
                    __M_writer(u'                                    *Inherited template field\n                                </div>\n                                <div style="clear: both"></div>\n                            </div>\n')
                    pass
                pass
            # SOURCE LINE 337
            __M_writer(u'                    <div class="form-row">\n                        <input type="submit" class="primary-button" name="runtool_btn" value="Upload to library"/>\n                    </div>\n                </form>\n            </div>\n        </div>\n')
            # SOURCE LINE 343
        elif upload_option == 'import_from_history':
            # SOURCE LINE 344
            __M_writer(u'        <div class="toolForm">\n            <div class="toolFormTitle">Active datasets in your current history (')
            # SOURCE LINE 345
            __M_writer(unicode( util.unicodify( history.name )))
            __M_writer(u')</div>\n            <div class="toolFormBody">\n')
            # SOURCE LINE 347
            if history and history.active_datasets:
                # SOURCE LINE 348
                __M_writer(u'                    <form name="add_history_datasets_to_library" action="')
                __M_writer(unicode(h.url_for( controller='library_common', action='add_history_datasets_to_library', cntrller=cntrller, library_id=library_id )))
                __M_writer(u'" enctype="multipart/form-data" method="post">\n                        <input type="hidden" name="folder_id" value="')
                # SOURCE LINE 349
                __M_writer(unicode(folder_id))
                __M_writer(u'"/>\n                        <input type="hidden" name="show_deleted" value="')
                # SOURCE LINE 350
                __M_writer(unicode(show_deleted))
                __M_writer(u'"/>\n                        <input type="hidden" name="upload_option" value="import_from_history"/>\n                        <input type="hidden" name="ldda_message" value="')
                # SOURCE LINE 352
                __M_writer(unicode(ldda_message))
                __M_writer(u'"/>\n                        ')
                # SOURCE LINE 353

                role_ids_selected = ''
                if roles_select_list:
                    selected = roles_select_list.get_selected( return_value=True, multi=True )
                    if selected:
                        role_ids_selected = ','.join( selected )
                                        
                
                # SOURCE LINE 359
                __M_writer(u'\n                        <input type="hidden" name="roles" value="')
                # SOURCE LINE 360
                __M_writer(unicode(role_ids_selected))
                __M_writer(u'"/>\n')
                # SOURCE LINE 361
                if replace_dataset not in [ None, 'None' ]:
                    # SOURCE LINE 362
                    __M_writer(u'                            <input type="hidden" name="replace_id" value="')
                    __M_writer(unicode(trans.security.encode_id( replace_dataset.id )))
                    __M_writer(u'"/>\n                            <div class="form-row">\n                                You are currently selecting a new file to replace \'<a href="')
                    # SOURCE LINE 364
                    __M_writer(unicode(h.url_for( controller='library_common', action='ldda_info', cntrller=cntrller, library_id=library_id, folder_id=folder_id, id=trans.security.encode_id( replace_dataset.library_dataset_dataset_association.id ) )))
                    __M_writer(u'">')
                    __M_writer(unicode( util.unicodify( replace_dataset.name )))
                    __M_writer(u'</a>\'.\n                                <div style="clear: both"></div>\n                            </div>\n')
                    pass
                # SOURCE LINE 368
                for hda in history.visible_datasets:
                    # SOURCE LINE 369
                    __M_writer(u'                            ')
                    encoded_id = trans.security.encode_id( hda.id ) 
                    
                    __M_writer(u'\n                            <div class="form-row">\n                                <input name="hda_ids" id="hist_')
                    # SOURCE LINE 371
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'" value="')
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'" type="checkbox"/>\n                                <label for="hist_')
                    # SOURCE LINE 372
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'" style="display: inline;font-weight:normal;">')
                    __M_writer(unicode(hda.hid))
                    __M_writer(u': ')
                    __M_writer(unicode( util.unicodify( hda.name )))
                    __M_writer(u'</label>\n                            </div>\n')
                    pass
                # SOURCE LINE 375
                if widgets:
                    # SOURCE LINE 376
                    __M_writer(u'                            <input type="hidden" name="template_id" value="')
                    __M_writer(unicode(template_id))
                    __M_writer(u'"/>\n')
                    # SOURCE LINE 377
                    for i, field in enumerate( widgets ):
                        # SOURCE LINE 378
                        __M_writer(u'                                <div class="form-row">\n                                    <label>')
                        # SOURCE LINE 379
                        __M_writer(unicode(field[ 'label' ]))
                        __M_writer(u'</label>\n                                    <div class="form-row-input">\n                                        ')
                        # SOURCE LINE 381
                        __M_writer(unicode(field[ 'widget' ].get_html()))
                        __M_writer(u'\n                                    </div>\n                                    <div class="toolParamHelp" style="clear: both;">\n')
                        # SOURCE LINE 384
                        if field[ 'helptext' ]:
                            # SOURCE LINE 385
                            __M_writer(u'                                            ')
                            __M_writer(unicode(field[ 'helptext' ]))
                            __M_writer(u'<br/>\n')
                            pass
                        # SOURCE LINE 387
                        __M_writer(u'                                        *Inherited template field\n                                    </div>\n                                    <div style="clear: both"></div>\n                                </div>\n')
                        pass
                    pass
                # SOURCE LINE 393
                __M_writer(u'                        <div class="form-row">\n                            <input type="submit" name="add_history_datasets_to_library_button" value="Import to library"/>\n                        </div>\n                    </form>\n')
                # SOURCE LINE 397
            else:
                # SOURCE LINE 398
                __M_writer(u'                    <p>Your current history is empty</p>\n')
                pass
            # SOURCE LINE 400
            __M_writer(u'            </div>\n        </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_compression_types_help(context,comptypes):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7eba090')._populate(_import_ns, [u'render_template_field'])
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n    <div class="libraryItemBody">\n        <p class="infomark">\n            TIP: You can download individual library datasets by selecting "Download this dataset" from the context menu (triangle) next to each dataset\'s name.\n        </p>\n    </div>\n')
        # SOURCE LINE 52
        if len( comptypes ) > 1:
            # SOURCE LINE 53
            __M_writer(u'        <div class="libraryItemBody">\n            <p class="infomark">\n                TIP: Several compression options are available for downloading multiple library datasets simultaneously:\n            </p>\n            <ul style="padding-left: 1em; list-style-type: disc;">\n')
            # SOURCE LINE 58
            if 'gz' in comptypes:
                # SOURCE LINE 59
                __M_writer(u'                    <li>gzip: Recommended for fast network connections\n')
                # SOURCE LINE 60
                if trans.app.config.upstream_gzip:
                    # SOURCE LINE 61
                    __M_writer(u'                            NOTE: The file you receive will be an uncompressed .tar file - this is because the Galaxy server compresses it and your browser decompresses it on the fly.\n')
                    pass
                # SOURCE LINE 63
                __M_writer(u'                    </li>\n')
                pass
            # SOURCE LINE 65
            if 'bz2' in comptypes:
                # SOURCE LINE 66
                __M_writer(u'                    <li>bzip2: Recommended for slower network connections (smaller size but takes longer to compress)</li>\n')
                pass
            # SOURCE LINE 68
            if 'zip' in comptypes:
                # SOURCE LINE 69
                __M_writer(u'                    <li>zip: Not recommended but is provided as an option for those who cannot open the above formats</li>\n')
                pass
            # SOURCE LINE 71
            __M_writer(u'            </ul>\n        </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_actions_on_multiple_items(context,actions_to_exclude=[]):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7eba090')._populate(_import_ns, [u'render_template_field'])
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        default_action = _import_ns.get('default_action', context.get('default_action', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        comptypes = _import_ns.get('comptypes', context.get('comptypes', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 405
        __M_writer(u'\n    ')
        # SOURCE LINE 406

        is_admin = trans.user_is_admin() and cntrller=='library_admin'
        can_delete = 'delete' not in actions_to_exclude
        can_download = 'download' not in actions_to_exclude
        can_import_to_histories = 'import_to_histories' not in actions_to_exclude
        can_manage_permissions = 'manage_permissions' not in actions_to_exclude
        can_move = 'move' not in actions_to_exclude
            
        
        # SOURCE LINE 413
        __M_writer(u'\n    <tfoot>\n        <tr>\n            <td colspan="5" style="padding-left: 42px;">\n                For selected datasets:\n                <select name="do_action" id="action_on_selected_items">\n')
        # SOURCE LINE 419
        if can_import_to_histories:
            # SOURCE LINE 420
            if default_action == 'import_to_current_history':
                # SOURCE LINE 421
                __M_writer(u'                            <option value="import_to_current_history" selected>Import to current history</option>\n')
                # SOURCE LINE 422
            else:
                # SOURCE LINE 423
                __M_writer(u'                            <option value="import_to_current_history">Import to current history</option>\n')
                pass
            # SOURCE LINE 425
            __M_writer(u'                        <option value="import_to_histories">Import to histories</option>\n')
            pass
        # SOURCE LINE 427
        if can_manage_permissions:
            # SOURCE LINE 428
            if not is_admin and default_action == 'manage_permissions':
                # SOURCE LINE 429
                __M_writer(u'                            <option value="manage_permissions" selected>Edit permissions</option>\n')
                # SOURCE LINE 430
            else:
                # SOURCE LINE 431
                __M_writer(u'                            <option value="manage_permissions">Edit permissions</option>\n')
                pass
            pass
        # SOURCE LINE 434
        if can_move:
            # SOURCE LINE 435
            __M_writer(u'                        <option value="move">Move</option>\n')
            pass
        # SOURCE LINE 437
        if can_delete:
            # SOURCE LINE 438
            __M_writer(u'                        <option value="delete">Delete</option>\n')
            pass
        # SOURCE LINE 440
        if can_download:
            # SOURCE LINE 441
            if 'gz' in comptypes:
                # SOURCE LINE 442
                __M_writer(u'                            <option value="tgz"\n')
                # SOURCE LINE 443
                if default_action == 'download':
                    # SOURCE LINE 444
                    __M_writer(u'                                selected\n')
                    pass
                # SOURCE LINE 446
                __M_writer(u'                            >Download as a .tar.gz file</option>\n')
                pass
            # SOURCE LINE 448
            if 'bz2' in comptypes:
                # SOURCE LINE 449
                __M_writer(u'                            <option value="tbz">Download as a .tar.bz2 file</option>\n')
                pass
            # SOURCE LINE 451
            if 'zip' in comptypes:
                # SOURCE LINE 452
                __M_writer(u'                            <option value="zip">Download as a .zip file</option>\n')
                pass
            # SOURCE LINE 454
            if 'ngxzip' in comptypes:
                # SOURCE LINE 456
                __M_writer(u'                            <option value="ngxzip"\n')
                # SOURCE LINE 457
                if default_action == 'download':
                    # SOURCE LINE 458
                    __M_writer(u'                                selected\n')
                    pass
                # SOURCE LINE 460
                __M_writer(u'                            >Download as a .zip file</option>\n')
                pass
            pass
        # SOURCE LINE 463
        __M_writer(u'                </select>\n                <input type="submit" class="primary-button" name="action_on_datasets_button" id="action_on_datasets_button" value="Go"/>\n            </td>\n        </tr>\n    </tfoot>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


