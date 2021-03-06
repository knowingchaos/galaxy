!function( exports, $ ){

"use strict"

var ensure_dd_helper = function () {
    // Insert div that covers everything when dragging the borders
    if ( $( "#DD-helper" ).length == 0 ) {
        $( "<div id='DD-helper'/>" ).css( {
            background: 'white', opacity: 0, zIndex: 9000,
            position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' 
        } ).appendTo( "body" ).hide();
    }
}

// Panels

var MIN_PANEL_WIDTH = 150,
    MAX_PANEL_WIDTH = 800;

var Panel = function( options ) {
    this.$panel = options.panel;
    this.$center = options.center;
    this.$drag = options.drag;
    this.$toggle = options.toggle;
    this.left = !options.right;
    this.hidden = false;
    this.hidden_by_tool = false;
    this.saved_size = null;
    this.init();
}
$.extend( Panel.prototype, {
    resize: function( x ) {
        this.$panel.css( "width", x );
        if ( this.left ) {
            this.$center.css( "left", x );
        } else {
            this.$center.css( "right", x );
        }
        // ie7-recalc.js
        if ( document.recalc ) { document.recalc(); }
    },
    do_toggle: function() {
        var self = this;
        if ( this.hidden ) {
            this.$toggle.removeClass( "hidden" );
            if ( this.left ) {
                this.$panel.css( "left", - this.saved_size ).show().animate( { "left": 0 }, "fast", function () {
                    self.resize( self.saved_size );
                });
            } else {
                this.$panel.css( "right", - this.saved_size ).show().animate( { "right": 0 }, "fast", function () {
                    self.resize( self.saved_size );
                });
            }
            self.hidden = false;
        } else {
            self.saved_size = this.$panel.width();
            if ( document.recalc ) { document.recalc(); }
            // Hide border
            if ( this.left ) {
                this.$panel.animate( { left: - this.saved_size }, "fast" );
            } else {
                this.$panel.animate( { right: - this.saved_size }, "fast" );
            }
            // self.resize(0);
            if ( this.left ) {
                this.$center.css( "left", 0 );
            } else {
                this.$center.css( "right", 0 );
            }

            self.hidden = true;
            self.$toggle.addClass( "hidden" );
        }
        this.hidden_by_tool = false;
    },
    handle_minwidth_hint: function( x ) {
        var space = this.$center.width() - ( this.hidden ? this.saved_size : 0 );
        if ( space < x )
        {
            if ( ! this.hidden ) {
                this.do_toggle();
                this.hidden_by_tool = true;
            }
        } else {
            if ( this.hidden_by_tool ) {
                this.do_toggle();
                this.hidden_by_tool = false;
            }
        }
    },
    force_panel: function( op ) {
        if ( ( this.hidden && op == 'show' ) || ( ! this.hidden && op == 'hide' ) ) { 
            this.do_toggle();
        }
    },
    init: function() {
        var self = this;
        // Pull the collapse element out to body level so it is visible when panel is hidden
        this.$toggle.remove().appendTo( "body" );
        // Resizing using drag element
        this.$drag.on( "dragstart", function( e, d ) {
            $( '#DD-helper' ).show();
            d.width = self.$panel.width();
        }).on( "dragend", function() {  
            $( '#DD-helper' ).hide();
        }).on( "drag", function( e, d ) {
            var x;
            if ( self.left ) {
                x = d.width + d.deltaX;
            } else {
                x = d.width - d.deltaX;
            }
            // Limit range
            x = Math.min( MAX_PANEL_WIDTH, Math.max( MIN_PANEL_WIDTH, x ) );
            self.resize( x );
        });
        // Hide/show using toggle element
        self.$toggle.on( "click", function() { self.do_toggle(); } );
    }
});
  
// Modal dialog boxes
var Modal = function( options ) {
    this.$overlay = options.overlay;
    this.$dialog = options.dialog;
    this.$header = this.$dialog.find( ".modal-header" );
    this.$body = this.$dialog.find( ".modal-body" );
    this.$footer = this.$dialog.find( ".modal-footer" );
    this.$backdrop = options.backdrop;
}
$.extend( Modal.prototype, {
    setContent: function( options ) {
        // Title
        if ( options.title ) {
            this.$header.find( ".title" ).html( options.title );
            this.$header.show();
        } else {
            this.$header.hide();
        }
        // Buttons
        this.$footer.hide();
        var $buttons = this.$footer.find( ".buttons" ).html( "" );
        if ( options.buttons ) {
            $.each( options.buttons, function( name, value ) {
                 $buttons.append( $( '<button></button> ' ).text( name ).click( value ) ).append( " " );
            });
            this.$footer.show();
        }
        var $extraButtons = this.$footer.find( ".extra_buttons" ).html( "" );
        if ( options.extra_buttons ) {
            $.each( options.extra_buttons, function( name, value ) {
                 $extraButtons.append( $( '<button></button>' ).text( name ).click( value ) ).append( " " );
            });
            this.$footer.show();
        }
        // Body
        var body = options.body;
        if ( body == "progress" ) {
            body = $("<div class='progress progress-striped active'><div class='bar' style='width: 100%'></div></div>"); 
        }
        this.$body.html( body );
    },
    show: function( options, callback ) {
        if ( ! this.$dialog.is( ":visible" ) ) {
            if ( options.backdrop) {
                this.$backdrop.addClass( "in" );
            } else {
                this.$backdrop.removeClass( "in" );
            }
            this.$overlay.show();
            this.$dialog.show();
            // Fix min-width so that modal cannot shrink considerably if 
            // new content is loaded.
            this.$body.css( "min-width", this.$body.width() );
            // Set max-height so that modal does not exceed window size.
            // FIXME: this could perhaps be handled better using a container for the modal 
            // header-body-footer and setting max-height for the container.
            this.$body.css( "max-height", 
                            // 2* to provide buffer between bottom of modal and bottom of page.
                            $(window).height() - 2 * this.$dialog.offset().top - 
                            this.$footer.outerHeight() - this.$header.outerHeight());
        }
        // Callback on init
        if ( callback ) {
            callback();
        }
    },
    hide: function() {
        var modal = this;
        modal.$dialog.fadeOut( function() {
           modal.$overlay.hide();
           modal.$backdrop.removeClass( "in" );
           modal.$body.children().remove();
           // Clear min-width to allow for modal to take size of new body.
           modal.$body.css( "min-width", undefined );
       });
   }
});

var modal;

$(function(){
   modal = new Modal( { overlay: $("#overlay"), dialog: $("#dialog-box"), backdrop: $("#overlay-background") } );
});

// Backward compatibility
function hide_modal() {
    modal.hide();
}
function show_modal( title, body, buttons, extra_buttons, init_fn ) {
    modal.setContent( { title: title, body: body, buttons: buttons, extra_buttons: extra_buttons } );
    modal.show( { backdrop: true }, init_fn );
}
function show_message( title, body, buttons, extra_buttons, init_fn ) {
    modal.setContent( { title: title, body: body, buttons: buttons, extra_buttons: extra_buttons } );
    modal.show( { backdrop: false }, init_fn  );
}
function show_in_overlay( options ) {
    var width = options.width || '600';
    var height = options.height || '400';
    var scroll = options.scroll || 'auto';
    $("#overlay-background").bind( "click.overlay", function() {
        hide_modal();
        $("#overlay-background").unbind( "click.overlay" );
    });
    show_modal( null, $( "<div style='margin: -5px;'><img id='close_button' style='position:absolute;right:-17px;top:-15px;src='" + galaxy_paths.attributes.image_path + "/closebox.png'><iframe style='margin: 0; padding: 0;' src='" + options.url + "' width='" + width + "' height='" + height + "' scrolling='" + scroll + "' frameborder='0'></iframe></div>" ) );
    $("#close_button").bind( "click", function() { hide_modal(); } );
}

function user_changed( user_email, is_admin ) {
    if ( user_email ) {
        $(".loggedin-only").show();
        $(".loggedout-only").hide();
        $("#user-email").text( user_email );
        if ( is_admin ) {
            $(".admin-only").show();
        }
    } else {
        $(".loggedin-only").hide();
        $(".loggedout-only").show();
        $(".admin-only").hide();
    }
}

// Masthead dropdown menus
$(function() {
    var $dropdowns = $("#masthead ul.nav > li.dropdown > .dropdown-menu");
    $("body").on( "click.nav_popups", function( e ) {
        $dropdowns.hide();
        $("#DD-helper").hide();
        // If the target is in the menu, treat normally
        if ( $(e.target).closest( "#masthead ul.nav > li.dropdown > .dropdown-menu" ).length ) {
            return;
        }
        // Otherwise, was the click in a tab
        var $clicked = $(e.target).closest( "#masthead ul.nav > li.dropdown" );
        if ( $clicked.length ) {
            $("#DD-helper").show();
            $clicked.children( ".dropdown-menu" ).show();
            e.preventDefault();
        }
    });
});

// Exports
exports.ensure_dd_helper = ensure_dd_helper;
exports.Panel = Panel;
exports.Modal = Modal;
exports.hide_modal = hide_modal;
exports.show_modal = show_modal;
exports.show_message = show_message;
exports.show_in_overlay = show_in_overlay;
exports.user_changed = user_changed;

}( window, window.jQuery );
