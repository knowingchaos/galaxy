# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383491727.831356
_template_filename=u'templates/webapps/tool_shed/base_panels.mako'
_template_uri=u'/webapps/tool_shed/base_panels.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['masthead', 'javascripts', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 133
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        def tab(id,display,href,target='_parent',visible=True,extra_class='',menu_options=None):
            context.caller_stack._push_frame()
            try:
                self = context.get('self', UNDEFINED)
                len = context.get('len', UNDEFINED)
                __M_writer = context.writer()
                # SOURCE LINE 19
                __M_writer(u'\n                    ')
                # SOURCE LINE 20

                cls = ""
                a_cls = ""
                extra = ""
                if extra_class:
                    cls += " " + extra_class
                if self.active_view == id:
                    cls += " active"
                if menu_options:
                    cls += " dropdown"
                    a_cls += " dropdown-toggle"
                    extra = "<b class='caret'></b>"
                style = ""
                if not visible:
                    style = "display: none;"
                
                
                # SOURCE LINE 35
                __M_writer(u'\n                    <li class="')
                # SOURCE LINE 36
                __M_writer(unicode(cls))
                __M_writer(u'" style="')
                __M_writer(unicode(style))
                __M_writer(u'">\n')
                # SOURCE LINE 37
                if href:
                    # SOURCE LINE 38
                    __M_writer(u'                            <a class="')
                    __M_writer(unicode(a_cls))
                    __M_writer(u'" data-toggle="dropdown" target="')
                    __M_writer(unicode(target))
                    __M_writer(u'" href="')
                    __M_writer(unicode(href))
                    __M_writer(u'">')
                    __M_writer(unicode(display))
                    __M_writer(unicode(extra))
                    __M_writer(u'</a>\n')
                    # SOURCE LINE 39
                else:
                    # SOURCE LINE 40
                    __M_writer(u'                            <a class="')
                    __M_writer(unicode(a_cls))
                    __M_writer(u'" data-toggle="dropdown">')
                    __M_writer(unicode(display))
                    __M_writer(unicode(extra))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 42
                if menu_options:
                    # SOURCE LINE 43
                    __M_writer(u'                            <ul class="dropdown-menu">\n')
                    # SOURCE LINE 44
                    for menu_item in menu_options:
                        # SOURCE LINE 45
                        if not menu_item:
                            # SOURCE LINE 46
                            __M_writer(u'                                        <li class="divider"></li>\n')
                            # SOURCE LINE 47
                        else:
                            # SOURCE LINE 48
                            __M_writer(u'                                        <li>\n')
                            # SOURCE LINE 49
                            if len ( menu_item ) == 1:
                                # SOURCE LINE 50
                                __M_writer(u'                                            ')
                                __M_writer(unicode(menu_item[0]))
                                __M_writer(u'\n')
                                # SOURCE LINE 51
                            elif len ( menu_item ) == 2:
                                # SOURCE LINE 52
                                __M_writer(u'                                            ')
                                name, link = menu_item 
                                
                                __M_writer(u'\n                                            <a href="')
                                # SOURCE LINE 53
                                __M_writer(unicode(link))
                                __M_writer(u'">')
                                __M_writer(filters.html_escape(unicode(name )))
                                __M_writer(u'</a>\n')
                                # SOURCE LINE 54
                            else:
                                # SOURCE LINE 55
                                __M_writer(u'                                            ')
                                name, link, target = menu_item 
                                
                                __M_writer(u'\n                                            <a target="')
                                # SOURCE LINE 56
                                __M_writer(unicode(target))
                                __M_writer(u'" href="')
                                __M_writer(unicode(link))
                                __M_writer(u'">')
                                __M_writer(filters.html_escape(unicode(name )))
                                __M_writer(u'</a>\n')
                                pass
                            # SOURCE LINE 58
                            __M_writer(u'                                        </li>\n')
                            pass
                        pass
                    # SOURCE LINE 61
                    __M_writer(u'                            </ul>\n')
                    pass
                # SOURCE LINE 63
                __M_writer(u'                    </li>\n                ')
                return ''
            finally:
                context.caller_stack._pop_frame()
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        __M_writer(u'    <div style="position: relative; right: -50%; float: left;">\n        <div style="display: block; position: relative; right: 50%;">\n\n            <ul class="nav" border="0" cellspacing="0">\n    \n                ')
        # SOURCE LINE 64
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'                ')
        __M_writer(unicode(tab( "repositories", "Repositories", h.url_for( controller='/repository', action='index' ) )))
        __M_writer(u'\n                \n')
        # SOURCE LINE 70
        __M_writer(u'                ')
        __M_writer(unicode(tab( "admin", "Admin", h.url_for( controller='/admin', action='index' ), extra_class="admin-only", visible=( trans.user and app.config.is_admin_user( trans.user ) ) )))
        __M_writer(u'\n\n')
        # SOURCE LINE 73
        __M_writer(u'                ')

        menu_options = []
        qa_url = app.config.get( "qa_url", None )
        if qa_url:
            menu_options = [ [_('Galaxy Q&A'), qa_url, "_blank" ] ]
        menu_options.extend( [
            [_('Support'), app.config.get( "support_url", "http://wiki.g2.bx.psu.edu/Support" ), "_blank" ],
            [_('Tool shed wiki'), app.config.get( "wiki_url", "http://wiki.g2.bx.psu.edu/Tool%20Shed" ), "_blank" ],
            [_('Galaxy wiki'), app.config.get( "wiki_url", "http://wiki.g2.bx.psu.edu/" ), "_blank" ],
            [_('Video tutorials (screencasts)'), app.config.get( "screencasts_url", "http://galaxycast.org" ), "_blank" ],
            [_('How to Cite Galaxy'), app.config.get( "citation_url", "http://wiki.g2.bx.psu.edu/Citing%20Galaxy" ), "_blank" ]
        ] )
        tab( "help", _("Help"), None, menu_options=menu_options )
                        
        
        # SOURCE LINE 86
        __M_writer(u'\n\n')
        # SOURCE LINE 89
        __M_writer(u'                ')
  
                    # Menu for user who is not logged in.
        menu_options = [ [ _("Login"), h.url_for( controller='/user', action='login' ), "galaxy_main" ] ]
        if app.config.allow_user_creation:
            menu_options.append( [ _("Register"), h.url_for( controller='/user', action='create', cntrller='user' ), "galaxy_main" ] ) 
        extra_class = "loggedout-only"
        visible = ( trans.user == None )
        tab( "user", _("User"), None, visible=visible, menu_options=menu_options )
        # Menu for user who is logged in.
        if trans.user:
            email = trans.user.email
        else:
            email = ""
        menu_options = [ [ '<a>Logged in as <span id="user-email">%s</span></a>' %  email ] ]
        if app.config.use_remote_user:
            if app.config.remote_user_logout_href:
                menu_options.append( [ _('Logout'), app.config.remote_user_logout_href, "_top" ] )
        else:
            menu_options.append( [ _('Preferences'), h.url_for( controller='/user', action='index', cntrller='user' ), "galaxy_main" ] )
            menu_options.append( [ _('API Keys'), h.url_for( controller='/user', action='api_keys', cntrller='user' ), "galaxy_main" ] )
            logout_url = h.url_for( controller='/user', action='logout' )
            menu_options.append( [ 'Logout', logout_url, "_top" ] )
            menu_options.append( None )
        if app.config.use_remote_user:
            menu_options.append( [ _('Public Name'), h.url_for( controller='/user', action='edit_username', cntrller='user' ), "galaxy_main" ] )
                    
        extra_class = "loggedin-only"
        visible = ( trans.user != None )
        tab( "user", "User", None, visible=visible, menu_options=menu_options )
                        
        
        # SOURCE LINE 118
        __M_writer(u'\n            </ul>\n        </div>\n    </div>\n    \n')
        # SOURCE LINE 124
        __M_writer(u'    <div class="title">\n        <a href="')
        # SOURCE LINE 125
        __M_writer(unicode(h.url_for( app.config.get( 'logo_url', '/' ) )))
        __M_writer(u'">\n        <img border="0" src="')
        # SOURCE LINE 126
        __M_writer(unicode(h.url_for('/static/images/galaxyIcon_noText.png')))
        __M_writer(u'">\n        Galaxy Tool Shed\n')
        # SOURCE LINE 128
        if app.config.brand:
            # SOURCE LINE 129
            __M_writer(u'            <span>/ ')
            __M_writer(unicode(app.config.brand))
            __M_writer(u'</span>\n')
            pass
        # SOURCE LINE 131
        __M_writer(u'        </a>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Galaxy Tool Shed')
        return ''
    finally:
        context.caller_stack._pop_frame()


