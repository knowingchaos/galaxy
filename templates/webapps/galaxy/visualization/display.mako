<%inherit file="/display_base.mako"/>
<%namespace file="/visualization/trackster_common.mako" import="*" />

<%def name="javascripts()">
    <% config = item_data %>
    ${parent.javascripts()}

    <script type='text/javascript'>
        $(function() {
            // HACK: add bookmarks container and header.
            $('#right > .unified-panel-body > div').append( 
                $('<div/>').attr('id', 'bookmarks-container')
                .append( $('<h4/>').text('Bookmarks') )
            );
        });
    </script>
    
    <!--[if lt IE 9]>
      <script type='text/javascript' src="${h.url_for('/static/scripts/libs/IE/excanvas.js')}"></script>
    <![endif]-->
</%def>

<%def name="stylesheets()">
    ${parent.stylesheets()}
    
    ## Style changes needed for display.
    <style type="text/css">
        .page-body {
            padding: 0px;
        }
        #bookmarks-container {
            padding-left: 10px;
        }
        .bookmark {
            margin: 0em;
        }
    </style>
</%def>

<%def name="render_item_header( item )">
    ## Don't need to show header
</%def>

<%def name="render_item_links( visualization )">
    <a 
        href="${h.url_for( controller='/visualization', action='imp', id=trans.security.encode_id( visualization.id ) )}"
        class="icon-button import"
        ## Needed to overwide initial width so that link is floated left appropriately.
        style="width: 100%"
        title="Import visualization">Import visualization</a>
</%def>

<%def name="render_item( visualization, config )">
    <div id="${trans.security.encode_id( visualization.id )}" class="unified-panel-body" style="overflow:none;top:0px;"></div>

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

            var ui = new (trackster_ui.TracksterUI)( "${h.url_for('/')}" )
                container_element = $("#${trans.security.encode_id( visualization.id )}");
            
            $(function() {
                var is_embedded = (container_element.parents(".item-content").length > 0);
                
                // HTML setup.
                if (is_embedded) {
                    container_element.css( { "position": "relative" } );
                } else { // Viewing just one shared viz
                    $("#right-border").click(function() { view.resize_window(); });
                }
                
                // Create visualization.
                var callback;
                %if 'viewport' in config:
                    var callback = function() { view.change_chrom( '${config['viewport']['chrom']}', ${config['viewport']['start']}, ${config['viewport']['end']} ); }
                %endif
                view = ui.create_visualization( {
                                                container: container_element,
                                                name: "${config.get('title') | h}",
                                                vis_id: "${config.get('vis_id')}", 
                                                dbkey: "${config.get('dbkey')}"
                                             }, 
                                             ${ h.to_json_string( config.get( 'viewport', dict() ) ) },
                                             ${ h.to_json_string( config['tracks'] ) },
                                             ${ h.to_json_string( config.get('bookmarks') ) }
                                             );
                
                // Set up keyboard navigation.
                ui.init_keyboard_nav(view);
                
                // HACK: set viewport height because it cannot be set automatically. Currently, max height for embedded
                // elts is 25em, so use 20em.
                view.viewport_container.height("20em");
            });

        });

    </script>
</%def>