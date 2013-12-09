##
## Utilities for creating Trackster visualizations.
##

## Render needed CSS files.
<%def name="render_trackster_css_files()">
    ${h.css( "history", "autocomplete_tagging", "trackster", "library", 
             "jquery-ui/smoothness/jquery-ui" )}
</%def>


## Render needed JavaScript files.
<%def name="render_trackster_js_files()">
    ${h.js( "galaxy.panels", "libs/jquery/jstorage", "libs/jquery/jquery.event.drag", "libs/jquery/jquery.event.hover","libs/jquery/jquery.mousewheel", "libs/jquery/jquery-ui", "libs/jquery/jquery-ui-combobox",
    	"libs/require", "libs/farbtastic" )}
</%def>

## Render a block of JavaScript that contains all necessary variables for Trackster.
<%def name="render_trackster_js_vars()">
        add_track_async_url = "${h.url_for( controller='/api/datasets' )}";
        select_datasets_url = "${h.url_for( controller='/visualization', action='list_current_history_datasets' )}";
        reference_url = "${h.url_for( controller='/api/genomes' )}";
        chrom_url = "${h.url_for( controller='/api/genomes' )}";
        datasets_url = "${h.url_for( controller='/api/datasets' )}";
</%def>