# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383491729.8254659
_template_filename='templates/webapps/tool_shed/repository/view_repository.mako'
_template_uri='/webapps/tool_shed/repository/view_repository.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts']


# SOURCE LINE 30

def inherit(context):
    if context.get('use_panels'):
        return '/webapps/tool_shed/base_panels.mako'
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7fe160459410', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe160459410')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x7fe160459650', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/repository_actions_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe160459650')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7fe1604594d0', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe1604594d0')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7fe160459590', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe160459590')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fe160459410')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fe160459650')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7fe1604594d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7fe160459590')._populate(_import_ns, [u'*'])
        containers_dict = _import_ns.get('containers_dict', context.get('containers_dict', UNDEFINED))
        revision_label = _import_ns.get('revision_label', context.get('revision_label', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        render_tool_shed_repository_actions = _import_ns.get('render_tool_shed_repository_actions', context.get('render_tool_shed_repository_actions', UNDEFINED))
        num_ratings = _import_ns.get('num_ratings', context.get('num_ratings', UNDEFINED))
        render_long_description = _import_ns.get('render_long_description', context.get('render_long_description', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        alerts_check_box = _import_ns.get('alerts_check_box', context.get('alerts_check_box', UNDEFINED))
        render_review_comment = _import_ns.get('render_review_comment', context.get('render_review_comment', UNDEFINED))
        render_clone_str = _import_ns.get('render_clone_str', context.get('render_clone_str', UNDEFINED))
        display_reviews = _import_ns.get('display_reviews', context.get('display_reviews', UNDEFINED))
        render_galaxy_repository_actions = _import_ns.get('render_galaxy_repository_actions', context.get('render_galaxy_repository_actions', UNDEFINED))
        metadata = _import_ns.get('metadata', context.get('metadata', UNDEFINED))
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        is_malicious = _import_ns.get('is_malicious', context.get('is_malicious', UNDEFINED))
        repository_type_select_field = _import_ns.get('repository_type_select_field', context.get('repository_type_select_field', UNDEFINED))
        changeset_revision = _import_ns.get('changeset_revision', context.get('changeset_revision', UNDEFINED))
        render_repository_type_select_field = _import_ns.get('render_repository_type_select_field', context.get('render_repository_type_select_field', UNDEFINED))
        render_star_rating = _import_ns.get('render_star_rating', context.get('render_star_rating', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        avg_rating = _import_ns.get('avg_rating', context.get('avg_rating', UNDEFINED))
        render_repository_items = _import_ns.get('render_repository_items', context.get('render_repository_items', UNDEFINED))
        render_sharable_str = _import_ns.get('render_sharable_str', context.get('render_sharable_str', UNDEFINED))
        changeset_revision_select_field = _import_ns.get('changeset_revision_select_field', context.get('changeset_revision_select_field', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7

        from galaxy.web.framework.helpers import time_ago
        from tool_shed.util.shed_util_common import to_safe_string
        
        is_new = repository.is_new( trans.app )
        is_deprecated = repository.deprecated
        
        can_browse_contents = trans.webapp.name == 'tool_shed' and not is_new
        can_push = not is_deprecated and trans.app.security_agent.can_push( trans.app, trans.user, repository )
        can_download = not is_deprecated and not is_new and ( not is_malicious or can_push )
        can_view_change_log = trans.webapp.name == 'tool_shed' and not is_new
        changeset_revision_is_repository_tip = changeset_revision == repository.tip( trans.app )
        
        if changeset_revision_is_repository_tip:
            tip_str = 'repository tip'
            sharable_link_label = 'Sharable link to this repository:'
            sharable_link_changeset_revision = None
        else:
            tip_str = ''
            sharable_link_label = 'Sharable link to this repository revision:'
            sharable_link_changeset_revision = changeset_revision
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tip_str','can_browse_contents','is_new','to_safe_string','changeset_revision_is_repository_tip','is_deprecated','can_view_change_log','can_download','can_push','sharable_link_changeset_revision','time_ago','sharable_link_label'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n\n')
        # SOURCE LINE 50
        if trans.webapp.name == 'tool_shed':
            # SOURCE LINE 51
            __M_writer(u'    ')
            __M_writer(unicode(render_tool_shed_repository_actions( repository=repository, changeset_revision=changeset_revision )))
            __M_writer(u'\n')
            # SOURCE LINE 52
        else:
            # SOURCE LINE 53
            __M_writer(u'    ')
            __M_writer(unicode(render_galaxy_repository_actions( repository=repository )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 55
        __M_writer(u'\n')
        # SOURCE LINE 56
        if message:
            # SOURCE LINE 57
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 59
        __M_writer(u'\n')
        # SOURCE LINE 60
        if repository.deprecated:
            # SOURCE LINE 61
            __M_writer(u'    <div class="warningmessage">\n        This repository has been marked as deprecated, so some tool shed features may be restricted.\n    </div>\n')
            pass
        # SOURCE LINE 65
        __M_writer(u'\n')
        # SOURCE LINE 66
        if len( changeset_revision_select_field.options ) > 1:
            # SOURCE LINE 67
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">Repository revision</div>\n        <div class="toolFormBody">\n            <form name="change_revision" id="change_revision" action="')
            # SOURCE LINE 70
            __M_writer(unicode(h.url_for( controller='repository', action='view_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'" method="post" >\n                <div class="form-row">\n                    ')
            # SOURCE LINE 72
            __M_writer(unicode(changeset_revision_select_field.get_html()))
            __M_writer(u' <i>')
            __M_writer(unicode(tip_str))
            __M_writer(u'</i>\n                    <div class="toolParamHelp" style="clear: both;">\n                        Select a revision to inspect and download versions of Galaxy utilities from this repository.\n                    </div>\n                </div>\n            </form>\n        </div>\n    </div>\n    <p/>\n')
            pass
        # SOURCE LINE 82
        __M_writer(u'<div class="toolForm">\n    <div class="toolFormTitle">Repository \'')
        # SOURCE LINE 83
        __M_writer(filters.html_escape(unicode(repository.name )))
        __M_writer(u'\'</div>\n    <div class="toolFormBody">\n        <div class="form-row">\n            <label>')
        # SOURCE LINE 86
        __M_writer(unicode(sharable_link_label))
        __M_writer(u'</label>\n            ')
        # SOURCE LINE 87
        __M_writer(unicode(render_sharable_str( repository, changeset_revision=sharable_link_changeset_revision )))
        __M_writer(u'\n        </div>\n')
        # SOURCE LINE 89
        if can_download:
            # SOURCE LINE 90
            __M_writer(u'            <div class="form-row">\n                <label>Clone this repository:</label>\n                ')
            # SOURCE LINE 92
            __M_writer(unicode(render_clone_str( repository )))
            __M_writer(u'\n            </div>\n')
            pass
        # SOURCE LINE 95
        __M_writer(u'        <div class="form-row">\n            <label>Name:</label>\n')
        # SOURCE LINE 97
        if can_browse_contents:
            # SOURCE LINE 98
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='repository', action='browse_repository', id=trans.app.security.encode_id( repository.id ) )))
            __M_writer(u'">')
            __M_writer(unicode(repository.name))
            __M_writer(u'</a>\n')
            # SOURCE LINE 99
        else:
            # SOURCE LINE 100
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(repository.name )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 102
        __M_writer(u'        </div>\n        ')
        # SOURCE LINE 103
        __M_writer(unicode(render_repository_type_select_field( repository_type_select_field, render_help=False )))
        __M_writer(u'\n        <div class="form-row">\n            <label>Synopsis:</label>\n            ')
        # SOURCE LINE 106
        __M_writer(filters.html_escape(unicode(repository.description )))
        __M_writer(u'\n        </div>\n')
        # SOURCE LINE 108
        if repository.long_description:
            # SOURCE LINE 109
            __M_writer(u'            ')
            __M_writer(unicode(render_long_description( to_safe_string( repository.long_description, to_html=True ) )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 111
        __M_writer(u'        <div class="form-row">\n            <label>Revision:</label>\n')
        # SOURCE LINE 113
        if can_view_change_log:
            # SOURCE LINE 114
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='repository', action='view_changelog', id=trans.app.security.encode_id( repository.id ) )))
            __M_writer(u'">')
            __M_writer(unicode(revision_label))
            __M_writer(u'</a>\n')
            # SOURCE LINE 115
        else:
            # SOURCE LINE 116
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(revision_label )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 118
        __M_writer(u'        </div>\n        <div class="form-row">\n            <label>Owner:</label>\n            ')
        # SOURCE LINE 121
        __M_writer(filters.html_escape(unicode(repository.user.username )))
        __M_writer(u'\n        </div>\n        <div class="form-row">\n            <label>Times downloaded:</label>\n            ')
        # SOURCE LINE 125
        __M_writer(unicode(repository.times_downloaded))
        __M_writer(u'\n        </div>\n')
        # SOURCE LINE 127
        if trans.user_is_admin():
            # SOURCE LINE 128
            __M_writer(u'            <div class="form-row">\n                <label>Location:</label>\n                ')
            # SOURCE LINE 130
            __M_writer(filters.html_escape(unicode(repository.repo_path( trans.app ) )))
            __M_writer(u'\n            </div>\n            <div class="form-row">\n                <label>Deleted:</label>\n                ')
            # SOURCE LINE 134
            __M_writer(unicode(repository.deleted))
            __M_writer(u'\n            </div>\n')
            pass
        # SOURCE LINE 137
        __M_writer(u'    </div>\n</div>\n')
        # SOURCE LINE 139
        __M_writer(unicode(render_repository_items( metadata, containers_dict, can_set_metadata=False, render_repository_actions_for='tool_shed' )))
        __M_writer(u'\n')
        # SOURCE LINE 140
        if repository.categories:
            # SOURCE LINE 141
            __M_writer(u'    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">Categories</div>\n        <div class="toolFormBody">\n')
            # SOURCE LINE 145
            for rca in repository.categories:
                # SOURCE LINE 146
                __M_writer(u'                <div class="form-row">\n                    ')
                # SOURCE LINE 147
                __M_writer(filters.html_escape(unicode(rca.category.name )))
                __M_writer(u'\n                </div>\n')
                pass
            # SOURCE LINE 150
            __M_writer(u'            <div style="clear: both"></div>\n        </div>\n    </div>\n')
            pass
        # SOURCE LINE 154
        if trans.webapp.name == 'tool_shed' and trans.user and trans.app.config.smtp_server:
            # SOURCE LINE 155
            __M_writer(u'    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">Notification on update</div>\n        <div class="toolFormBody">\n            <form name="receive_email_alerts" id="receive_email_alerts" action="')
            # SOURCE LINE 159
            __M_writer(unicode(h.url_for( controller='repository', action='view_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'" method="post" >\n                <div class="form-row">\n                    <label>Receive email alerts:</label>\n                    ')
            # SOURCE LINE 162
            __M_writer(unicode(alerts_check_box.get_html()))
            __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        Check the box and click <b>Save</b> to receive email alerts when updates to this repository occur.\n                    </div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" name="receive_email_alerts_button" value="Save"/>\n                </div>\n            </form>\n        </div>\n    </div>\n')
            pass
        # SOURCE LINE 174
        if repository.ratings:
            # SOURCE LINE 175
            __M_writer(u'    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">Rating</div>\n        <div class="toolFormBody">\n            <div class="form-row">\n                <label>Times Rated:</label>\n                ')
            # SOURCE LINE 181
            __M_writer(unicode(num_ratings))
            __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Average Rating:</label>\n                ')
            # SOURCE LINE 186
            __M_writer(unicode(render_star_rating( 'avg_rating', avg_rating, disabled=True )))
            __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n        </div>\n    </div>\n    <p/>\n    <div class="toolForm">\n        <div class="toolFormBody">\n')
            # SOURCE LINE 194
            if display_reviews:
                # SOURCE LINE 195
                __M_writer(u'                <div class="form-row">\n                    <a href="')
                # SOURCE LINE 196
                __M_writer(unicode(h.url_for( controller='repository', action='view_repository', id=trans.security.encode_id( repository.id ), display_reviews=False )))
                __M_writer(u'"><label>Hide Reviews</label></a>\n                </div>\n                <div style="clear: both"></div>\n                <div class="form-row">\n                    <table class="grid">\n                        <thead>\n                            <tr>\n                                <th>Rating</th>\n                                <th>Comments</th>\n                                <th>Reviewed</th>\n                                <th>User</th>\n                            </tr>\n                        </thead>\n                        ')
                # SOURCE LINE 209
                count = 0 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                # SOURCE LINE 210
                for review in repository.ratings:
                    # SOURCE LINE 211
                    __M_writer(u'                            ')

                    count += 1
                    name = 'rating%d' % count
                                                
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count','name'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 214
                    __M_writer(u'\n                            <tr>\n                                <td>')
                    # SOURCE LINE 216
                    __M_writer(unicode(render_star_rating( name, review.rating, disabled=True )))
                    __M_writer(u'</td>\n                                <td>')
                    # SOURCE LINE 217
                    __M_writer(unicode(render_review_comment( to_safe_string( review.comment, to_html=True ) )))
                    __M_writer(u'</td>\n                                <td>')
                    # SOURCE LINE 218
                    __M_writer(unicode(time_ago( review.update_time )))
                    __M_writer(u'</td>\n                                <td>')
                    # SOURCE LINE 219
                    __M_writer(unicode(review.user.username))
                    __M_writer(u'</td>\n                            </tr>\n')
                    pass
                # SOURCE LINE 222
                __M_writer(u'                    </table>\n                </div>\n                <div style="clear: both"></div>\n')
                # SOURCE LINE 225
            else:
                # SOURCE LINE 226
                __M_writer(u'                <div class="form-row">\n                    <a href="')
                # SOURCE LINE 227
                __M_writer(unicode(h.url_for( controller='repository', action='view_repository', id=trans.security.encode_id( repository.id ), display_reviews=True )))
                __M_writer(u'"><label>Display Reviews</label></a>\n                </div>\n                <div style="clear: both"></div>\n')
                pass
            # SOURCE LINE 231
            __M_writer(u'        </div>\n    </div>\n')
            pass
        # SOURCE LINE 234
        __M_writer(u'<p/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fe160459410')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fe160459650')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7fe1604594d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7fe160459590')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n    ')
        # SOURCE LINE 40
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 41
        __M_writer(unicode(h.css('base','library','panel_layout','jquery.rating')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fe160459410')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fe160459650')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7fe1604594d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7fe160459590')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        container_javascripts = _import_ns.get('container_javascripts', context.get('container_javascripts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n    ')
        # SOURCE LINE 45
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 46
        __M_writer(unicode(h.js("libs/jquery/jquery.rating", "libs/jquery/jstorage" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 47
        __M_writer(unicode(container_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


