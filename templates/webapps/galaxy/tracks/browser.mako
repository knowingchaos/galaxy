<%inherit file="/webapps/galaxy/base_panels.mako"/>
<%namespace file="/visualization/trackster_common.mako" import="*" />

<%def name="init()">
<%
    self.has_left_panel=False
    self.has_right_panel=True
    self.active_view="visualization"
    self.message_box_visible=False
%>
</%def>

<%def name="stylesheets()">
    ${parent.stylesheets()}
    ${render_trackster_css_files()}
</%def>

<%def name="javascripts()">
${parent.javascripts()}

<!--[if lt IE 9]>
  <script type='text/javascript' src="${h.url_for('/static/scripts/libs/IE/excanvas.js')}"></script>
<![endif]-->

${render_trackster_js_files()}

<script type="text/javascript">

    require.config({ 
        baseUrl: "${h.url_for('/static/scripts') }",
        shim: {
            "libs/underscore": { exports: "_" },
            "libs/backbone/backbone": { exports: "Backbone" },
            "libs/backbone/backbone-relational": ["libs/backbone/backbone"]
        }
    });
    require( ["base", "viz/visualization", "viz/trackster_ui", "viz/trackster/tracks"], 
             function( base, visualization, trackster_ui, tracks ) {

    ${render_trackster_js_vars()}

    // FIXME: deliberate global required for now due to requireJS integration.
    view = null;

    var browser_router,
        ui = new (trackster_ui.TracksterUI)( "${h.url_for('/')}" );

    /**
     * Set up router.
     */
    var set_up_router = function(options) {
        browser_router = new visualization.TrackBrowserRouter(options);
        Backbone.history.start();   
    };
    

    var browser_router;
    $(function() {

        ui.createButtonMenu();

        // Attach the button menu to the panel header and float it left
        ui.buttonMenu.$el.attr("style", "float: right");
        $("#center .unified-panel-header-inner").append(ui.buttonMenu.$el);
        
        // Hide bookmarks by default right now.
        force_right_panel("hide"); 
        
        // Resize view when showing/hiding right panel (bookmarks for now).
        $("#right-border").click(function() { view.resize_window(); });
        
        %if config:
            view = ui.create_visualization( {
                                            container: $("#browser-container"), 
                                            name: "${config.get('title') | h}",
                                            vis_id: "${config.get('vis_id')}", 
                                            dbkey: "${config.get('dbkey')}"
                                         },
                                         ${ h.to_json_string( config.get( 'viewport', dict() ) ) },
                                         ${ h.to_json_string( config['tracks'] ) },
                                         ${ h.to_json_string( config['bookmarks'] ) },
                                         true
                                         );
            init_editor();
            set_up_router({view: view});
        %else:
            var continue_fn = function() {
                view = ui.create_visualization( {
                    container: $("#browser-container"),
                    name: $("#new-title").val(),
                    dbkey: $("#new-dbkey").val()
                }, ${ h.to_json_string( viewport_config ) } );
                view.editor = true;
                init_editor();
                set_up_router({view: view});
                hide_modal();
            };
            $.ajax({
                url: "${h.url_for( controller='visualization', action='new_browser', default_dbkey=default_dbkey )}",
                data: {},
                error: function() { alert( "Couldn't create new browser" ) },
                success: function(form_html) {
                    show_modal("New Visualization", form_html, {
                        "Cancel": function() { window.location = "${h.url_for( controller='visualization', action='list' )}"; },
                        "Create": function() { $(document).trigger("convert_to_values"); continue_fn(); }
                    });
                    $("#new-title").focus();
                    $("select[name='dbkey']").select2({ width: 'resolve'});
                    // To support the large number of options for dbkey, enable scrolling in overlay.
                    $("#overlay").css("overflow", "auto");
                }
            });
        %endif
        
        /**
         * Initialization for editor-specific functions.
         */
        function init_editor() {
            $("#title").text(view.name + " (" + view.dbkey + ")");
           
            if (!is_in_galaxy_frame())
            window.onbeforeunload = function() {
                if (view.has_changes) {
                    return "There are unsaved changes to your visualization which will be lost.";
                }
            };
                        
            %if add_dataset is not None:
                $.ajax({
                    url: add_track_async_url + "/${add_dataset}",
                    data: { hda_ldda: 'hda', data_type: 'track_config' },
                    dataType: "json",
                    success: function(track_data) { view.add_drawable( trackster_ui.object_from_template(track_data, view, view) ) }
                });
                
            %endif
            
            //
            // Initialize icons.
            //
            
            $("#add-bookmark-button").click(function() {
                // Add new bookmark.
                var position = view.chrom + ":" + view.low + "-" + view.high,
                    annotation = "Bookmark description";
                return ui.add_bookmark(position, annotation, true);
            });

            // make_popupmenu( $("#bookmarks-more-button"), {
            //     "Add from BED dataset": function() {
            //         add_bookmarks();    
            //     }
            // });

            ui.init_keyboard_nav(view);
        };
        
    });

    });

</script>
</%def>

<%def name="center_panel()">
<div class="unified-panel-header" unselectable="on">
    <div class="unified-panel-header-inner">
        <div style="float:left;" id="title"></div>
    </div>
    <div style="clear: both"></div>
</div>
<div id="browser-container" class="unified-panel-body"></div>

</%def>

<%def name="right_panel()">

<div class="unified-panel-header" unselectable="on">
    <div class="unified-panel-header-inner">
        <div style="float: right">
            <a id="add-bookmark-button" class='icon-button menu-button plus-button' href="javascript:void(0);" title="Add bookmark"></a>
            ## <a id="bookmarks-more-button" class='icon-button menu-button gear popup' href="javascript:void(0);" title="More actions"></a>
        </div>
        Bookmarks
    </div>
</div>
<div class="unified-panel-body" style="overflow: auto;">
    <div id="bookmarks-container"></div>
</div>

</%def>
