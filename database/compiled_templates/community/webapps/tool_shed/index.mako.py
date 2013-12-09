# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383491727.71066
_template_filename='templates/webapps/tool_shed/index.mako'
_template_uri='/webapps/tool_shed/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'init', 'javascripts', 'center_panel', 'left_panel']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x6c01450', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x6c01450')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/tool_shed/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6c01450')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 216
        __M_writer(u'\n\n')
        # SOURCE LINE 235
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6c01450')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'    ')
        __M_writer(unicode(h.css( "base", "autocomplete_tagging", "tool_menu" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u'    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n\n    <style type="text/css">\n        body { margin: 0; padding: 0; overflow: hidden; }\n        #left {\n            background: #C1C9E5 url(')
        # SOURCE LINE 14
        __M_writer(unicode(h.url_for('/static/style/menu_bg.png')))
        __M_writer(u') top repeat-x;\n        }\n        .unified-panel-body {\n            overflow: auto;\n        }\n        .toolMenu {\n            margin-left: 10px;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6c01450')._populate(_import_ns, [u'render_msg'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n    ')
        # SOURCE LINE 30

        self.has_left_panel=True
        self.has_right_panel=False
        self.active_view="tools"
            
        
        # SOURCE LINE 34
        __M_writer(u'\n')
        # SOURCE LINE 35
        if trans.app.config.require_login and not trans.user:
            # SOURCE LINE 36
            __M_writer(u'        <script type="text/javascript">\n            if ( window != top ) {\n                top.location.href = location.href;\n            }\n        </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6c01450')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n    ')
        # SOURCE LINE 26
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6c01450')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        repository_id = _import_ns.get('repository_id', context.get('repository_id', UNDEFINED))
        user_id = _import_ns.get('user_id', context.get('user_id', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        changeset_revision = _import_ns.get('changeset_revision', context.get('changeset_revision', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 218
        __M_writer(u'\n    ')
        # SOURCE LINE 219

        if trans.app.config.require_login and not trans.user:
            center_url = h.url_for( controller='user', action='login', message=message, status=status )
        elif repository_id and changeset_revision:
            # Route in was a sharable url: /view/{owner}/{name}/{changeset_revision}.
            center_url = h.url_for( controller='repository', action='view_repository', id=repository_id, changeset_revision=changeset_revision, message=message, status=status )
        elif repository_id:
            # Route in was a sharable url: /view/{owner}/{name}.
            center_url = h.url_for( controller='repository', action='view_repository', id=repository_id, message=message, status=status )
        elif user_id:
            # Route in was a sharable url: /view/{owner}.
            center_url = h.url_for( controller='repository', action='browse_repositories', operation="repositories_by_user", user_id=user_id, message=message, status=status )
        else:
            center_url = h.url_for( controller='repository', action='browse_categories', message=message, status=status )
            
        
        # SOURCE LINE 233
        __M_writer(u'\n    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 100%; height: 100%;" src="')
        # SOURCE LINE 234
        __M_writer(unicode(center_url))
        __M_writer(u'"></iframe>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6c01450')._populate(_import_ns, [u'render_msg'])
        repository_id = _import_ns.get('repository_id', context.get('repository_id', UNDEFINED))
        user_id = _import_ns.get('user_id', context.get('user_id', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        has_deprecated_repositories = _import_ns.get('has_deprecated_repositories', context.get('has_deprecated_repositories', UNDEFINED))
        has_reviewed_repositories = _import_ns.get('has_reviewed_repositories', context.get('has_reviewed_repositories', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        repository_metadata = _import_ns.get('repository_metadata', context.get('repository_metadata', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n    ')
        # SOURCE LINE 45
        can_review_repositories = trans.app.security_agent.user_can_review_repositories( trans.user ) 
        
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>')
        # SOURCE LINE 47
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.valid_tools )))
        __M_writer(u' valid tools on ')
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.generation_time )))
        __M_writer(u'</div>\n    </div>\n    <div class="unified-panel-body">\n        <div class="toolMenu">\n            <div class="toolSectionList">\n')
        # SOURCE LINE 52
        if user_id or repository_id:
            # SOURCE LINE 54
            __M_writer(u'                    <div class="toolSectionPad"></div>\n                    <div class="toolSectionTitle">\n                        All Repositories\n                    </div>\n                    <div class="toolTitle">\n                        <a href="')
            # SOURCE LINE 59
            __M_writer(unicode(h.url_for( controller='repository', action='index' )))
            __M_writer(u'">Browse by category</a>\n                    </div>\n')
            # SOURCE LINE 61
        else:
            # SOURCE LINE 62
            if repository_metadata:
                # SOURCE LINE 63
                __M_writer(u'                        <div class="toolSectionPad"></div>\n                        <div class="toolSectionTitle">\n                            Search\n                        </div>\n                        <div class="toolSectionBody">\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                # SOURCE LINE 69
                __M_writer(unicode(h.url_for( controller='repository', action='find_tools' )))
                __M_writer(u'">Search for valid tools</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                # SOURCE LINE 72
                __M_writer(unicode(h.url_for( controller='repository', action='find_workflows' )))
                __M_writer(u'">Search for workflows</a>\n                            </div>\n                        </div>\n                        <div class="toolSectionPad"></div>\n                        <div class="toolSectionTitle">\n                            Valid Galaxy Utilities\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                # SOURCE LINE 80
                __M_writer(unicode(h.url_for( controller='repository', action='browse_tools' )))
                __M_writer(u'">Tools</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                # SOURCE LINE 83
                __M_writer(unicode(h.url_for( controller='repository', action='browse_datatypes' )))
                __M_writer(u'">Custom datatypes</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                # SOURCE LINE 86
                __M_writer(unicode(h.url_for( controller='repository', action='browse_repository_dependencies' )))
                __M_writer(u'">Repository dependency definitions</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                # SOURCE LINE 89
                __M_writer(unicode(h.url_for( controller='repository', action='browse_tool_dependencies' )))
                __M_writer(u'">Tool dependency definitions</a>\n                        </div>\n')
                pass
            # SOURCE LINE 92
            __M_writer(u'                    <div class="toolSectionPad"></div>\n                    <div class="toolSectionTitle">\n                        All Repositories\n                    </div>\n                    <div class="toolTitle">\n                        <a target="galaxy_main" href="')
            # SOURCE LINE 97
            __M_writer(unicode(h.url_for( controller='repository', action='browse_categories' )))
            __M_writer(u'">Browse by category</a>\n                    </div>\n')
            # SOURCE LINE 99
            if trans.user:
                # SOURCE LINE 100
                if trans.user.active_repositories:
                    # SOURCE LINE 101
                    __M_writer(u'                            <div class="toolSectionPad"></div>\n                            <div class="toolSectionTitle">\n                                Repositories I Can Change\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 106
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_repositories_i_own' )))
                    __M_writer(u'">Repositories I own</a>\n                            </div>\n')
                    # SOURCE LINE 108
                    if has_reviewed_repositories:
                        # SOURCE LINE 109
                        __M_writer(u'                                <div class="toolTitle">\n                                    <a target="galaxy_main" href="')
                        # SOURCE LINE 110
                        __M_writer(unicode(h.url_for( controller='repository', action='browse_repositories', operation='reviewed_repositories_i_own' )))
                        __M_writer(u'">Reviewed repositories I own</a>\n                                </div>\n')
                        pass
                    # SOURCE LINE 113
                    if has_deprecated_repositories:
                        # SOURCE LINE 114
                        __M_writer(u'                                <div class="toolTitle">\n                                    <a target="galaxy_main" href="')
                        # SOURCE LINE 115
                        __M_writer(unicode(h.url_for( controller='repository', action='browse_deprecated_repositories_i_own' )))
                        __M_writer(u'">Deprecated repositories I own</a>\n                                </div>\n')
                        pass
                    # SOURCE LINE 118
                    __M_writer(u'                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 119
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_my_writable_repositories' )))
                    __M_writer(u'">My writable repositories</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 122
                    __M_writer(unicode(h.url_for( controller='repository', action='reset_metadata_on_my_writable_repositories_in_tool_shed' )))
                    __M_writer(u'">Reset metadata on my repositories</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 125
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_my_writable_repositories_missing_tool_test_components' )))
                    __M_writer(u'">Latest revision: missing tool tests</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 128
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_my_writable_repositories_with_install_errors' )))
                    __M_writer(u'">Latest revision: installation errors</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 131
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_my_writable_repositories_with_failing_tool_tests' )))
                    __M_writer(u'">Latest revision: failing tool tests</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 134
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_my_writable_repositories_with_skip_tool_test_checked' )))
                    __M_writer(u'">Latest revision: skip tool tests</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 137
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_my_writable_repositories_with_no_failing_tool_tests' )))
                    __M_writer(u'">Latest revision: all tool tests pass</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    # SOURCE LINE 140
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_my_writable_repositories_with_invalid_tools' )))
                    __M_writer(u'">Latest revision: invalid tools</a>\n                            </div>\n')
                    pass
                # SOURCE LINE 143
                __M_writer(u'                        <div class="toolSectionPad"></div>\n                        <div class="toolSectionTitle">\n                            Available Actions\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                # SOURCE LINE 148
                __M_writer(unicode(h.url_for( controller='repository', action='create_repository' )))
                __M_writer(u'">Create new repository</a>\n                        </div>\n')
                # SOURCE LINE 150
                if can_review_repositories:
                    # SOURCE LINE 151
                    __M_writer(u'                            <div class="toolSectionPad"></div>\n                            <div class="toolSectionTitle">\n                                Reviewing Repositories\n                            </div>\n                            <div class="toolSectionBody">\n                                <div class="toolSectionBg">\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 158
                    __M_writer(unicode(h.url_for( controller='repository_review', action='manage_repositories_ready_for_review' )))
                    __M_writer(u'">Repositories ready for review</a>\n                                    </div>\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 161
                    __M_writer(unicode(h.url_for( controller='repository_review', action='manage_repositories_without_reviews' )))
                    __M_writer(u'">All repositories with no reviews</a>\n                                    </div>\n')
                    # SOURCE LINE 163
                    if trans.user.repository_reviews:
                        # SOURCE LINE 164
                        __M_writer(u'                                        <div class="toolTitle">\n                                            <a target="galaxy_main" href="')
                        # SOURCE LINE 165
                        __M_writer(unicode(h.url_for( controller='repository_review', action='manage_repositories_reviewed_by_me' )))
                        __M_writer(u'">Repositories reviewed by me</a>\n                                        </div>\n')
                        pass
                    # SOURCE LINE 168
                    __M_writer(u'                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 169
                    __M_writer(unicode(h.url_for( controller='repository_review', action='manage_repositories_with_reviews' )))
                    __M_writer(u'">All reviewed repositories</a>\n                                    </div>\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 172
                    __M_writer(unicode(h.url_for( controller='repository_review', action='manage_components' )))
                    __M_writer(u'">Manage review components</a>\n                                    </div>\n                                </div>\n                            </div>\n                            <div class="toolSectionPad"></div>\n                            <div class="toolSectionTitle">\n                                Reviewing Repositories With Tools\n                            </div>\n                            <div class="toolSectionBody">\n                                <div class="toolSectionBg">\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 183
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_repositories_missing_tool_test_components' )))
                    __M_writer(u'">Latest revision: missing tool tests</a>\n                                    </div>\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 186
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_repositories_with_install_errors' )))
                    __M_writer(u'">Latest revision: installation errors</a>\n                                    </div>\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 189
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_repositories_with_failing_tool_tests' )))
                    __M_writer(u'">Latest revision: failing tool tests</a>\n                                    </div>\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 192
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_repositories_with_skip_tool_test_checked' )))
                    __M_writer(u'">Latest revision: skip tool tests</a>\n                                    </div>\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 195
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_repositories_with_no_failing_tool_tests' )))
                    __M_writer(u'">Latest revision: all tool tests pass</a>\n                                    </div>\n                                    <div class="toolTitle">\n                                        <a target="galaxy_main" href="')
                    # SOURCE LINE 198
                    __M_writer(unicode(h.url_for( controller='repository', action='browse_repositories_with_invalid_tools' )))
                    __M_writer(u'">Latest revision: invalid tools</a>\n                                    </div>\n                                </div>\n                            </div>\n')
                    pass
                # SOURCE LINE 203
            else:
                # SOURCE LINE 204
                __M_writer(u'                        <div class="toolSectionPad"></div>\n                        <div class="toolSectionTitle">\n                            Available Actions\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                # SOURCE LINE 209
                __M_writer(unicode(h.url_for( controller='/user', action='login' )))
                __M_writer(u'">Login to create a repository</a>\n                        </div>\n')
                pass
            pass
        # SOURCE LINE 213
        __M_writer(u'            </div>\n        </div>    \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


