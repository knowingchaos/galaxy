# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384081429.228915
_template_filename=u'templates/base/base_panels.mako'
_template_uri=u'/base/base_panels.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['overlay', 'late_javascripts', 'stylesheets', 'init', 'masthead', 'javascripts']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        app = context.get('app', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML>\n\n\n')
        # SOURCE LINE 4

        self.has_left_panel = hasattr( self, 'left_panel' )
        self.has_right_panel = hasattr( self, 'right_panel' )
        self.message_box_visible = app.config.message_box_visible
        self.overlay_visible=False
        self.active_view=None
        self.body_class=""
        self.require_javascript=False
        
        
        # SOURCE LINE 12
        __M_writer(u'\n    \n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 142
        __M_writer(u'\n\n')
        # SOURCE LINE 255
        __M_writer(u'\n\n')
        # SOURCE LINE 260
        __M_writer(u'\n\n')
        # SOURCE LINE 292
        __M_writer(u'\n\n')
        # SOURCE LINE 295
        __M_writer(u'<html>\n    <!--base_panels.mako-->\n    ')
        # SOURCE LINE 297
        __M_writer(unicode(self.init()))
        __M_writer(u'    \n    <head>\n')
        # SOURCE LINE 299
        if app.config.brand:
            # SOURCE LINE 300
            __M_writer(u'            <title>')
            __M_writer(unicode(self.title()))
            __M_writer(u' / ')
            __M_writer(unicode(app.config.brand))
            __M_writer(u'</title>\n')
            # SOURCE LINE 301
        else:
            # SOURCE LINE 302
            __M_writer(u'            <title>')
            __M_writer(unicode(self.title()))
            __M_writer(u'</title>\n')
            pass
        # SOURCE LINE 304
        __M_writer(u'        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        # SOURCE LINE 306
        __M_writer(u'        <meta name = "viewport" content = "maximum-scale=1.0">\n')
        # SOURCE LINE 308
        __M_writer(u'        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n        ')
        # SOURCE LINE 309
        __M_writer(unicode(self.stylesheets()))
        __M_writer(u'\n        ')
        # SOURCE LINE 310
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n    </head>\n    \n    <body scroll="no" class="full-content ')
        # SOURCE LINE 313
        __M_writer(unicode(self.body_class))
        __M_writer(u'">\n')
        # SOURCE LINE 314
        if self.require_javascript:
            # SOURCE LINE 315
            __M_writer(u'            <noscript>\n                <div class="overlay overlay-background">\n                    <div class="modal dialog-box" border="0">\n                        <div class="modal-header"><h3 class="title">Javascript Required</h3></div>\n                        <div class="modal-body">The Galaxy analysis interface requires a browser with Javascript enabled. <br> Please enable Javascript and refresh this page</div>\n                    </div>\n                </div>\n            </noscript>\n')
            pass
        # SOURCE LINE 324
        __M_writer(u'        <div id="everything" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">\n')
        # SOURCE LINE 326
        if trans.user:
            # SOURCE LINE 327
            __M_writer(u'            <div id="background"></div>\n')
            # SOURCE LINE 329
            __M_writer(u'            <div id="masthead" class="navbar navbar-fixed-top">\n                <div class="masthead-inner navbar-inner">\n                    ')
            # SOURCE LINE 331
            __M_writer(unicode(self.masthead()))
            __M_writer(u'\n                </div>\n            </div>\n            <div id="messagebox" class="panel-')
            # SOURCE LINE 334
            __M_writer(unicode(app.config.message_box_class))
            __M_writer(u'-message">\n')
            # SOURCE LINE 335
            if self.message_box_visible and app.config.message_box_content:
                # SOURCE LINE 336
                __M_writer(u'                        ')
                __M_writer(unicode(app.config.message_box_content))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 338
            __M_writer(u'            </div>\n            ')
            # SOURCE LINE 339
            __M_writer(unicode(self.overlay(visible=self.overlay_visible)))
            __M_writer(u'\n')
            # SOURCE LINE 340
            if self.has_left_panel:
                # SOURCE LINE 341
                __M_writer(u'\t\t\t\t\t<div id="left">\n\t\t\t\t\t\t')
                # SOURCE LINE 342
                __M_writer(unicode(self.left_panel()))
                __M_writer(u'\n\t\t\t\t\t\t<div class="unified-panel-footer">\n\t\t\t\t\t\t\t<div class="panel-collapse"></span></div>\n\t\t\t\t\t\t\t<div class="drag"></div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n')
                pass
            pass
        # SOURCE LINE 350
        __M_writer(u'            <div id="center">\n                ')
        # SOURCE LINE 351
        __M_writer(unicode(self.center_panel()))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 353
        if trans.user:
            # SOURCE LINE 354
            if self.has_right_panel:
                # SOURCE LINE 355
                __M_writer(u'\t\t\t\t\t<div id="right">\n\t\t\t\t\t\t')
                # SOURCE LINE 356
                __M_writer(unicode(self.right_panel()))
                __M_writer(u'\n\t\t\t\t\t\t<div class="unified-panel-footer">\n\t\t\t\t\t\t\t<div class="panel-collapse right"></span></div>\n\t\t\t\t\t\t\t<div class="drag"></div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n')
                pass
            pass
        # SOURCE LINE 364
        __M_writer(u'        </div>\n')
        # SOURCE LINE 366
        __M_writer(u'    </body>\n')
        # SOURCE LINE 369
        __M_writer(u'    ')
        __M_writer(unicode(self.late_javascripts()))
        __M_writer(u'\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context,title='',content='',visible=False):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 262
        __M_writer(u'\n    ')
        # SOURCE LINE 263
        __M_writer(u'\n    ')
        # SOURCE LINE 264
        __M_writer(u'\n\n    ')
        # SOURCE LINE 266

        if visible:
            display = "style='display: block;'"
            overlay_class = "in"
        else:
            display = "style='display: none;'"
            overlay_class = ""
        
        
        # SOURCE LINE 273
        __M_writer(u'\n\n    <div id="overlay" ')
        # SOURCE LINE 275
        __M_writer(unicode(display))
        __M_writer(u'>\n\n        <div id="overlay-background" class="modal-backdrop fade ')
        # SOURCE LINE 277
        __M_writer(unicode(overlay_class))
        __M_writer(u'"></div>\n\n        <div id="dialog-box" class="modal dialog-box" border="0" ')
        # SOURCE LINE 279
        __M_writer(unicode(display))
        __M_writer(u'>\n                <div class="modal-header">\n                    <span><h3 class=\'title\'>')
        # SOURCE LINE 281
        __M_writer(unicode(title))
        __M_writer(u'</h3></span>\n                </div>\n                <div class="modal-body">')
        # SOURCE LINE 283
        __M_writer(unicode(content))
        __M_writer(u'</div>\n                <div class="modal-footer">\n                    <div class="buttons" style="float: right;"></div>\n                    <div class="extra_buttons" style=""></div>\n                    <div style="clear: both;"></div>\n                </div>\n        </div>\n    \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 145
        __M_writer(u'\n')
        # SOURCE LINE 148
        __M_writer(u'    ')
        __M_writer(unicode(h.js( 'libs/jquery/jquery.event.drag', 'libs/jquery/jquery.event.hover', 'libs/jquery/jquery.form', 'libs/jquery/jquery.rating', 'galaxy.panels' )))
        __M_writer(u'\n    <script type="text/javascript">\n        \n    ensure_dd_helper();\n        \n')
        # SOURCE LINE 153
        if self.has_left_panel:
            # SOURCE LINE 154
            __M_writer(u'            var lp = new Panel( { panel: $("#left"), center: $("#center"), drag: $("#left > .unified-panel-footer > .drag" ), toggle: $("#left > .unified-panel-footer > .panel-collapse" ) } );\n            force_left_panel = function( x ) { lp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 157
        __M_writer(u'        \n')
        # SOURCE LINE 158
        if self.has_right_panel:
            # SOURCE LINE 159
            __M_writer(u'            var rp = new Panel( { panel: $("#right"), center: $("#center"), drag: $("#right > .unified-panel-footer > .drag" ), toggle: $("#right > .unified-panel-footer > .panel-collapse" ), right: true } );\n            window.handle_minwidth_hint = function( x ) { rp.handle_minwidth_hint( x ) };\n            force_right_panel = function( x ) { rp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 163
        __M_writer(u'    \n    </script>\n')
        # SOURCE LINE 166
        __M_writer(u'    <![if !IE]>\n    <script type="text/javascript">\n        var upload_form_error = function( msg ) {\n            if ( ! $("iframe#galaxy_main").contents().find("body").find("div[class=\'errormessage\']").size() ) {\n                $("iframe#galaxy_main").contents().find("body").prepend( \'<div class="errormessage" name="upload_error">\' + msg + \'</div><p/>\' );\n            } else {\n                $("iframe#galaxy_main").contents().find("body").find("div[class=\'errormessage\']").text( msg );\n            }\n        }\n        var uploads_in_progress = 0;\n        jQuery( function() {\n            $("iframe#galaxy_main").load( function() {\n                $(this).contents().find("form").each( function() { \n                    if ( $(this).find("input[galaxy-ajax-upload]").length > 0 ){\n                        $(this).submit( function() {\n                            // Only bother using a hidden iframe if there\'s a file (e.g. big data) upload\n                            var file_upload = false;\n                            $(this).find("input[galaxy-ajax-upload]").each( function() {\n                                if ( $(this).val() != \'\' ) {\n                                    file_upload = true;\n                                }\n                            });\n                            if ( ! file_upload ) {\n                                return true;\n                            }\n                            // Make a synchronous request to create the datasets first\n                            var async_datasets;\n                            var upload_error = false;\n                            $.ajax( {\n                                async:      false,\n                                type:       "POST",\n                                url:        "')
        # SOURCE LINE 197
        __M_writer(unicode(h.url_for(controller='/tool_runner', action='upload_async_create')))
        __M_writer(u'",\n                                data:       $(this).formSerialize(),\n                                dataType:   "json",\n                                success:    function(array_obj, status) {\n                                                if (array_obj.length > 0) {\n                                                    if (array_obj[0] == \'error\') {\n                                                        upload_error = true;\n                                                        upload_form_error(array_obj[1]);\n                                                    } else {\n                                                        async_datasets = array_obj.join();\n                                                    }\n                                                } else {\n                                                    // ( gvk 1/22/10 ) FIXME: this block is never entered, so there may be a bug somewhere\n                                                    // I\'ve done some debugging like checking to see if array_obj is undefined, but have not\n                                                    // tracked down the behavior that will result in this block being entered.  I believe the\n                                                    // intent was to have this block entered if the upload button is clicked on the upload\n                                                    // form but no file was selected.\n                                                    upload_error = true;\n                                                    upload_form_error( \'No data was entered in the upload form.  You may choose to upload a file, paste some data directly in the data box, or enter URL(s) to fetch data.\' );\n                                                }\n                                            }\n                            } );\n                            if (upload_error == true) {\n                                return false;\n                            } else {\n                                $(this).find("input[name=async_datasets]").val( async_datasets );\n                                $(this).append("<input type=\'hidden\' name=\'ajax_upload\' value=\'true\'>");\n                            }\n                            // iframe submit is required for nginx (otherwise the encoding is wrong)\n                            $(this).ajaxSubmit( { iframe:   true,\n                                                  complete: function (xhr, stat) {\n                                                                uploads_in_progress--;\n                                                                if (uploads_in_progress == 0) {\n                                                                    window.onbeforeunload = null;\n                                                                }\n                                                            }\n                                                 } );\n                            uploads_in_progress++;\n                            window.onbeforeunload = function() { return "Navigating away from the Galaxy analysis interface will interrupt the file upload(s) currently in progress.  Do you really want to do this?"; }\n                            if ( $(this).find("input[name=\'folder_id\']").val() != undefined ) {\n                                var library_id = $(this).find("input[name=\'library_id\']").val();\n                                var show_deleted = $(this).find("input[name=\'show_deleted\']").val();\n                                if ( location.pathname.indexOf( \'admin\' ) != -1 ) {\n                                    $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 240
        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library' )))
        __M_writer(u'?cntrller=library_admin&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);\n                                } else {\n                                    $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 242
        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library' )))
        __M_writer(u'?cntrller=library&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);\n                                }\n                            } else {\n                                $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 245
        __M_writer(unicode(h.url_for(controller='tool_runner', action='upload_async_message')))
        __M_writer(u'");\n                            }\n                            return false;\n                        });\n                    }\n                });\n            });\n        });\n    </script>\n    <![endif]>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n    ')
        # SOURCE LINE 20
        __M_writer(unicode(h.css('base','jquery.rating')))
        __M_writer(u'\n    <style type="text/css">\n    #center {\n')
        # SOURCE LINE 23
        if not self.has_left_panel:
            # SOURCE LINE 24
            __M_writer(u'            left: 0 !important;\n')
            pass
        # SOURCE LINE 26
        if not self.has_right_panel:
            # SOURCE LINE 27
            __M_writer(u'            right: 0 !important;\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'    }\n')
        # SOURCE LINE 30
        if self.message_box_visible:
            # SOURCE LINE 31
            __M_writer(u'        #left, #left-border, #center, #right-border, #right\n        {\n            top: 64px;\n        }\n')
            pass
        # SOURCE LINE 36
        __M_writer(u'    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 258
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        if app.config.sentry_dsn:
            # SOURCE LINE 44
            __M_writer(u'        ')
            __M_writer(unicode(h.js( "libs/tracekit", "libs/raven" )))
            __M_writer(u"\n        <script>\n            Raven.config('")
            # SOURCE LINE 46
            __M_writer(unicode(app.config.sentry_dsn_public))
            __M_writer(u"').install();\n")
            # SOURCE LINE 47
            if trans.user:
                # SOURCE LINE 48
                __M_writer(u'                Raven.setUser( { email: "')
                __M_writer(unicode(trans.user.email))
                __M_writer(u'" } );\n')
                pass
            # SOURCE LINE 50
            __M_writer(u'        </script>\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'\n    ')
        # SOURCE LINE 53
        __M_writer(unicode(h.js(
        'libs/jquery/jquery',
        'libs/jquery/jquery.migrate',
        'libs/json2',
        'libs/jquery/select2',
        'libs/bootstrap',
        'libs/underscore',
        'libs/backbone/backbone',
        'libs/backbone/backbone-relational',
        'libs/handlebars.runtime',
        'galaxy.base',
        'libs/require'
    )))
        # SOURCE LINE 65
        __M_writer(u'\n\n    ')
        # SOURCE LINE 67
        __M_writer(unicode(h.templates(
        "template-popupmenu-menu"
    )))
        # SOURCE LINE 69
        __M_writer(u'\n\n    ')
        # SOURCE LINE 71
        __M_writer(unicode(h.js(
        "mvc/ui"
    )))
        # SOURCE LINE 73
        __M_writer(u'\n\n    <script type="text/javascript">\n')
        # SOURCE LINE 77
        __M_writer(u'        var galaxy_config = {\n            url: {\n                styles : "')
        # SOURCE LINE 79
        __M_writer(unicode(h.url_for('/static/style')))
        __M_writer(u'"\n            }\n        };\n\n')
        # SOURCE LINE 84
        __M_writer(u'        function is_in_galaxy_frame()\n        {\n            var iframes = parent.document.getElementsByTagName("iframe");\n            for (var i=0, len=iframes.length; i < len; ++i)\n                if (document == iframes[i].contentDocument || self == iframes[i].contentWindow)\n                    return $(iframes[i]).hasClass(\'f-iframe\');\n            return false;\n        };\n\n')
        # SOURCE LINE 94
        __M_writer(u'        function load_css (url)\n        {\n')
        # SOURCE LINE 97
        __M_writer(u'            if (!$(\'link[href="\' + url + \'"]\').length)\n                $(\'<link href="\' + url + \'" rel="stylesheet">\').appendTo(\'head\');\n        };\n\n')
        # SOURCE LINE 102
        __M_writer(u"        if (is_in_galaxy_frame())\n            load_css(galaxy_config.url.styles + '/galaxy.frame.masthead.css');\n        \n        // console protection\n        window.console = window.console || {\n            log     : function(){},\n            debug   : function(){},\n            info    : function(){},\n            warn    : function(){},\n            error   : function(){},\n            assert  : function(){}\n        };\n\n        // Set up needed paths.\n        var galaxy_paths = new GalaxyPaths({\n            root_path: '")
        # SOURCE LINE 117
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u"',\n            image_path: '")
        # SOURCE LINE 118
        __M_writer(unicode(h.url_for( "/static/images" )))
        __M_writer(u"',\n            \n            tool_url: '")
        # SOURCE LINE 120
        __M_writer(unicode(h.url_for( controller="/api/tools" )))
        __M_writer(u"',\n            history_url: '")
        # SOURCE LINE 121
        __M_writer(unicode(h.url_for( controller="/api/histories" )))
        __M_writer(u"',\n            \n            datasets_url: '")
        # SOURCE LINE 123
        __M_writer(unicode(h.url_for( controller="/api/datasets" )))
        __M_writer(u"',\n            sweepster_url: '")
        # SOURCE LINE 124
        __M_writer(unicode(h.url_for( controller="/visualization", action="sweepster" )))
        __M_writer(u"',\n            visualization_url: '")
        # SOURCE LINE 125
        __M_writer(unicode(h.url_for( controller="/visualization", action="save" )))
        __M_writer(u"',\n        });\n\n")
        # SOURCE LINE 129
        __M_writer(u'        require.config({\n            baseUrl: "')
        # SOURCE LINE 130
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n            shim: {\n                "libs/underscore": { exports: "_" },\n                "libs/backbone/backbone": { exports: "Backbone" },\n                "libs/backbone/backbone-relational": ["libs/backbone/backbone"]\n            }\n        });\n        \n')
        # SOURCE LINE 139
        __M_writer(u"        var frame_manager = null;\n        require(['galaxy.frame'], function(frame) { this.frame_manager = new frame.GalaxyFrameManager(galaxy_config); });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


