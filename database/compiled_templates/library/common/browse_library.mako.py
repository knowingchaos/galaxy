# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383202403.8358729
_template_filename='templates/webapps/galaxy/library/common/browse_library.mako'
_template_uri='library/common/browse_library.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['body', 'render_content', 'title', 'center_panel', 'stylesheets', 'grid_javascripts', 'init', 'render_dataset', 'render_folder', 'javascripts']


# SOURCE LINE 7

def inherit(context):
    if context.get('use_panels'):
        return '/webapps/galaxy/base_panels.mako'
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7f31cc1a3f90', context._clean_inheritance_tokens(), templateuri=u'/library/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f31cc1a3f90')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f31cc1a3790', context._clean_inheritance_tokens(), templateuri=u'/library/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f31cc1a3790')] = ns

    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7f31cc1a35d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f31cc1a35d0')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f31cc1a3550', context._clean_inheritance_tokens(), templateuri=u'/library/common/library_item_info.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f31cc1a3550')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x7f31cc2ae4d0', context._clean_inheritance_tokens(), templateuri=u'/library/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f31cc2ae4d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n')
        # SOURCE LINE 207
        __M_writer(u'\n\n')
        # SOURCE LINE 311
        __M_writer(u'\n\n')
        # SOURCE LINE 470
        __M_writer(u'\n\n')
        # SOURCE LINE 615
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        def render_content(simple=False):
            return render_render_content(context,simple)
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n    ')
        # SOURCE LINE 40
        __M_writer(unicode(render_content()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_content(context,simple=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        use_panels = _import_ns.get('use_panels', context.get('use_panels', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        comptypes = _import_ns.get('comptypes', context.get('comptypes', UNDEFINED))
        render_actions_on_multiple_items = _import_ns.get('render_actions_on_multiple_items', context.get('render_actions_on_multiple_items', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        current_user_roles = _import_ns.get('current_user_roles', context.get('current_user_roles', UNDEFINED))
        render_compression_types_help = _import_ns.get('render_compression_types_help', context.get('render_compression_types_help', UNDEFINED))
        library = _import_ns.get('library', context.get('library', UNDEFINED))
        show_deleted = _import_ns.get('show_deleted', context.get('show_deleted', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        hidden_folder_ids = _import_ns.get('hidden_folder_ids', context.get('hidden_folder_ids', UNDEFINED))
        created_ldda_ids = _import_ns.get('created_ldda_ids', context.get('created_ldda_ids', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 472
        __M_writer(u'\n    ')
        # SOURCE LINE 473

        from galaxy import util
        from galaxy.webapps.galaxy.controllers.library_common import branch_deleted
        from time import strftime
        
        is_admin = trans.user_is_admin() and cntrller == 'library_admin'
        
        if is_admin:
            can_add = can_modify = can_manage = True
        elif cntrller in [ 'library', 'requests' ]:
            can_add = trans.app.security_agent.can_add_library_item( current_user_roles, library )
            can_modify = trans.app.security_agent.can_modify_library_item( current_user_roles, library )
            can_manage = trans.app.security_agent.can_manage_library_item( current_user_roles, library )
        else:
            can_add = can_modify = can_manage = False
            
        info_association, inherited = library.get_info_association()
        form_type = trans.model.FormDefinition.types.LIBRARY_INFO_TEMPLATE
        
        self.has_accessible_datasets = trans.app.security_agent.has_accessible_library_datasets( trans, library.root_folder, trans.user, current_user_roles )
        root_folder_has_accessible_library_datasets = trans.app.security_agent.has_accessible_library_datasets( trans, library.root_folder, trans.user, current_user_roles, search_downward=False )
        has_accessible_folders = is_admin or trans.app.security_agent.has_accessible_folders( trans, library.root_folder, trans.user, current_user_roles )
        
        tracked_datasets = {}
        
        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
            
        
        # SOURCE LINE 505
        __M_writer(u'\n    \n    <h2>Data Library &ldquo;')
        # SOURCE LINE 507
        __M_writer(unicode(library.name))
        __M_writer(u'&rdquo;</h2>\n    \n     <ul class="manage-table-actions">\n')
        # SOURCE LINE 510
        if not library.deleted and ( is_admin or can_add ):
            # SOURCE LINE 511
            __M_writer(u'             <li><a class="action-button" href="')
            __M_writer(unicode(h.url_for( controller='library_common', action='upload_library_dataset', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( library.root_folder.id ), use_panels=use_panels, show_deleted=show_deleted )))
            __M_writer(u'">Add datasets</a></li>\n             <li><a class="action-button" href="')
            # SOURCE LINE 512
            __M_writer(unicode(h.url_for( controller='library_common', action='create_folder', cntrller=cntrller, parent_id=trans.security.encode_id( library.root_folder.id ), library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
            __M_writer(u'">Add folder</a></li>\n')
            pass
        # SOURCE LINE 514
        if ( ( not library.deleted ) and ( can_modify or can_manage ) ) or ( can_modify and not library.purged ) or ( library.purged ):
            # SOURCE LINE 515
            __M_writer(u'             <li><a class="action-button" id="library-')
            __M_writer(unicode(library.id))
            __M_writer(u'-popup" class="menubutton">Library Actions</a></li>\n             <div popupmenu="library-')
            # SOURCE LINE 516
            __M_writer(unicode(library.id))
            __M_writer(u'-popup">\n')
            # SOURCE LINE 517
            if not library.deleted:
                # SOURCE LINE 518
                if can_modify:
                    # SOURCE LINE 519
                    __M_writer(u'                         <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='library_info', cntrller=cntrller, id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Edit information</a>\n                         <a class="action-button" confirm="Click OK to delete the library named \'')
                    # SOURCE LINE 520
                    __M_writer(unicode(library.name))
                    __M_writer(u'\'." href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='delete_library_item', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_id=trans.security.encode_id( library.id ), item_type='library' )))
                    __M_writer(u'">Delete this data library</a>\n')
                    # SOURCE LINE 521
                    if show_deleted:
                        # SOURCE LINE 522
                        __M_writer(u'                             <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library', cntrller=cntrller, id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=False )))
                        __M_writer(u'">Hide deleted items</a>\n')
                        # SOURCE LINE 523
                    else:
                        # SOURCE LINE 524
                        __M_writer(u'                             <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library', cntrller=cntrller, id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=True )))
                        __M_writer(u'">Show deleted items</a>\n')
                        pass
                    pass
                # SOURCE LINE 527
                if can_modify and not library.info_association:
                    # SOURCE LINE 528
                    __M_writer(u'                         <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='add_template', cntrller=cntrller, item_type='library', form_type=form_type, library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Use template</a>\n')
                    pass
                # SOURCE LINE 530
                if can_modify and info_association:
                    # SOURCE LINE 531
                    __M_writer(u'                         <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='edit_template', cntrller=cntrller, item_type='library', form_type=form_type, library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Edit template</a>\n                         <a class="action-button" href="')
                    # SOURCE LINE 532
                    __M_writer(unicode(h.url_for( controller='library_common', action='delete_template', cntrller=cntrller, item_type='library', form_type=form_type, library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Unuse template</a>\n')
                    pass
                # SOURCE LINE 534
                if can_manage:
                    # SOURCE LINE 535
                    if not trans.app.security_agent.library_is_public( library, contents=True ):
                        # SOURCE LINE 536
                        __M_writer(u'                             <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='make_library_item_public', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_type='library', id=trans.security.encode_id( library.id ), contents=True, use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Make public</a>\n')
                        pass
                    # SOURCE LINE 538
                    __M_writer(u'                         <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='library_permissions', cntrller=cntrller, id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Edit permissions</a>\n')
                    pass
                # SOURCE LINE 540
                if root_folder_has_accessible_library_datasets:
                    # SOURCE LINE 541
                    __M_writer(u'                        <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='import_datasets_to_histories', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( library.root_folder.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Select datasets for import into selected histories</a>\n')
                    pass
                # SOURCE LINE 543
            elif can_modify and not library.purged:
                # SOURCE LINE 544
                __M_writer(u'                     <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='library_common', action='undelete_library_item', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_id=trans.security.encode_id( library.id ), item_type='library', use_panels=use_panels )))
                __M_writer(u'">Undelete this data library</a>\n')
                # SOURCE LINE 545
            elif library.purged:
                # SOURCE LINE 546
                __M_writer(u'                     <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='library_common', action='browse_library', cntrller=cntrller, id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                __M_writer(u'">This data library has been purged</a>\n')
                pass
            # SOURCE LINE 548
            __M_writer(u'             </div>\n')
            pass
        # SOURCE LINE 550
        __M_writer(u'    </ul>\n    \n')
        # SOURCE LINE 552
        if message:
            # SOURCE LINE 553
            __M_writer(u'        ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 555
        __M_writer(u'\n')
        # SOURCE LINE 556
        if library.synopsis not in [ '', 'None', None ]:
            # SOURCE LINE 557
            __M_writer(u'        <div class="libraryItemBody">\n            ')
            # SOURCE LINE 558
            __M_writer(unicode(library.synopsis))
            __M_writer(u'\n        </div>\n')
            pass
        # SOURCE LINE 561
        __M_writer(u'    \n')
        # SOURCE LINE 562
        if self.has_accessible_datasets:
            # SOURCE LINE 563
            __M_writer(u'        <form name="act_on_multiple_datasets" action="')
            __M_writer(unicode(h.url_for( controller='library_common', action='act_on_multiple_datasets', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
            __M_writer(u'" onSubmit="javascript:return checkForm();" method="post">\n')
            pass
        # SOURCE LINE 565
        if has_accessible_folders:
            # SOURCE LINE 566
            __M_writer(u'        <table cellspacing="0" cellpadding="0" border="0" width="100%" class="grid" id="library-grid">\n            <thead>\n                <tr class="libraryTitle">\n                    <th>\n')
            # SOURCE LINE 570
            if self.has_accessible_datasets:
                # SOURCE LINE 571
                __M_writer(u'                            <input type="checkbox" id="checkAll" name=select_all_datasets_checkbox value="true" onclick=\'checkAllFields(1);\'/><input type="hidden" name=select_all_datasets_checkbox value="true"/>\n')
                pass
            # SOURCE LINE 573
            __M_writer(u'                        Name\n                    </th>\n')
            # SOURCE LINE 575
            if not simple:
                # SOURCE LINE 576
                __M_writer(u'                        <th>Message</th>\n                        <th>Data type</th>\n')
                pass
            # SOURCE LINE 579
            __M_writer(u'                    <th>Date uploaded</th>\n                    <th>File size</th>\n                </tr>\n            </thead>\n            ')
            # SOURCE LINE 583
            row_counter = RowCounter() 
            
            __M_writer(u'\n')
            # SOURCE LINE 584
            if cntrller in [ 'library', 'requests' ]:
                # SOURCE LINE 585
                __M_writer(u'                ')
                __M_writer(unicode(self.render_folder( 'library', library.root_folder, 0, created_ldda_ids, library, hidden_folder_ids, tracked_datasets, show_deleted=show_deleted, parent=None, row_counter=row_counter, root_folder=True, simple=simple )))
                __M_writer(u'\n')
                # SOURCE LINE 586
                if not library.deleted and self.has_accessible_datasets and not simple:
                    # SOURCE LINE 587
                    __M_writer(u'                    ')
                    __M_writer(unicode(render_actions_on_multiple_items()))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 589
            elif ( trans.user_is_admin() and cntrller in [ 'library_admin', 'requests_admin' ] ):
                # SOURCE LINE 590
                __M_writer(u'                ')
                __M_writer(unicode(self.render_folder( 'library_admin', library.root_folder, 0, created_ldda_ids, library, [], tracked_datasets, show_deleted=show_deleted, parent=None, row_counter=row_counter, root_folder=True )))
                __M_writer(u'\n')
                # SOURCE LINE 591
                if not library.deleted and not show_deleted and self.has_accessible_datasets:
                    # SOURCE LINE 592
                    __M_writer(u'                    ')
                    __M_writer(unicode(render_actions_on_multiple_items()))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 595
            __M_writer(u'        </table>\n')
            pass
        # SOURCE LINE 597
        if self.has_accessible_datasets:
            # SOURCE LINE 598
            __M_writer(u'        </form>\n')
            pass
        # SOURCE LINE 600
        __M_writer(u'     \n')
        # SOURCE LINE 601
        if tracked_datasets:
            # SOURCE LINE 602
            __M_writer(u'        <script type="text/javascript">\n            // Updater\n            updater({')
            # SOURCE LINE 604
            __M_writer(unicode( ",".join( [ '"%s" : "%s"' % ( k, v ) for k, v in tracked_datasets.iteritems() ] ) ))
            __M_writer(u'});\n        </script>\n        <!-- running: do not change this comment, used by TwillTestCase.library_wait -->\n')
            pass
        # SOURCE LINE 608
        __M_writer(u'    \n')
        # SOURCE LINE 609
        if self.has_accessible_datasets and not simple:
            # SOURCE LINE 610
            __M_writer(u'        ')
            __M_writer(unicode(render_compression_types_help( comptypes )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 612
        if not has_accessible_folders:
            # SOURCE LINE 613
            __M_writer(u"        The data library '")
            __M_writer(unicode(library.name))
            __M_writer(u"' does not contain any datasets that you can access.\n")
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'Browse data library')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        def render_content(simple=False):
            return render_render_content(context,simple)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n   <div style="overflow: auto; height: 100%;">\n       <div class="page-container" style="padding: 10px;">\n           ')
        # SOURCE LINE 33
        __M_writer(unicode(render_content()))
        __M_writer(u'\n       </div>\n   </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n    ')
        # SOURCE LINE 45
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 46
        __M_writer(unicode(h.css( "library" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        library = _import_ns.get('library', context.get('library', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\n    <script type="text/javascript">\n        var init_libraries = function() {\n            var storage_id = "library-expand-state-')
        # SOURCE LINE 59
        __M_writer(unicode(trans.security.encode_id(library.id)))
        __M_writer(u'";\n            \n            var restore_folder_state = function() {\n                var state = $.jStorage.get(storage_id);\n                if (state) {\n                    for (var id in state) {\n                        if (state[id] === true) {\n                            var row = $("#" + id),\n                                index = row.parent().children().index(row);\n                            row.addClass("expanded").show();\n                            row.siblings().filter("tr[parent=\'" + index + "\']").show();\n                        }\n                    }\n                }\n            };\n            \n            var save_folder_state = function() {\n                var state = {};\n                $("tr.folderRow").each( function() {\n                    var folder = $(this);\n                    state[folder.attr("id")] = folder.hasClass("expanded");\n                });\n                $.jStorage.set(storage_id, state);\n            };\n            \n            $("#library-grid").each(function() {\n                var child_of_parent_cache = {};\n                // Recursively fill in children and descendents of each row\n                var process_row = function(q, parents) {\n                    // Find my index\n                    var parent = q.parent(),\n                        this_level = child_of_parent_cache[parent] || (child_of_parent_cache[parent] = parent.children());\n                        \n                    var index = this_level.index(q);\n                    // Find my immediate children\n                    var children = $(par_child_dict[index]);\n                    // Recursively handle them\n                    var descendents = children;\n                    children.each( function() {\n                        child_descendents = process_row( $(this), parents.add(q) );\n                        descendents = descendents.add(child_descendents);\n                    });\n                    // Set up expand / hide link\n                    var expand_fn = function() {\n                        if ( q.hasClass("expanded") ) {\n                            descendents.hide();\n                            descendents.removeClass("expanded");\n                            q.removeClass("expanded");\n                        } else {\n                            children.show();\n                            q.addClass("expanded");\n                        }\n                        save_folder_state();\n                    };\n                    $("." + q.attr("id") + "-click").click(expand_fn);\n                    // Check/uncheck boxes in subfolders.\n                    q.children("td").children("input[type=checkbox]").click( function() {\n                        if ( $(this).is(":checked") ) {\n                            descendents.find("input[type=checkbox]").attr("checked", true);\n                        } else {\n                            descendents.find("input[type=checkbox]").attr("checked", false);\n                            // If you uncheck a lower level checkbox, uncheck the boxes above it\n                            // (since deselecting a child means the parent is not fully selected any more).\n                            parents.children("td").children("input[type=checkbox]").attr("checked", false);\n                        }\n                    });\n                    // return descendents for use by parent\n                    return descendents;\n                }\n                \n                // Initialize dict[parent_id] = rows_which_have_that_parent_id_as_parent_attr\n                var par_child_dict = {},\n                    no_parent = [];\n                \n                $(this).find("tbody tr").each( function() {\n                    if ( $(this).attr("parent")) {\n                        var parent = $(this).attr("parent");\n                        if (par_child_dict[parent] !== undefined) {\n                            par_child_dict[parent].push(this);\n                        } else {\n                            par_child_dict[parent] = [this];\n                        }\n                    } else {\n                        no_parent.push(this);\n                    }                        \n                });\n                \n                $(no_parent).each( function() {\n                    descendents = process_row( $(this), $([]) );\n                    descendents.hide();\n               });\n            });\n            \n            restore_folder_state();\n        };\n        $(function() {\n            init_libraries();\n        });\n        \n        // Looks for changes in dataset state using an async request. Keeps\n        // calling itself (via setTimeout) until all datasets are in a terminal\n        // state.\n        var updater = function ( tracked_datasets ) {\n            // Check if there are any items left to track\n            var empty = true;\n            for ( i in tracked_datasets ) {\n                empty = false;\n                break;\n            }\n            if ( ! empty ) {\n                setTimeout( function() { updater_callback( tracked_datasets ) }, 3000 );\n            }\n        };\n        var updater_callback = function ( tracked_datasets ) {\n            // Build request data\n            var ids = []\n            var states = []\n            $.each( tracked_datasets, function ( id, state ) {\n                ids.push( id );\n                states.push( state );\n            });\n            // Make ajax call\n            $.ajax( {\n                type: "POST",\n                url: "')
        # SOURCE LINE 183
        __M_writer(unicode(h.url_for( controller='library_common', action='library_item_updates' )))
        __M_writer(u'",\n                dataType: "json",\n                data: { ids: ids.join( "," ), states: states.join( "," ) },\n                success : function ( data ) {\n                    $.each( data, function( id, val ) {\n                        // Replace HTML\n                        var cell = $("#libraryItem-" + id).find("#libraryItemInfo");\n                        cell.html( val.html );\n                        // If new state was terminal, stop tracking\n                        if (( val.state == "ok") || ( val.state == "error") || ( val.state == "empty") || ( val.state == "deleted" ) || ( val.state == "discarded" )) {\n                            delete tracked_datasets[ parseInt(id) ];\n                        } else {\n                            tracked_datasets[ parseInt(id) ] = val.state;\n                        }\n                    });\n                    updater( tracked_datasets ); \n                },\n                error: function() {\n                    // Just retry, like the old method, should try to be smarter\n                    updater( tracked_datasets );\n                }\n            });\n        };\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n')
        # SOURCE LINE 17

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        self.active_view="user"
        self.overlay_visible=False
        self.has_accessible_datasets = False
        
        
        # SOURCE LINE 24
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_dataset(context,cntrller,ldda,library_dataset,selected,library,folder,pad,parent,row_counter,tracked_datasets,show_deleted=False,simple=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        use_panels = _import_ns.get('use_panels', context.get('use_panels', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        current_user_roles = _import_ns.get('current_user_roles', context.get('current_user_roles', UNDEFINED))
        render_library_item_info = _import_ns.get('render_library_item_info', context.get('render_library_item_info', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 209
        __M_writer(u'\n    ')
        # SOURCE LINE 210

        ## The received ldda must always be a LibraryDatasetDatasetAssociation object.  The object id passed to methods
        ## from the drop down menu should be the ldda id to prevent id collision ( which could happen when displaying
        ## children, which are always lddas ).  We also need to make sure we're displaying the latest version of this
        ## library_dataset, so we display the attributes from the ldda.
        
        from galaxy.webapps.galaxy.controllers.library_common import branch_deleted
        
        is_admin = trans.user_is_admin() and cntrller == 'library_admin'
        
        if ldda == library_dataset.library_dataset_dataset_association:
            current_version = True
            if is_admin:
                can_modify = can_manage = True
            elif cntrller in [ 'library', 'requests' ]:
                can_modify = trans.app.security_agent.can_modify_library_item( current_user_roles, library_dataset )
                can_manage = trans.app.security_agent.can_manage_library_item( current_user_roles, library_dataset )
            else:
                can_modify = can_manage = False
        else:
            current_version = False
        if current_version and ldda.state not in ( 'ok', 'error', 'empty', 'deleted', 'discarded' ):
            tracked_datasets[ldda.id] = ldda.state
        info_association, inherited = ldda.get_info_association( restrict=True )
        form_type = trans.model.FormDefinition.types.LIBRARY_INFO_TEMPLATE
            
        
        # SOURCE LINE 235
        __M_writer(u'\n')
        # SOURCE LINE 236
        if current_version and ( not ldda.library_dataset.deleted or show_deleted ):
            # SOURCE LINE 237
            __M_writer(u'        <tr class="datasetRow"\n')
            # SOURCE LINE 238
            if parent is not None:
                # SOURCE LINE 239
                __M_writer(u'                parent="')
                __M_writer(unicode(parent))
                __M_writer(u'"\n')
                pass
            # SOURCE LINE 241
            __M_writer(u'            id="libraryItem-')
            __M_writer(unicode(ldda.id))
            __M_writer(u'">\n            <td style="padding-left: ')
            # SOURCE LINE 242
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n                <input style="float: left;" type="checkbox" name="ldda_ids" id="')
            # SOURCE LINE 243
            __M_writer(unicode(trans.security.encode_id( ldda.id )))
            __M_writer(u'" value="')
            __M_writer(unicode(trans.security.encode_id( ldda.id )))
            __M_writer(u'"\n')
            # SOURCE LINE 244
            if selected:
                # SOURCE LINE 245
                __M_writer(u'                    checked="checked"\n')
                pass
            # SOURCE LINE 247
            __M_writer(u'                />\n')
            # SOURCE LINE 248
            if simple:
                # SOURCE LINE 249
                __M_writer(u'                    <label for="')
                __M_writer(unicode(trans.security.encode_id( ldda.id )))
                __M_writer(u'">')
                __M_writer(unicode( util.unicodify( ldda.name )))
                __M_writer(u'</label>\n')
                # SOURCE LINE 250
            else:
                # SOURCE LINE 251
                __M_writer(u'                    <div style="float: left; margin-left: 1px;" class="menubutton split popup" id="dataset-')
                __M_writer(unicode(ldda.id))
                __M_writer(u'-popup">\n                        <a class="view-info" href="')
                # SOURCE LINE 252
                __M_writer(unicode(h.url_for( controller='library_common', action='ldda_info', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), id=trans.security.encode_id( ldda.id ), use_panels=use_panels, show_deleted=show_deleted )))
                __M_writer(u'">\n')
                # SOURCE LINE 253
                if ldda.library_dataset.deleted:
                    # SOURCE LINE 254
                    __M_writer(u'                                <div class="libraryItem-error">')
                    __M_writer(unicode(util.unicodify( ldda.name )))
                    __M_writer(u'</div>\n')
                    # SOURCE LINE 255
                else:
                    # SOURCE LINE 256
                    __M_writer(u'                                ')
                    __M_writer(unicode(util.unicodify( ldda.name )))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 258
                __M_writer(u'                        </a>\n                    </div>\n')
                # SOURCE LINE 260
                if not library.deleted:
                    # SOURCE LINE 261
                    __M_writer(u'                        <div popupmenu="dataset-')
                    __M_writer(unicode(ldda.id))
                    __M_writer(u'-popup">\n')
                    # SOURCE LINE 262
                    if not branch_deleted( folder ) and not ldda.library_dataset.deleted and can_modify:
                        # SOURCE LINE 263
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='ldda_edit_info', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), id=trans.security.encode_id( ldda.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Edit information</a>\n                                <a class="action-button" href="')
                        # SOURCE LINE 264
                        __M_writer(unicode(h.url_for( controller='library_common', action='move_library_item', cntrller=cntrller, item_type='ldda', item_id=trans.security.encode_id( ldda.id ), source_library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Move this dataset</a>\n')
                        # SOURCE LINE 265
                    else:
                        # SOURCE LINE 266
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='ldda_info', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), id=trans.security.encode_id( ldda.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">View information</a>\n')
                        pass
                    # SOURCE LINE 268
                    if not branch_deleted( folder ) and not ldda.library_dataset.deleted and can_modify and not info_association:
                        # SOURCE LINE 269
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='add_template', cntrller=cntrller, item_type='ldda', form_type=form_type, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), ldda_id=trans.security.encode_id( ldda.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Use template</a>\n')
                        pass
                    # SOURCE LINE 271
                    if not branch_deleted( folder ) and not ldda.library_dataset.deleted and can_modify and info_association:
                        # SOURCE LINE 272
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='edit_template', cntrller=cntrller, item_type='ldda', form_type=form_type, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), ldda_id=trans.security.encode_id( ldda.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Edit template</a>\n                                <a class="action-button" href="')
                        # SOURCE LINE 273
                        __M_writer(unicode(h.url_for( controller='library_common', action='delete_template', cntrller=cntrller, item_type='ldda', form_type=form_type, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), ldda_id=trans.security.encode_id( ldda.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Unuse template</a>\n')
                        pass
                    # SOURCE LINE 275
                    if not branch_deleted( folder ) and not ldda.library_dataset.deleted and can_manage:
                        # SOURCE LINE 276
                        if not trans.app.security_agent.dataset_is_public( ldda.dataset ):
                            # SOURCE LINE 277
                            __M_writer(u'                                    <a class="action-button" href="')
                            __M_writer(unicode(h.url_for( controller='library_common', action='make_library_item_public', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_type='ldda', id=trans.security.encode_id( ldda.dataset.id ), use_panels=use_panels, show_deleted=show_deleted )))
                            __M_writer(u'">Make public</a>\n')
                            pass
                        # SOURCE LINE 279
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='ldda_permissions', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), id=trans.security.encode_id( ldda.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Edit permissions</a>\n')
                        pass
                    # SOURCE LINE 281
                    if not branch_deleted( folder ) and not ldda.library_dataset.deleted and can_modify:
                        # SOURCE LINE 282
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='upload_library_dataset', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), replace_id=trans.security.encode_id( library_dataset.id ), show_deleted=show_deleted )))
                        __M_writer(u'">Upload a new version of this dataset</a>\n')
                        pass
                    # SOURCE LINE 284
                    if not branch_deleted( folder ) and not ldda.library_dataset.deleted and ldda.has_data:
                        # SOURCE LINE 285
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='import_datasets_to_histories', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), ldda_ids=trans.security.encode_id( ldda.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Import this dataset into selected histories</a>\n                                <a class="action-button" href="')
                        # SOURCE LINE 286
                        __M_writer(unicode(h.url_for( controller='library_common', action='download_dataset_from_folder', cntrller=cntrller, id=trans.security.encode_id( ldda.id ), library_id=trans.security.encode_id( library.id ), use_panels=use_panels )))
                        __M_writer(u'">Download this dataset</a>\n')
                        pass
                    # SOURCE LINE 288
                    if can_modify:
                        # SOURCE LINE 289
                        if not library.deleted and not branch_deleted( folder ) and not ldda.library_dataset.deleted:
                            # SOURCE LINE 290
                            __M_writer(u'                                    <a class="action-button" confirm="Click OK to delete dataset \'')
                            __M_writer(unicode(util.unicodify( ldda.name )))
                            __M_writer(u'\'." href="')
                            __M_writer(unicode(h.url_for( controller='library_common', action='delete_library_item', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_id=trans.security.encode_id( library_dataset.id ), item_type='library_dataset', show_deleted=show_deleted )))
                            __M_writer(u'">Delete this dataset</a>\n')
                            # SOURCE LINE 291
                        elif not library.deleted and not branch_deleted( folder ) and not ldda.library_dataset.purged and ldda.library_dataset.deleted:
                            # SOURCE LINE 292
                            __M_writer(u'                                    <a class="action-button" href="')
                            __M_writer(unicode(h.url_for( controller='library_common', action='undelete_library_item', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_id=trans.security.encode_id( library_dataset.id ), item_type='library_dataset', show_deleted=show_deleted )))
                            __M_writer(u'">Undelete this dataset</a>\n')
                            pass
                        pass
                    # SOURCE LINE 295
                    __M_writer(u'                        </div>\n')
                    pass
                pass
            # SOURCE LINE 298
            __M_writer(u'            </td>\n')
            # SOURCE LINE 299
            if not simple:
                # SOURCE LINE 300
                __M_writer(u'                <td id="libraryItemInfo">')
                __M_writer(unicode(render_library_item_info( ldda )))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 301
                __M_writer(unicode(ldda.extension))
                __M_writer(u'</td>\n')
                pass
            # SOURCE LINE 303
            __M_writer(u'            <td>')
            __M_writer(unicode(ldda.create_time.strftime( "%Y-%m-%d" )))
            __M_writer(u'</td>\n            <td>')
            # SOURCE LINE 304
            __M_writer(unicode(ldda.get_size( nice_size=True )))
            __M_writer(u'</td>\n        </tr>\n        ')
            # SOURCE LINE 306

            my_row = row_counter.count
            row_counter.increment()
                    
            
            # SOURCE LINE 309
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_folder(context,cntrller,folder,folder_pad,created_ldda_ids,library,hidden_folder_ids,tracked_datasets,show_deleted=False,parent=None,row_counter=None,root_folder=False,simple=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        use_panels = _import_ns.get('use_panels', context.get('use_panels', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        current_user_roles = _import_ns.get('current_user_roles', context.get('current_user_roles', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        def render_dataset(cntrller,ldda,library_dataset,selected,library,folder,pad,parent,row_counter,tracked_datasets,show_deleted=False,simple=False):
            return render_render_dataset(context,cntrller,ldda,library_dataset,selected,library,folder,pad,parent,row_counter,tracked_datasets,show_deleted,simple)
        def render_folder(cntrller,folder,folder_pad,created_ldda_ids,library,hidden_folder_ids,tracked_datasets,show_deleted=False,parent=None,row_counter=None,root_folder=False,simple=False):
            return render_render_folder(context,cntrller,folder,folder_pad,created_ldda_ids,library,hidden_folder_ids,tracked_datasets,show_deleted,parent,row_counter,root_folder,simple)
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 313
        __M_writer(u'\n    ')
        # SOURCE LINE 314

        from galaxy.webapps.galaxy.controllers.library_common import active_folders, active_folders_and_library_datasets, activatable_folders_and_library_datasets, branch_deleted
        
        is_admin = trans.user_is_admin() and cntrller == 'library_admin'
        has_accessible_library_datasets = trans.app.security_agent.has_accessible_library_datasets( trans, folder, trans.user, current_user_roles, search_downward=False )
        
        if root_folder:
            pad = folder_pad
            expander = h.url_for("/static/images/silk/resultset_bottom.png")
            folder_img = h.url_for("/static/images/silk/folder_page.png")
        else:
            pad = folder_pad + 20
            expander = h.url_for("/static/images/silk/resultset_next.png")
            folder_img = h.url_for("/static/images/silk/folder.png")
        if created_ldda_ids:
            created_ldda_ids = util.listify( created_ldda_ids )
        if str( folder.id ) in hidden_folder_ids:
            return ""
        my_row = None
        if is_admin:
            can_add = can_modify = can_manage = True
        elif cntrller in [ 'library' ]:
            can_access, folder_ids = trans.app.security_agent.check_folder_contents( trans.user, current_user_roles, folder )
            if not can_access:
                can_show, folder_ids = \
                    trans.app.security_agent.show_library_item( trans.user,
                                                                current_user_roles,
                                                                folder,
                                                                [ trans.app.security_agent.permitted_actions.LIBRARY_ADD,
                                                                  trans.app.security_agent.permitted_actions.LIBRARY_MODIFY,
                                                                  trans.app.security_agent.permitted_actions.LIBRARY_MANAGE ] )
                if not can_show:
                    return ""
            can_add = trans.app.security_agent.can_add_library_item( current_user_roles, folder )
            can_modify = trans.app.security_agent.can_modify_library_item( current_user_roles, folder )
            can_manage = trans.app.security_agent.can_manage_library_item( current_user_roles, folder )
        else:
            can_add = can_modify = can_manage = False
            
        form_type = trans.model.FormDefinition.types.LIBRARY_INFO_TEMPLATE
        info_association, inherited = folder.get_info_association( restrict=True )
            
        
        # SOURCE LINE 355
        __M_writer(u'\n')
        # SOURCE LINE 356
        if not root_folder and ( not folder.deleted or show_deleted ):
            # SOURCE LINE 357
            __M_writer(u'        ')
            encoded_id = trans.security.encode_id( folder.id ) 
            
            __M_writer(u'\n        <tr id="folder-')
            # SOURCE LINE 358
            __M_writer(unicode(encoded_id))
            __M_writer(u'" class="folderRow libraryOrFolderRow"\n')
            # SOURCE LINE 359
            if parent is not None:
                # SOURCE LINE 360
                __M_writer(u'                parent="')
                __M_writer(unicode(parent))
                __M_writer(u'"\n                style="display: none;"\n')
                pass
            # SOURCE LINE 363
            __M_writer(u'            >\n            <td style="padding-left: ')
            # SOURCE LINE 364
            __M_writer(unicode(folder_pad))
            __M_writer(u'px;">\n                <input type="checkbox" class="folderCheckbox"/>\n                <span class="expandLink folder-')
            # SOURCE LINE 366
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                    <div style="float: left; margin-left: 2px;" class="menubutton split popup" id="folder_img-')
            # SOURCE LINE 367
            __M_writer(unicode(folder.id))
            __M_writer(u'-popup">\n                        <a class="folder-')
            # SOURCE LINE 368
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click" href="javascript:void(0);">\n                            <span class="rowIcon"></span>\n')
            # SOURCE LINE 370
            if folder.deleted:
                # SOURCE LINE 371
                __M_writer(u'                                <div class="libraryItem-error">')
                __M_writer(unicode(folder.name))
                __M_writer(u'</div>\n')
                # SOURCE LINE 372
            else:
                # SOURCE LINE 373
                __M_writer(u'                                ')
                __M_writer(unicode(folder.name))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 375
            __M_writer(u'                        </a>\n                    </div>\n                </span>\n')
            # SOURCE LINE 378
            if not library.deleted:
                # SOURCE LINE 379
                __M_writer(u'                    <div popupmenu="folder_img-')
                __M_writer(unicode(folder.id))
                __M_writer(u'-popup">\n')
                # SOURCE LINE 380
                if not branch_deleted( folder ) and can_add:
                    # SOURCE LINE 381
                    __M_writer(u'                            <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='upload_library_dataset', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Add datasets</a>\n                            <a class="action-button" href="')
                    # SOURCE LINE 382
                    __M_writer(unicode(h.url_for( controller='library_common', action='create_folder', cntrller=cntrller, parent_id=trans.security.encode_id( folder.id ), library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Add sub-folder</a>\n')
                    pass
                # SOURCE LINE 384
                if not branch_deleted( folder ):
                    # SOURCE LINE 385
                    if has_accessible_library_datasets:
                        # SOURCE LINE 386
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='import_datasets_to_histories', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Select datasets for import into selected histories</a>\n')
                        pass
                    # SOURCE LINE 388
                    if can_modify:
                        # SOURCE LINE 389
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='folder_info', cntrller=cntrller, id=trans.security.encode_id( folder.id ), library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Edit information</a>\n                                <a class="action-button" href="')
                        # SOURCE LINE 390
                        __M_writer(unicode(h.url_for( controller='library_common', action='move_library_item', cntrller=cntrller, item_type='folder', item_id=trans.security.encode_id( folder.id ), source_library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Move this folder</a>\n')
                        # SOURCE LINE 391
                    else:
                        # SOURCE LINE 392
                        __M_writer(u'                                <a class="action-button" class="view-info" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='folder_info', cntrller=cntrller, id=trans.security.encode_id( folder.id ), library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">View information</a>\n')
                        pass
                    pass
                # SOURCE LINE 395
                if not branch_deleted( folder ) and can_modify and not info_association:
                    # SOURCE LINE 396
                    __M_writer(u'                            <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='add_template', cntrller=cntrller, item_type='folder', form_type=form_type, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Use template</a>\n')
                    pass
                # SOURCE LINE 398
                if not branch_deleted( folder ) and can_modify and info_association:
                    # SOURCE LINE 399
                    __M_writer(u'                            <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='edit_template', cntrller=cntrller, item_type='folder', form_type=form_type, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Edit template</a>\n                            <a class="action-button" href="')
                    # SOURCE LINE 400
                    __M_writer(unicode(h.url_for( controller='library_common', action='delete_template', cntrller=cntrller, item_type='folder', form_type=form_type, library_id=trans.security.encode_id( library.id ), folder_id=trans.security.encode_id( folder.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Unuse template</a>\n')
                    pass
                # SOURCE LINE 402
                if not branch_deleted( folder ) and can_manage:
                    # SOURCE LINE 403
                    if not trans.app.security_agent.folder_is_public( folder ):
                        # SOURCE LINE 404
                        __M_writer(u'                               <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='make_library_item_public', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_type='folder', id=trans.security.encode_id( folder.id ), use_panels=use_panels, show_deleted=show_deleted )))
                        __M_writer(u'">Make public</a>\n')
                        pass
                    # SOURCE LINE 406
                    __M_writer(u'                            <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='library_common', action='folder_permissions', cntrller=cntrller, id=trans.security.encode_id( folder.id ), library_id=trans.security.encode_id( library.id ), use_panels=use_panels, show_deleted=show_deleted )))
                    __M_writer(u'">Edit permissions</a>\n')
                    pass
                # SOURCE LINE 408
                if can_modify:
                    # SOURCE LINE 409
                    if not library.deleted and not folder.deleted:
                        # SOURCE LINE 410
                        __M_writer(u'                                <a class="action-button" confirm="Click OK to delete the folder \'')
                        __M_writer(unicode(folder.name))
                        __M_writer(u'.\'" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='delete_library_item', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_id=trans.security.encode_id( folder.id ), item_type='folder', show_deleted=show_deleted )))
                        __M_writer(u'">Delete this folder</a>\n')
                        # SOURCE LINE 411
                    elif not library.deleted and folder.deleted and not folder.purged:
                        # SOURCE LINE 412
                        __M_writer(u'                                <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='library_common', action='undelete_library_item', cntrller=cntrller, library_id=trans.security.encode_id( library.id ), item_id=trans.security.encode_id( folder.id ), item_type='folder', show_deleted=show_deleted )))
                        __M_writer(u'">Undelete this folder</a>\n')
                        pass
                    pass
                # SOURCE LINE 415
                __M_writer(u'                    </div>\n')
                pass
            # SOURCE LINE 417
            __M_writer(u'            <td>\n')
            # SOURCE LINE 418
            if folder.description:
                # SOURCE LINE 419
                __M_writer(u'                ')
                __M_writer(unicode(folder.description))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 421
            __M_writer(u'            <td colspan="3"></td>\n        </tr>\n        ')
            # SOURCE LINE 423

            my_row = row_counter.count
            row_counter.increment()
                    
            
            # SOURCE LINE 426
            __M_writer(u'\n')
            pass
        # SOURCE LINE 428
        __M_writer(u'    ')

        if show_deleted:
            sub_folders, library_datasets = activatable_folders_and_library_datasets( trans, folder )
        else:
            sub_folders, library_datasets = active_folders_and_library_datasets( trans, folder )
            
        
        # SOURCE LINE 433
        __M_writer(u'\n')
        # SOURCE LINE 434
        if is_admin:
            # SOURCE LINE 435
            for sub_folder in sub_folders:
                # SOURCE LINE 436
                __M_writer(u'            ')
                __M_writer(unicode(render_folder( cntrller, sub_folder, pad, created_ldda_ids, library, [], tracked_datasets, show_deleted=show_deleted, parent=my_row, row_counter=row_counter, root_folder=False )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 438
            for library_dataset in library_datasets:
                # SOURCE LINE 439
                __M_writer(u'            ')

                ldda = library_dataset.library_dataset_dataset_association
                if ldda:
                    # There should always be an ldda, but some users running their own instances have reported that
                    # some of their LibraryDatasets have no associated lddas
                    selected = created_ldda_ids and str( ldda.id ) in created_ldda_ids
                            
                
                # SOURCE LINE 445
                __M_writer(u'\n')
                # SOURCE LINE 446
                if ldda:
                    # SOURCE LINE 447
                    __M_writer(u'                ')
                    __M_writer(unicode(render_dataset( cntrller, ldda, library_dataset, selected, library, folder, pad, my_row, row_counter, tracked_datasets, show_deleted=show_deleted )))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 450
        else:
            # SOURCE LINE 451
            for sub_folder in sub_folders:
                # SOURCE LINE 452
                __M_writer(u'            ')
                __M_writer(unicode(render_folder( cntrller, sub_folder, pad, created_ldda_ids, library, hidden_folder_ids, tracked_datasets, show_deleted=show_deleted, parent=my_row, row_counter=row_counter, root_folder=False, simple=simple )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 454
            for library_dataset in library_datasets:
                # SOURCE LINE 455
                __M_writer(u'            ')

                ldda = library_dataset.library_dataset_dataset_association
                if ldda:
                    # There should always be an ldda, but some users running their own instances have reported that
                    # some of their LibraryDatasets have no associated lddas
                    can_access = trans.app.security_agent.can_access_dataset( current_user_roles, ldda.dataset )
                    selected = created_ldda_ids and str( ldda.id ) in created_ldda_ids
                else:
                    can_access = False
                            
                
                # SOURCE LINE 464
                __M_writer(u'\n')
                # SOURCE LINE 465
                if can_access:
                    # SOURCE LINE 466
                    __M_writer(u'                ')
                    __M_writer(unicode(render_dataset( cntrller, ldda, library_dataset, selected, library, folder, pad, my_row, row_counter, tracked_datasets, show_deleted=show_deleted, simple=simple )))
                    __M_writer(u'\n')
                    pass
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f31cc1a3f90')._populate(_import_ns, [u'render_compression_types_help'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3790')._populate(_import_ns, [u'render_actions_on_multiple_items'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a35d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f31cc1a3550')._populate(_import_ns, [u'render_library_item_info'])
        _mako_get_namespace(context, '__anon_0x7f31cc2ae4d0')._populate(_import_ns, [u'common_javascripts'])
        common_javascripts = _import_ns.get('common_javascripts', context.get('common_javascripts', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer(u'\n    ')
        # SOURCE LINE 50
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 51
        __M_writer(unicode(h.js("libs/jquery/jstorage")))
        __M_writer(u'\n    ')
        # SOURCE LINE 52
        __M_writer(unicode(common_javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 53
        __M_writer(unicode(self.grid_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


