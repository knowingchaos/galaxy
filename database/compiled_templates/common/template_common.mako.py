# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383202404.032913
_template_filename=u'templates/common/template_common.mako'
_template_uri=u'/common/template_common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_template_field', 'render_template_fields']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 94
        __M_writer(u'\n            \n')
        # SOURCE LINE 200
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_template_field(context,field,render_as_hidden=False):
    context.caller_stack._push_frame()
    try:
        util = context.get('util', UNDEFINED)
        int = context.get('int', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        str = context.get('str', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    ')
        # SOURCE LINE 2

        from galaxy.web.form_builder import AddressField, CheckboxField, SelectField, TextArea, TextField, WorkflowField, WorkflowMappingField, HistoryField
        
        widget = field[ 'widget' ]
        has_contents = False
        label = field[ 'label' ]
        value = ''
        if isinstance( widget, TextArea ) and widget.value:
            has_contents = True
            if render_as_hidden:
                value = widget.value
            else:
                value = '<pre>%s</pre>' % widget.value
        elif isinstance( widget, TextField ) and widget.value:
            has_contents = True
            value = widget.value
        elif isinstance( widget, SelectField ) and widget.options:
            for option_label, option_value, selected in widget.options:
                if selected:
                    has_contents = True
                    value = option_value
        elif isinstance( widget, CheckboxField ) and widget.checked:
            has_contents = True
            if render_as_hidden:
                value = 'true'
            else:
                value = 'checked'
        elif isinstance( widget, WorkflowField ) and str( widget.value ).lower() not in [ 'none' ]:
            has_contents = True
            if render_as_hidden:
                value = widget.value
            else:
                workflow_user = widget.user
                if workflow_user:
                    for workflow in workflow_user.stored_workflows:
                        if not workflow.deleted and str( widget.value ) == str( workflow.id ):
                            value = workflow.name
                            break
                else:
                    # If we didn't find the selected workflow option above, we'll just print the value
                    value = widget.value
        elif isinstance( widget, WorkflowMappingField ) and str( widget.value ).lower() not in [ 'none' ]:
            has_contents = True
            if render_as_hidden:
                value = widget.value
            else:
                workflow_user = widget.user
                if workflow_user:
                    for workflow in workflow_user.stored_workflows:
                        if not workflow.deleted and str( widget.value ) == str( workflow.id ):
                            value = workflow.name
                            break
                else:
                    # If we didn't find the selected workflow option above, we'll just print the value
                    value = widget.value
        elif isinstance( widget, HistoryField ) and str( widget.value ).lower() not in [ 'none' ]:
            has_contents = True
            if render_as_hidden:
                value = widget.value
            else:
                history_user = widget.user
                if history_user:
                    for history in history_user.histories:
                        if not history.deleted and str( widget.value ) == str( history.id ):
                            value = util.unicodify( history.name )
                            break
                else:
                    # If we didn't find the selected workflow option above, we'll just print the value
                    value = widget.value
        elif isinstance( widget, AddressField ) and str( widget.value ).lower() not in [ 'none' ]:
            has_contents = True
            if render_as_hidden:
                value = widget.value
            else:
                address = trans.sa_session.query( trans.model.UserAddress ).get( int( widget.value ) )
                label = address.desc
                value = address.get_html()
            
        
        # SOURCE LINE 79
        __M_writer(u'\n')
        # SOURCE LINE 80
        if has_contents:
            # SOURCE LINE 81
            if render_as_hidden:
                # SOURCE LINE 82
                __M_writer(u'            <input type="hidden" name="')
                __M_writer(unicode(widget.name))
                __M_writer(u'" value="')
                __M_writer(unicode(value))
                __M_writer(u'"/>\n')
                # SOURCE LINE 83
            else:
                # SOURCE LINE 84
                __M_writer(u'            <div class="form-row">\n                <label>')
                # SOURCE LINE 85
                __M_writer(unicode(label))
                __M_writer(u'</label>\n                ')
                # SOURCE LINE 86
                __M_writer(unicode(value))
                __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n                    ')
                # SOURCE LINE 88
                __M_writer(unicode(field[ 'helptext' ]))
                __M_writer(u'\n                </div>\n                <div style="clear: both"></div>\n            </div>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_template_fields(context,cntrller,item_type,widgets,widget_fields_have_contents,request_type_id=None,sample_id=None,library_id=None,folder_id=None,ldda_id=None,info_association=None,inherited=False,editable=True):
    context.caller_stack._push_frame()
    try:
        show_deleted = context.get('show_deleted', UNDEFINED)
        h = context.get('h', UNDEFINED)
        def render_template_field(field,render_as_hidden=False):
            return render_render_template_field(context,field,render_as_hidden)
        util = context.get('util', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'\n    ')
        # SOURCE LINE 97
  
        in_library = False
        in_sample_tracking = False
        
        if item_type == 'library':
            item = trans.sa_session.query( trans.app.model.Library ).get( trans.security.decode_id( library_id ) )
        elif item_type == 'folder':
            item = trans.sa_session.query( trans.app.model.LibraryFolder ).get( trans.security.decode_id( folder_id ) )
        elif item_type == 'ldda':
            item = trans.sa_session.query( trans.app.model.LibraryDatasetDatasetAssociation ).get( trans.security.decode_id( ldda_id ) )
        elif item_type == 'request_type':
            item = trans.sa_session.query( trans.app.model.RequestType ).get( trans.security.decode_id( request_type_id ) )
        elif item_type == 'sample':
            item = trans.sa_session.query( trans.app.model.Sample ).get( trans.security.decode_id( sample_id ) )
        
        if cntrller in [ 'library', 'library_admin' ]:
            in_library = True
            template_section_title = 'Other information'
            form_type = trans.model.FormDefinition.types.LIBRARY_INFO_TEMPLATE
            if trans.user_is_admin() and cntrller == 'library_admin':
                can_modify = True
            elif cntrller == 'library':
                can_modify = trans.app.security_agent.can_modify_library_item( trans.get_current_user_roles(), item )
            else:
                can_modify = False
        elif cntrller in [ 'requests_admin', 'requests', 'request_type' ]:
            in_sample_tracking = True
            template_section_title = 'Run details'
            form_type = trans.model.FormDefinition.types.RUN_DETAILS_TEMPLATE
            
        
        # SOURCE LINE 126
        __M_writer(u'\n')
        # SOURCE LINE 127
        if ( in_sample_tracking and editable ) or ( in_library and editable and can_modify ):
            # SOURCE LINE 128
            __M_writer(u'        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">\n                <div class="menubutton popup" id="item-')
            # SOURCE LINE 131
            __M_writer(unicode(item.id))
            __M_writer(u'-popup">')
            __M_writer(unicode(template_section_title))
            __M_writer(u'</div>\n                <div popupmenu="item-')
            # SOURCE LINE 132
            __M_writer(unicode(item.id))
            __M_writer(u'-popup">\n')
            # SOURCE LINE 133
            if in_library and info_association and inherited and can_modify:
                # SOURCE LINE 136
                __M_writer(u'                        <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='library_common', action='add_template', cntrller=cntrller, item_type=item_type, form_type=form_type, library_id=library_id, folder_id=folder_id, ldda_id=ldda_id, show_deleted=show_deleted )))
                __M_writer(u'">Select a different template</a>\n')
                # SOURCE LINE 137
            elif in_library and info_association and not inherited and can_modify:
                # SOURCE LINE 138
                __M_writer(u'                        <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='library_common', action='edit_template', cntrller=cntrller, item_type=item_type, form_type=form_type, library_id=library_id, folder_id=folder_id, ldda_id=ldda_id, show_deleted=show_deleted )))
                __M_writer(u'">Edit template</a>\n                        <a class="action-button" href="')
                # SOURCE LINE 139
                __M_writer(unicode(h.url_for( controller='library_common', action='delete_template', cntrller=cntrller, item_type=item_type, form_type=form_type, library_id=library_id, folder_id=folder_id, ldda_id=ldda_id, show_deleted=show_deleted )))
                __M_writer(u'">Unuse template</a>\n')
                # SOURCE LINE 140
                if item_type not in [ 'ldda', 'library_dataset' ]:
                    # SOURCE LINE 141
                    if info_association.inheritable:
                        # SOURCE LINE 142
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='manage_template_inheritance', cntrller=cntrller, item_type=item_type, library_id=library_id, folder_id=folder_id, ldda_id=ldda_id, show_deleted=show_deleted )))
                        __M_writer(u'">Dis-inherit template</a>\n')
                        # SOURCE LINE 143
                    else:
                        # SOURCE LINE 144
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='manage_template_inheritance', cntrller=cntrller, item_type=item_type, library_id=library_id, folder_id=folder_id, ldda_id=ldda_id, show_deleted=show_deleted )))
                        __M_writer(u'">Inherit template</a>\n')
                        pass
                    pass
                # SOURCE LINE 147
            elif in_sample_tracking:
                # SOURCE LINE 148
                __M_writer(u'                        <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='request_type', action='add_template', cntrller=cntrller, item_type=item_type, form_type=form_type, request_type_id=request_type_id )))
                __M_writer(u'">Select a different template</a>\n                        <a class="action-button" href="')
                # SOURCE LINE 149
                __M_writer(unicode(h.url_for( controller='request_type', action='edit_template', cntrller=cntrller, item_type=item_type, form_type=form_type, request_type_id=request_type_id )))
                __M_writer(u'">Edit template</a>\n                        <a class="action-button" href="')
                # SOURCE LINE 150
                __M_writer(unicode(h.url_for( controller='request_type', action='delete_template', cntrller=cntrller, item_type=item_type, form_type=form_type, request_type_id=request_type_id )))
                __M_writer(u'">Unuse template</a>\n')
                pass
            # SOURCE LINE 152
            __M_writer(u'                </div>\n            </div>\n            <div class="toolFormBody">\n')
            # SOURCE LINE 155
            if in_library and inherited:
                # SOURCE LINE 156
                __M_writer(u'                    <div class="form-row">\n                        <font color="red">\n                            <b>\n                                This is an inherited template and is not required to be used with this ')
                # SOURCE LINE 159
                __M_writer(unicode(item_type))
                __M_writer(u'.  You can \n                                <a href="')
                # SOURCE LINE 160
                __M_writer(unicode(h.url_for( controller='library_common', action='add_template', cntrller=cntrller, item_type=item_type, form_type=form_type, library_id=library_id, folder_id=folder_id, ldda_id=ldda_id, show_deleted=show_deleted )))
                __M_writer(u'"><font color="red">Select a different template</font></a>\n                                or fill in the desired fields and save this one.  This template will not be associated with this ')
                # SOURCE LINE 161
                __M_writer(unicode(item_type))
                __M_writer(u' until you click the Save button.\n                            </b>\n                        </font>\n                    </div>\n')
                pass
            # SOURCE LINE 166
            if in_library:
                # SOURCE LINE 167
                __M_writer(u'                    <form name="edit_info" id="edit_info" action="')
                __M_writer(unicode(h.url_for( controller='library_common', action='edit_template_info', cntrller=cntrller, item_type=item_type, form_type=form_type, library_id=library_id, folder_id=folder_id, ldda_id=ldda_id, show_deleted=show_deleted )))
                __M_writer(u'" method="post">\n')
                # SOURCE LINE 168
            elif in_sample_tracking:
                # SOURCE LINE 169
                __M_writer(u'                    <form name="edit_info" id="edit_info" action="')
                __M_writer(unicode(h.url_for( controller='request_type', action='edit_template_info', cntrller=cntrller, item_type=item_type, form_type=form_type, request_type_id=request_type_id, sample_id=sample_id )))
                __M_writer(u'" method="post">\n')
                pass
            # SOURCE LINE 171
            for i, field in enumerate( widgets ):
                # SOURCE LINE 172
                __M_writer(u'                        <div class="form-row">\n                            <label>')
                # SOURCE LINE 173
                __M_writer(unicode(field[ 'label' ]))
                __M_writer(u'</label>\n                            ')
                # SOURCE LINE 174
                __M_writer(unicode(field[ 'widget' ].get_html()))
                __M_writer(u'\n                            <div class="toolParamHelp" style="clear: both;">\n                                ')
                # SOURCE LINE 176
                __M_writer(unicode(field[ 'helptext' ]))
                __M_writer(u'\n                            </div>\n                            <div style="clear: both"></div>\n                        </div>\n')
                pass
            # SOURCE LINE 181
            __M_writer(u'                    <div class="form-row">\n                        <input type="submit" name="edit_info_button" value="Save"/>\n                    </div>\n                </form>\n            </div>\n        </div>\n        <p/>\n')
            # SOURCE LINE 188
        elif widget_fields_have_contents:
            # SOURCE LINE 189
            __M_writer(u'        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Other information about ')
            # SOURCE LINE 191
            __M_writer(unicode( util.unicodify( item.name )))
            __M_writer(u'</div>\n            <div class="toolFormBody">\n')
            # SOURCE LINE 193
            for i, field in enumerate( widgets ):
                # SOURCE LINE 194
                __M_writer(u'                    ')
                __M_writer(unicode(render_template_field( field )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 196
            __M_writer(u'            </div>\n        </div>\n        <p/>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


