# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383491728.8116691
_template_filename='templates/webapps/tool_shed/category/grid.mako'
_template_uri='/webapps/tool_shed/category/grid.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['make_grid', 'render_grid_header', 'center_panel', 'grid_body']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7057910', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7057910')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7057750', context._clean_inheritance_tokens(), templateuri=u'/grid_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7057750')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7057c90', context._clean_inheritance_tokens(), templateuri=u'/grid_base.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7057c90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/grid_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7057910')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7057750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7057c90')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n\n')
        # SOURCE LINE 56
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_make_grid(context,grid,repo_grid):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7057910')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7057750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7057c90')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_grid_table = _import_ns.get('render_grid_table', context.get('render_grid_table', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        show_item_checkboxes = _import_ns.get('show_item_checkboxes', context.get('show_item_checkboxes', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        render_message = _import_ns.get('render_message', context.get('render_message', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n    <div class="loading-elt-overlay"></div>\n    <table>\n        <tr>\n            <td width="75%">')
        # SOURCE LINE 37
        __M_writer(unicode(self.render_grid_header( grid, repo_grid )))
        __M_writer(u'</td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr>\n            <td width="100%" id="grid-message" valign="top">')
        # SOURCE LINE 42
        __M_writer(unicode(render_message( message, status )))
        __M_writer(u'</td>\n            <td></td>\n            <td></td>\n        </tr>\n    </table>\n    ')
        # SOURCE LINE 47
        __M_writer(unicode(render_grid_table( grid, show_item_checkboxes )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_header(context,grid,repo_grid,render_title=True):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7057910')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7057750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7057c90')._populate(_import_ns, [u'*'])
        grid_title = _import_ns.get('grid_title', context.get('grid_title', UNDEFINED))
        render_grid_filters = _import_ns.get('render_grid_filters', context.get('render_grid_filters', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\n    <div class="grid-header">\n')
        # SOURCE LINE 10
        if render_title:
            # SOURCE LINE 11
            __M_writer(u'            ')
            __M_writer(unicode(grid_title()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 13
        if grid.global_actions:
            # SOURCE LINE 14
            __M_writer(u'            <ul class="manage-table-actions">\n')
            # SOURCE LINE 15
            if len( grid.global_actions ) < 4:
                # SOURCE LINE 16
                for action in grid.global_actions:
                    # SOURCE LINE 17
                    __M_writer(u'                        <li><a class="action-button" href="')
                    __M_writer(unicode(h.url_for( **action.url_args )))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(unicode(action.label )))
                    __M_writer(u'</a></li>\n')
                    pass
                # SOURCE LINE 19
            else:
                # SOURCE LINE 20
                __M_writer(u'                    <li><a class="action-button" id="action-8675309-popup" class="menubutton">Actions</a></li>\n                    <div popupmenu="action-8675309-popup">\n')
                # SOURCE LINE 22
                for action in grid.global_actions:
                    # SOURCE LINE 23
                    __M_writer(u'                            <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( **action.url_args )))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(unicode(action.label )))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 25
                __M_writer(u'                    </div>\n')
                pass
            # SOURCE LINE 27
            __M_writer(u'            </ul>\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'        ')
        __M_writer(unicode(render_grid_filters( repo_grid, render_advanced_search=False )))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7057910')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7057750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7057c90')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\n    <div style="overflow: auto; height: 100%">\n        <div class="page-container" style="padding: 10px;">\n            ')
        # SOURCE LINE 61
        __M_writer(unicode(self.grid_body( grid )))
        __M_writer(u'\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_body(context,grid):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7057910')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7057750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7057c90')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n    ')
        # SOURCE LINE 51

        from tool_shed.grids.repository_grids import RepositoryGrid
        repo_grid = RepositoryGrid()
            
        
        # SOURCE LINE 54
        __M_writer(u'\n    ')
        # SOURCE LINE 55
        __M_writer(unicode(self.make_grid( grid, repo_grid )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


