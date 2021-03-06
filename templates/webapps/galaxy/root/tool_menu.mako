## Javascript required for tool menu.
<%def name="tool_menu_javascripts()">
    ${h.templates( "tool_link", "panel_section", "tool_search" )}
    ${h.js( "libs/require", "galaxy.autocom_tagging" )}
    
    <script type="text/javascript">
        require.config({ 
                baseUrl: "${h.url_for('/static/scripts')}",
                shim: {
                    "libs/underscore": { exports: "_" }
                }
        });

        require(["mvc/tools"], function(tools) {

            // Init. on document load.
            $(function() {
                // Create tool search, tool panel, and tool panel view.
                var tool_search = new tools.ToolSearch({ 
                        spinner_url: "${h.url_for('/static/images/loading_small_white_bg.gif')}",
                        search_url: "${h.url_for( controller='root', action='tool_search' )}",
                        hidden: false 
                    }),
                    tool_panel = new tools.ToolPanel({ tool_search: tool_search }),
                    tool_panel_view = new tools.ToolPanelView({ collection: tool_panel });

                // Add tool panel to Galaxy object.
                Galaxy.toolPanel = tool_panel;

                ## Populate tool panel if (a) anonymous use possible or (b) user is logged in.
                %if trans.user or not trans.app.config.require_login:
                    tool_panel.reset( tool_panel.parse( ${h.to_json_string( trans.app.toolbox.to_dict( trans ) )} ) );
                %endif

                // If there are tools, render panel and display everything.
                if (tool_panel.length > 1) { // > 1 because tool_search counts as a model
                    tool_panel_view.render();
                    $('.toolMenu').show();
                }
                $('.toolMenuContainer').prepend(tool_panel_view.$el);
                
                // Minsize init hint.
                $( "a[minsizehint]" ).click( function() {
                    if ( parent.handle_minwidth_hint ) {
                        parent.handle_minwidth_hint( $(this).attr( "minsizehint" ) );
                    }
                });
            });

        });
    </script>
</%def>

## Render tool menu.  
<%def name="render_tool_menu()">
    <div class="toolMenuContainer">
        
        <div class="toolMenu" style="display: none">
            ## Feedback when search returns no results.
            <div id="search-no-results" style="display: none; padding-top: 5px">
                <em><strong>Search did not match any tools.</strong></em>
            </div>
            
            ## Link to workflow management. The location of this may change, but eventually
            ## at least some workflows will appear here (the user should be able to
            ## configure which of their stored workflows appear in the tools menu). 
            
            %if t.user:
				<div class="toolSectionPad"></div>
				<div class="toolSectionPad"></div>
            ##     <div class="toolSectionTitle" id="title_XXinternalXXworkflow">
              ##     <span>Workflows</span>
              ##   </div>
              ##   <div id="XXinternalXXworkflow" class="toolSectionBody">
              ##       <div class="toolSectionBg">
                ##         %if t.user.stored_workflow_menu_entries:
                 ##            %for m in t.user.stored_workflow_menu_entries:
                    ##             <div class="toolTitle">
                       ##              <a href="${h.url_for( controller='workflow', action='run', id=trans.security.encode_id(m.stored_workflow_id) )}" target="galaxy_main">${ util.unicodify( m.stored_workflow.name ) }</a>
                          ##       </div>
                          ##   %endfor
                        ## %endif
                         ##<div class="toolTitle">
                            ## <a href="${h.url_for( controller='workflow', action='list_for_run')}" target="galaxy_main">All workflows</a>
                         ##</div>
                    ## </div>
                 ##</div>
            %endif
            
        </div>
    </div>
</%def>
