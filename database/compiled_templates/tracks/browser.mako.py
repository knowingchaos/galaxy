# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383207417.2837739
_template_filename='templates/webapps/galaxy/tracks/browser.mako'
_template_uri='tracks/browser.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'init', 'javascripts', 'center_panel', 'right_panel']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x8a2cf90', context._clean_inheritance_tokens(), templateuri=u'/visualization/trackster_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x8a2cf90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8a2cf90')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 163
        __M_writer(u'\n\n')
        # SOURCE LINE 174
        __M_writer(u'\n\n')
        # SOURCE LINE 191
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8a2cf90')._populate(_import_ns, [u'*'])
        render_trackster_css_files = _import_ns.get('render_trackster_css_files', context.get('render_trackster_css_files', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n    ')
        # SOURCE LINE 14
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(unicode(render_trackster_css_files()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8a2cf90')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5

        self.has_left_panel=False
        self.has_right_panel=True
        self.active_view="visualization"
        self.message_box_visible=False
        
        
        # SOURCE LINE 10
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8a2cf90')._populate(_import_ns, [u'*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        render_trackster_js_vars = _import_ns.get('render_trackster_js_vars', context.get('render_trackster_js_vars', UNDEFINED))
        viewport_config = _import_ns.get('viewport_config', context.get('viewport_config', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        render_trackster_js_files = _import_ns.get('render_trackster_js_files', context.get('render_trackster_js_files', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        add_dataset = _import_ns.get('add_dataset', context.get('add_dataset', UNDEFINED))
        default_dbkey = _import_ns.get('default_dbkey', context.get('default_dbkey', UNDEFINED))
        config = _import_ns.get('config', context.get('config', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\n')
        # SOURCE LINE 19
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n<!--[if lt IE 9]>\n  <script type=\'text/javascript\' src="')
        # SOURCE LINE 22
        __M_writer(unicode(h.url_for('/static/scripts/libs/IE/excanvas.js')))
        __M_writer(u'"></script>\n<![endif]-->\n\n')
        # SOURCE LINE 25
        __M_writer(unicode(render_trackster_js_files()))
        __M_writer(u'\n\n<script type="text/javascript">\n\n    require.config({ \n        baseUrl: "')
        # SOURCE LINE 30
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n        shim: {\n            "libs/underscore": { exports: "_" },\n            "libs/backbone/backbone": { exports: "Backbone" },\n            "libs/backbone/backbone-relational": ["libs/backbone/backbone"]\n        }\n    });\n    require( ["base", "viz/visualization", "viz/trackster_ui", "viz/trackster/tracks"], \n             function( base, visualization, trackster_ui, tracks ) {\n\n    ')
        # SOURCE LINE 40
        __M_writer(unicode(render_trackster_js_vars()))
        __M_writer(u'\n\n    // FIXME: deliberate global required for now due to requireJS integration.\n    view = null;\n\n    var browser_router,\n        ui = new (trackster_ui.TracksterUI)( "')
        # SOURCE LINE 46
        __M_writer(unicode(h.url_for('/')))
        __M_writer(u'" );\n\n    /**\n     * Set up router.\n     */\n    var set_up_router = function(options) {\n        browser_router = new visualization.TrackBrowserRouter(options);\n        Backbone.history.start();   \n    };\n    \n\n    var browser_router;\n    $(function() {\n\n        ui.createButtonMenu();\n\n        // Attach the button menu to the panel header and float it left\n        ui.buttonMenu.$el.attr("style", "float: right");\n        $("#center .unified-panel-header-inner").append(ui.buttonMenu.$el);\n        \n        // Hide bookmarks by default right now.\n        force_right_panel("hide"); \n        \n        // Resize view when showing/hiding right panel (bookmarks for now).\n        $("#right-border").click(function() { view.resize_window(); });\n        \n')
        # SOURCE LINE 72
        if config:
            # SOURCE LINE 73
            __M_writer(u'            view = ui.create_visualization( {\n                                            container: $("#browser-container"), \n                                            name: "')
            # SOURCE LINE 75
            __M_writer(filters.html_escape(unicode(config.get('title') )))
            __M_writer(u'",\n                                            vis_id: "')
            # SOURCE LINE 76
            __M_writer(unicode(config.get('vis_id')))
            __M_writer(u'", \n                                            dbkey: "')
            # SOURCE LINE 77
            __M_writer(unicode(config.get('dbkey')))
            __M_writer(u'"\n                                         },\n                                         ')
            # SOURCE LINE 79
            __M_writer(unicode( h.to_json_string( config.get( 'viewport', dict() ) ) ))
            __M_writer(u',\n                                         ')
            # SOURCE LINE 80
            __M_writer(unicode( h.to_json_string( config['tracks'] ) ))
            __M_writer(u',\n                                         ')
            # SOURCE LINE 81
            __M_writer(unicode( h.to_json_string( config['bookmarks'] ) ))
            __M_writer(u',\n                                         true\n                                         );\n            init_editor();\n            set_up_router({view: view});\n')
            # SOURCE LINE 86
        else:
            # SOURCE LINE 87
            __M_writer(u'            var continue_fn = function() {\n                view = ui.create_visualization( {\n                    container: $("#browser-container"),\n                    name: $("#new-title").val(),\n                    dbkey: $("#new-dbkey").val()\n                }, ')
            # SOURCE LINE 92
            __M_writer(unicode( h.to_json_string( viewport_config ) ))
            __M_writer(u' );\n                view.editor = true;\n                init_editor();\n                set_up_router({view: view});\n                hide_modal();\n            };\n            $.ajax({\n                url: "')
            # SOURCE LINE 99
            __M_writer(unicode(h.url_for( controller='visualization', action='new_browser', default_dbkey=default_dbkey )))
            __M_writer(u'",\n                data: {},\n                error: function() { alert( "Couldn\'t create new browser" ) },\n                success: function(form_html) {\n                    show_modal("New Visualization", form_html, {\n                        "Cancel": function() { window.location = "')
            # SOURCE LINE 104
            __M_writer(unicode(h.url_for( controller='visualization', action='list' )))
            __M_writer(u'"; },\n                        "Create": function() { $(document).trigger("convert_to_values"); continue_fn(); }\n                    });\n                    $("#new-title").focus();\n                    $("select[name=\'dbkey\']").select2({ width: \'resolve\'});\n                    // To support the large number of options for dbkey, enable scrolling in overlay.\n                    $("#overlay").css("overflow", "auto");\n                }\n            });\n')
            pass
        # SOURCE LINE 114
        __M_writer(u'        \n        /**\n         * Initialization for editor-specific functions.\n         */\n        function init_editor() {\n            $("#title").text(view.name + " (" + view.dbkey + ")");\n           \n            if (!is_in_galaxy_frame())\n            window.onbeforeunload = function() {\n                if (view.has_changes) {\n                    return "There are unsaved changes to your visualization which will be lost.";\n                }\n            };\n                        \n')
        # SOURCE LINE 128
        if add_dataset is not None:
            # SOURCE LINE 129
            __M_writer(u'                $.ajax({\n                    url: add_track_async_url + "/')
            # SOURCE LINE 130
            __M_writer(unicode(add_dataset))
            __M_writer(u'",\n                    data: { hda_ldda: \'hda\', data_type: \'track_config\' },\n                    dataType: "json",\n                    success: function(track_data) { view.add_drawable( trackster_ui.object_from_template(track_data, view, view) ) }\n                });\n                \n')
            pass
        # SOURCE LINE 137
        __M_writer(u'            \n            //\n            // Initialize icons.\n            //\n            \n            $("#add-bookmark-button").click(function() {\n                // Add new bookmark.\n                var position = view.chrom + ":" + view.low + "-" + view.high,\n                    annotation = "Bookmark description";\n                return ui.add_bookmark(position, annotation, true);\n            });\n\n            // make_popupmenu( $("#bookmarks-more-button"), {\n            //     "Add from BED dataset": function() {\n            //         add_bookmarks();    \n            //     }\n            // });\n\n            ui.init_keyboard_nav(view);\n        };\n        \n    });\n\n    });\n\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8a2cf90')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 165
        __M_writer(u'\n<div class="unified-panel-header" unselectable="on">\n    <div class="unified-panel-header-inner">\n        <div style="float:left;" id="title"></div>\n    </div>\n    <div style="clear: both"></div>\n</div>\n<div id="browser-container" class="unified-panel-body"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8a2cf90')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 176
        __M_writer(u'\n\n<div class="unified-panel-header" unselectable="on">\n    <div class="unified-panel-header-inner">\n        <div style="float: right">\n            <a id="add-bookmark-button" class=\'icon-button menu-button plus-button\' href="javascript:void(0);" title="Add bookmark"></a>\n')
        # SOURCE LINE 183
        __M_writer(u'        </div>\n        Bookmarks\n    </div>\n</div>\n<div class="unified-panel-body" style="overflow: auto;">\n    <div id="bookmarks-container"></div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


