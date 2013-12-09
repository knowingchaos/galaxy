# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383788639.943871
_template_filename=u'templates/webapps/galaxy/root/tool_menu.mako'
_template_uri=u'/root/tool_menu.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['tool_menu_javascripts', 'render_tool_menu']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer(u'\n\n')
        # SOURCE LINE 92
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tool_menu_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n    ')
        # SOURCE LINE 3
        __M_writer(unicode(h.templates( "tool_link", "panel_section", "tool_search" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4
        __M_writer(unicode(h.js( "libs/require", "galaxy.autocom_tagging" )))
        __M_writer(u'\n    \n    <script type="text/javascript">\n        require.config({ \n                baseUrl: "')
        # SOURCE LINE 8
        __M_writer(unicode(h.url_for('/static/scripts')))
        __M_writer(u'",\n                shim: {\n                    "libs/underscore": { exports: "_" }\n                }\n        });\n\n        require(["mvc/tools"], function(tools) {\n\n            // Init. on document load.\n            $(function() {\n                // Create tool search, tool panel, and tool panel view.\n                var tool_search = new tools.ToolSearch({ \n                        spinner_url: "')
        # SOURCE LINE 20
        __M_writer(unicode(h.url_for('/static/images/loading_small_white_bg.gif')))
        __M_writer(u'",\n                        search_url: "')
        # SOURCE LINE 21
        __M_writer(unicode(h.url_for( controller='root', action='tool_search' )))
        __M_writer(u'",\n                        hidden: false \n                    }),\n                    tool_panel = new tools.ToolPanel({ tool_search: tool_search }),\n                    tool_panel_view = new tools.ToolPanelView({ collection: tool_panel });\n\n                // Add tool panel to Galaxy object.\n                Galaxy.toolPanel = tool_panel;\n\n')
        # SOURCE LINE 31
        if trans.user or not trans.app.config.require_login:
            # SOURCE LINE 32
            __M_writer(u'                    tool_panel.reset( tool_panel.parse( ')
            __M_writer(unicode(h.to_json_string( trans.app.toolbox.to_dict( trans ) )))
            __M_writer(u' ) );\n')
            pass
        # SOURCE LINE 34
        __M_writer(u'\n                // If there are tools, render panel and display everything.\n                if (tool_panel.length > 1) { // > 1 because tool_search counts as a model\n                    tool_panel_view.render();\n                    $(\'.toolMenu\').show();\n                }\n                $(\'.toolMenuContainer\').prepend(tool_panel_view.$el);\n                \n                // Minsize init hint.\n                $( "a[minsizehint]" ).click( function() {\n                    if ( parent.handle_minwidth_hint ) {\n                        parent.handle_minwidth_hint( $(this).attr( "minsizehint" ) );\n                    }\n                });\n            });\n\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_menu(context):
    context.caller_stack._push_frame()
    try:
        t = context.get('t', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(u'\n    <div class="toolMenuContainer">\n        \n        <div class="toolMenu" style="display: none">\n')
        # SOURCE LINE 60
        __M_writer(u'            <div id="search-no-results" style="display: none; padding-top: 5px">\n                <em><strong>Search did not match any tools.</strong></em>\n            </div>\n            \n')
        # SOURCE LINE 67
        __M_writer(u'            \n')
        # SOURCE LINE 68
        if t.user:
            # SOURCE LINE 69
            __M_writer(u'\t\t\t\t<div class="toolSectionPad"></div>\n\t\t\t\t<div class="toolSectionPad"></div>\n')
            pass
        # SOURCE LINE 89
        __M_writer(u'            \n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


