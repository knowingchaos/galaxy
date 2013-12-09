<!DOCTYPE HTML>


<%
    self.has_left_panel = hasattr( self, 'left_panel' )
    self.has_right_panel = hasattr( self, 'right_panel' )
    self.message_box_visible = app.config.message_box_visible
    self.overlay_visible=False
    self.active_view=None
    self.body_class=""
    self.require_javascript=False
%>
    
<%def name="init()">
    ## Override
</%def>

## Default stylesheets
<%def name="stylesheets()">
    ${h.css('base','jquery.rating')}
    <style type="text/css">
    #center {
        %if not self.has_left_panel:
            left: 0 !important;
        %endif
        %if not self.has_right_panel:
            right: 0 !important;
        %endif
    }
    %if self.message_box_visible:
        #left, #left-border, #center, #right-border, #right
        {
            top: 64px;
        }
    %endif
    </style>
</%def>

## Default javascripts
<%def name="javascripts()">

    ## Send errors to Sntry server if configured
    %if app.config.sentry_dsn:
        ${h.js( "libs/tracekit", "libs/raven" )}
        <script>
            Raven.config('${app.config.sentry_dsn_public}').install();
            %if trans.user:
                Raven.setUser( { email: "${trans.user.email}" } );
            %endif
        </script>
    %endif

    ${h.js(
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
    )}

    ${h.templates(
        "template-popupmenu-menu"
    )}

    ${h.js(
        "mvc/ui"
    )}

    <script type="text/javascript">
        ## path to style sheets
        var galaxy_config = {
            url: {
                styles : "${h.url_for('/static/style')}"
            }
        };

        ## check if its in a galaxy iframe
        function is_in_galaxy_frame()
        {
            var iframes = parent.document.getElementsByTagName("iframe");
            for (var i=0, len=iframes.length; i < len; ++i)
                if (document == iframes[i].contentDocument || self == iframes[i].contentWindow)
                    return $(iframes[i]).hasClass('f-iframe');
            return false;
        };

        ## load css
        function load_css (url)
        {
            ## check if css is already available
            if (!$('link[href="' + url + '"]').length)
                $('<link href="' + url + '" rel="stylesheet">').appendTo('head');
        };

        ## load additional style sheet
        if (is_in_galaxy_frame())
            load_css(galaxy_config.url.styles + '/galaxy.frame.masthead.css');
        
        // console protection
        window.console = window.console || {
            log     : function(){},
            debug   : function(){},
            info    : function(){},
            warn    : function(){},
            error   : function(){},
            assert  : function(){}
        };

        // Set up needed paths.
        var galaxy_paths = new GalaxyPaths({
            root_path: '${h.url_for( "/" )}',
            image_path: '${h.url_for( "/static/images" )}',
            
            tool_url: '${h.url_for( controller="/api/tools" )}',
            history_url: '${h.url_for( controller="/api/histories" )}',
            
            datasets_url: '${h.url_for( controller="/api/datasets" )}',
            sweepster_url: '${h.url_for( controller="/visualization", action="sweepster" )}',
            visualization_url: '${h.url_for( controller="/visualization", action="save" )}',
        });

        ## configure require
        require.config({
            baseUrl: "${h.url_for('/static/scripts') }",
            shim: {
                "libs/underscore": { exports: "_" },
                "libs/backbone/backbone": { exports: "Backbone" },
                "libs/backbone/backbone-relational": ["libs/backbone/backbone"]
            }
        });
        
        ## frame manager
        var frame_manager = null;
        require(['galaxy.frame'], function(frame) { this.frame_manager = new frame.GalaxyFrameManager(galaxy_config); });
    </script>
</%def>

## Default late-load javascripts
<%def name="late_javascripts()">
    ## Scripts can be loaded later since they progressively add features to
    ## the panels, but do not change layout
    ${h.js( 'libs/jquery/jquery.event.drag', 'libs/jquery/jquery.event.hover', 'libs/jquery/jquery.form', 'libs/jquery/jquery.rating', 'galaxy.panels' )}
    <script type="text/javascript">
        
    ensure_dd_helper();
        
    %if self.has_left_panel:
            var lp = new Panel( { panel: $("#left"), center: $("#center"), drag: $("#left > .unified-panel-footer > .drag" ), toggle: $("#left > .unified-panel-footer > .panel-collapse" ) } );
            force_left_panel = function( x ) { lp.force_panel( x ) };
        %endif
        
    %if self.has_right_panel:
            var rp = new Panel( { panel: $("#right"), center: $("#center"), drag: $("#right > .unified-panel-footer > .drag" ), toggle: $("#right > .unified-panel-footer > .panel-collapse" ), right: true } );
            window.handle_minwidth_hint = function( x ) { rp.handle_minwidth_hint( x ) };
            force_right_panel = function( x ) { rp.force_panel( x ) };
        %endif
    
    </script>
    ## Handle AJAX (actually hidden iframe) upload tool
    <![if !IE]>
    <script type="text/javascript">
        var upload_form_error = function( msg ) {
            if ( ! $("iframe#galaxy_main").contents().find("body").find("div[class='errormessage']").size() ) {
                $("iframe#galaxy_main").contents().find("body").prepend( '<div class="errormessage" name="upload_error">' + msg + '</div><p/>' );
            } else {
                $("iframe#galaxy_main").contents().find("body").find("div[class='errormessage']").text( msg );
            }
        }
        var uploads_in_progress = 0;
        jQuery( function() {
            $("iframe#galaxy_main").load( function() {
                $(this).contents().find("form").each( function() { 
                    if ( $(this).find("input[galaxy-ajax-upload]").length > 0 ){
                        $(this).submit( function() {
                            // Only bother using a hidden iframe if there's a file (e.g. big data) upload
                            var file_upload = false;
                            $(this).find("input[galaxy-ajax-upload]").each( function() {
                                if ( $(this).val() != '' ) {
                                    file_upload = true;
                                }
                            });
                            if ( ! file_upload ) {
                                return true;
                            }
                            // Make a synchronous request to create the datasets first
                            var async_datasets;
                            var upload_error = false;
                            $.ajax( {
                                async:      false,
                                type:       "POST",
                                url:        "${h.url_for(controller='/tool_runner', action='upload_async_create')}",
                                data:       $(this).formSerialize(),
                                dataType:   "json",
                                success:    function(array_obj, status) {
                                                if (array_obj.length > 0) {
                                                    if (array_obj[0] == 'error') {
                                                        upload_error = true;
                                                        upload_form_error(array_obj[1]);
                                                    } else {
                                                        async_datasets = array_obj.join();
                                                    }
                                                } else {
                                                    // ( gvk 1/22/10 ) FIXME: this block is never entered, so there may be a bug somewhere
                                                    // I've done some debugging like checking to see if array_obj is undefined, but have not
                                                    // tracked down the behavior that will result in this block being entered.  I believe the
                                                    // intent was to have this block entered if the upload button is clicked on the upload
                                                    // form but no file was selected.
                                                    upload_error = true;
                                                    upload_form_error( 'No data was entered in the upload form.  You may choose to upload a file, paste some data directly in the data box, or enter URL(s) to fetch data.' );
                                                }
                                            }
                            } );
                            if (upload_error == true) {
                                return false;
                            } else {
                                $(this).find("input[name=async_datasets]").val( async_datasets );
                                $(this).append("<input type='hidden' name='ajax_upload' value='true'>");
                            }
                            // iframe submit is required for nginx (otherwise the encoding is wrong)
                            $(this).ajaxSubmit( { iframe:   true,
                                                  complete: function (xhr, stat) {
                                                                uploads_in_progress--;
                                                                if (uploads_in_progress == 0) {
                                                                    window.onbeforeunload = null;
                                                                }
                                                            }
                                                 } );
                            uploads_in_progress++;
                            window.onbeforeunload = function() { return "Navigating away from the Galaxy analysis interface will interrupt the file upload(s) currently in progress.  Do you really want to do this?"; }
                            if ( $(this).find("input[name='folder_id']").val() != undefined ) {
                                var library_id = $(this).find("input[name='library_id']").val();
                                var show_deleted = $(this).find("input[name='show_deleted']").val();
                                if ( location.pathname.indexOf( 'admin' ) != -1 ) {
                                    $("iframe#galaxy_main").attr("src","${h.url_for( controller='library_common', action='browse_library' )}?cntrller=library_admin&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);
                                } else {
                                    $("iframe#galaxy_main").attr("src","${h.url_for( controller='library_common', action='browse_library' )}?cntrller=library&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);
                                }
                            } else {
                                $("iframe#galaxy_main").attr("src","${h.url_for(controller='tool_runner', action='upload_async_message')}");
                            }
                            return false;
                        });
                    }
                });
            });
        });
    </script>
    <![endif]>
</%def>

## Masthead
<%def name="masthead()">
    ## Override
</%def>

<%def name="overlay( title='', content='', visible=False )">
    <%def name="title()"></%def>
    <%def name="content()"></%def>

    <%
    if visible:
        display = "style='display: block;'"
        overlay_class = "in"
    else:
        display = "style='display: none;'"
        overlay_class = ""
    %>

    <div id="overlay" ${display}>

        <div id="overlay-background" class="modal-backdrop fade ${overlay_class}"></div>

        <div id="dialog-box" class="modal dialog-box" border="0" ${display}>
                <div class="modal-header">
                    <span><h3 class='title'>${title}</h3></span>
                </div>
                <div class="modal-body">${content}</div>
                <div class="modal-footer">
                    <div class="buttons" style="float: right;"></div>
                    <div class="extra_buttons" style=""></div>
                    <div style="clear: both;"></div>
                </div>
        </div>
    
    </div>
</%def>

## Document
<html>
    <!--base_panels.mako-->
    ${self.init()}    
    <head>
        %if app.config.brand:
            <title>${self.title()} / ${app.config.brand}</title>
        %else:
            <title>${self.title()}</title>
        %endif
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        ## For mobile browsers, don't scale up
        <meta name = "viewport" content = "maximum-scale=1.0">
        ## Force IE to standards mode, and prefer Google Chrome Frame if the user has already installed it
        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
        ${self.stylesheets()}
        ${self.javascripts()}
    </head>
    
    <body scroll="no" class="full-content ${self.body_class}">
        %if self.require_javascript:
            <noscript>
                <div class="overlay overlay-background">
                    <div class="modal dialog-box" border="0">
                        <div class="modal-header"><h3 class="title">Javascript Required</h3></div>
                        <div class="modal-body">The Galaxy analysis interface requires a browser with Javascript enabled. <br> Please enable Javascript and refresh this page</div>
                    </div>
                </div>
            </noscript>
        %endif
        <div id="everything" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
            ## Background displays first
			%if trans.user:
            <div id="background"></div>
            ## Layer iframes over backgrounds
            <div id="masthead" class="navbar navbar-fixed-top">
                <div class="masthead-inner navbar-inner">
                    ${self.masthead()}
                </div>
            </div>
            <div id="messagebox" class="panel-${app.config.message_box_class}-message">
                %if self.message_box_visible and app.config.message_box_content:
                        ${app.config.message_box_content}
                %endif
            </div>
            ${self.overlay(visible=self.overlay_visible)}
				%if self.has_left_panel:
					<div id="left">
						${self.left_panel()}
						<div class="unified-panel-footer">
							<div class="panel-collapse"></span></div>
							<div class="drag"></div>
						</div>
					</div>
				%endif
			%endif
            <div id="center">
                ${self.center_panel()}
            </div>
			%if trans.user:
				%if self.has_right_panel:
					<div id="right">
						${self.right_panel()}
						<div class="unified-panel-footer">
							<div class="panel-collapse right"></span></div>
							<div class="drag"></div>
						</div>
					</div>
				%endif
			%endif
        </div>
        ## Allow other body level elements
    </body>
    ## Scripts can be loaded later since they progressively add features to
    ## the panels, but do not change layout
    ${self.late_javascripts()}
</html>
