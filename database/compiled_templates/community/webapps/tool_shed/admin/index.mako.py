# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383494623.2711909
_template_filename='templates/webapps/tool_shed/admin/index.mako'
_template_uri='/webapps/tool_shed/admin/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'init', 'javascripts', 'center_panel', 'left_panel']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f82a444b350', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f82a444b350')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/tool_shed/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a444b350')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 111
        __M_writer(u'\n\n')
        # SOURCE LINE 118
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a444b350')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'    ')
        __M_writer(unicode(h.css( "base", "autocomplete_tagging", "tool_menu" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u'    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n\n    <style type="text/css">\n        body { margin: 0; padding: 0; overflow: hidden; }\n        #left {\n            background: #C1C9E5 url(')
        # SOURCE LINE 14
        __M_writer(unicode(h.url_for('/static/style/menu_bg.png')))
        __M_writer(u') top repeat-x;\n        }\n        .unified-panel-body {\n            overflow: auto;\n        }\n        .toolMenu {\n            margin-left: 10px;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a444b350')._populate(_import_ns, [u'render_msg'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n    ')
        # SOURCE LINE 30

        self.has_left_panel=True
        self.has_right_panel=False
        self.active_view="tools"
            
        
        # SOURCE LINE 34
        __M_writer(u'\n')
        # SOURCE LINE 35
        if trans.app.config.require_login and not trans.user:
            # SOURCE LINE 36
            __M_writer(u'        <script type="text/javascript">\n            if ( window != top ) {\n                top.location.href = location.href;\n            }\n        </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a444b350')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n    ')
        # SOURCE LINE 26
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a444b350')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 113
        __M_writer(u'\n    ')
        # SOURCE LINE 114

        center_url = h.url_for(controller='admin', action='center' )
            
        
        # SOURCE LINE 116
        __M_writer(u'\n    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 100%; height: 100%;" src="')
        # SOURCE LINE 117
        __M_writer(unicode(center_url))
        __M_writer(u'"> </iframe>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a444b350')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n    ')
        # SOURCE LINE 45
        can_review_repositories = trans.app.security_agent.user_can_review_repositories( trans.user ) 
        
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>Administration</div>\n    </div>\n    <div class="unified-panel-body">\n        <div class="toolMenu">\n            <div class="toolSectionList">\n                <div class="toolSectionTitle">\n                    Repositories\n                </div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
        # SOURCE LINE 58
        __M_writer(unicode(h.url_for( controller='repository', action='browse_categories' )))
        __M_writer(u'">Browse by category</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
        # SOURCE LINE 61
        __M_writer(unicode(h.url_for( controller='admin', action='browse_repositories' )))
        __M_writer(u'">Browse all repositories</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
        # SOURCE LINE 64
        __M_writer(unicode(h.url_for( controller='admin', action='reset_metadata_on_selected_repositories_in_tool_shed' )))
        __M_writer(u'">Reset selected metadata</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
        # SOURCE LINE 67
        __M_writer(unicode(h.url_for( controller='admin', action='browse_repository_metadata' )))
        __M_writer(u'">Browse metadata</a>\n                        </div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">\n                    Categories\n                </div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
        # SOURCE LINE 78
        __M_writer(unicode(h.url_for( controller='admin', action='manage_categories' )))
        __M_writer(u'">Manage categories</a>\n                        </div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">\n                    Security\n                </div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
        # SOURCE LINE 89
        __M_writer(unicode(h.url_for( controller='admin', action='users' )))
        __M_writer(u'">Manage users</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
        # SOURCE LINE 92
        __M_writer(unicode(h.url_for( controller='admin', action='groups' )))
        __M_writer(u'">Manage groups</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
        # SOURCE LINE 95
        __M_writer(unicode(h.url_for( controller='admin', action='roles' )))
        __M_writer(u'">Manage roles</a>\n                        </div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">\n                    Statistics\n                </div>\n                <div class="toolSectionBody">\n                    <div class="toolTitle">\n                        <a target="galaxy_main" href="')
        # SOURCE LINE 105
        __M_writer(unicode(h.url_for( controller='admin', action='regenerate_statistics' )))
        __M_writer(u'">View shed statistics</a>\n                    </div>\n                </div>\n            </div>\n        </div>    \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


