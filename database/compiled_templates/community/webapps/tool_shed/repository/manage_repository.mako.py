# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383539790.10076
_template_filename='templates/webapps/tool_shed/repository/manage_repository.mako'
_template_uri='/webapps/tool_shed/repository/manage_repository.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts']


# SOURCE LINE 76

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
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f72840781d0', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f72840781d0')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x7f7284078210', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/repository_actions_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f7284078210')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7f7284078d90', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f7284078d90')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f72940881d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f72940881d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f72840781d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f7284078210')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        _mako_get_namespace(context, '__anon_0x7f7284078d90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f72940881d0')._populate(_import_ns, [u'render_msg'])
        containers_dict = _import_ns.get('containers_dict', context.get('containers_dict', UNDEFINED))
        revision_label = _import_ns.get('revision_label', context.get('revision_label', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        skip_tool_tests_check_box = _import_ns.get('skip_tool_tests_check_box', context.get('skip_tool_tests_check_box', UNDEFINED))
        render_tool_shed_repository_actions = _import_ns.get('render_tool_shed_repository_actions', context.get('render_tool_shed_repository_actions', UNDEFINED))
        num_ratings = _import_ns.get('num_ratings', context.get('num_ratings', UNDEFINED))
        current_allow_push_list = _import_ns.get('current_allow_push_list', context.get('current_allow_push_list', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        long_description = _import_ns.get('long_description', context.get('long_description', UNDEFINED))
        alerts_check_box = _import_ns.get('alerts_check_box', context.get('alerts_check_box', UNDEFINED))
        render_review_comment = _import_ns.get('render_review_comment', context.get('render_review_comment', UNDEFINED))
        render_clone_str = _import_ns.get('render_clone_str', context.get('render_clone_str', UNDEFINED))
        display_reviews = _import_ns.get('display_reviews', context.get('display_reviews', UNDEFINED))
        selected_categories = _import_ns.get('selected_categories', context.get('selected_categories', UNDEFINED))
        allow_push_select_field = _import_ns.get('allow_push_select_field', context.get('allow_push_select_field', UNDEFINED))
        to_safe_string = _import_ns.get('to_safe_string', context.get('to_safe_string', UNDEFINED))
        metadata = _import_ns.get('metadata', context.get('metadata', UNDEFINED))
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        skip_tool_test = _import_ns.get('skip_tool_test', context.get('skip_tool_test', UNDEFINED))
        repository_type_select_field = _import_ns.get('repository_type_select_field', context.get('repository_type_select_field', UNDEFINED))
        changeset_revision = _import_ns.get('changeset_revision', context.get('changeset_revision', UNDEFINED))
        categories = _import_ns.get('categories', context.get('categories', UNDEFINED))
        repository_metadata = _import_ns.get('repository_metadata', context.get('repository_metadata', UNDEFINED))
        malicious_check_box = _import_ns.get('malicious_check_box', context.get('malicious_check_box', UNDEFINED))
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
        from tool_shed.util.shed_util_common import changeset_is_malicious
        
        if repository.metadata_revisions:
            has_metadata = True
        else:
            has_metadata = False
        
        is_admin = trans.user_is_admin()
        is_new = repository.is_new( trans.app )
        
        if repository.deprecated:
            is_deprecated = True
        else:
            is_deprecated = False
        
        if changeset_is_malicious( trans, trans.security.encode_id( repository.id ), repository.tip( trans.app ) ):
            is_malicious = True
        else:
            is_malicious = False
        
        if not is_deprecated and trans.app.security_agent.can_push( trans.app, trans.user, repository ):
            can_push = True
        else:
            can_push = False
        
        if not is_deprecated and not is_new and ( not is_malicious or can_push ):
            can_download = True
        else:
            can_download = False
        
        if has_metadata and not is_deprecated and trans.app.security_agent.user_can_review_repositories( trans.user ):
            can_review_repository = True
        else:
            can_review_repository = False
        
        if not is_new and not is_deprecated:
            can_set_metadata = True
        else:
            can_set_metadata = False
        
        if changeset_revision == repository.tip( trans.app ):
            changeset_revision_is_repository_tip = True
        else:
            changeset_revision_is_repository_tip = False
        
        if metadata and can_set_metadata and is_admin and changeset_revision_is_repository_tip:
            can_set_malicious = True
        else:
            can_set_malicious = False
        
        can_view_change_log = not is_new
        
        if repository_metadata and repository_metadata.includes_tools:
            includes_tools = True
        else:
            includes_tools = False
        
        if changeset_revision_is_repository_tip:
            tip_str = 'repository tip'
            sharable_link_label = 'Sharable link to this repository:'
            sharable_link_changeset_revision = None
        else:
            tip_str = ''
            sharable_link_label = 'Sharable link to this repository revision:'
            sharable_link_changeset_revision = changeset_revision
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['can_set_metadata','changeset_is_malicious','tip_str','can_view_change_log','has_metadata','is_new','can_download','changeset_revision_is_repository_tip','is_deprecated','is_malicious','is_admin','includes_tools','can_set_malicious','can_review_repository','can_push','sharable_link_changeset_revision','time_ago','sharable_link_label'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 74
        __M_writer(u'\n\n')
        # SOURCE LINE 82
        __M_writer(u'\n')
        # SOURCE LINE 83
        __M_writer(u'\n\n')
        # SOURCE LINE 88
        __M_writer(u'\n\n')
        # SOURCE LINE 94
        __M_writer(u'\n\n')
        # SOURCE LINE 96
        __M_writer(unicode(render_tool_shed_repository_actions( repository, metadata=metadata, changeset_revision=changeset_revision )))
        __M_writer(u'\n\n')
        # SOURCE LINE 98
        if message:
            # SOURCE LINE 99
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 101
        __M_writer(u'\n')
        # SOURCE LINE 102
        if repository.deprecated:
            # SOURCE LINE 103
            __M_writer(u'    <div class="warningmessage">\n        This repository has been marked as deprecated, so some tool shed features may be restricted.\n    </div>\n')
            pass
        # SOURCE LINE 107
        __M_writer(u'\n')
        # SOURCE LINE 108
        if len( changeset_revision_select_field.options ) > 1:
            # SOURCE LINE 109
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">Repository revision</div>\n        <div class="toolFormBody">\n            <form name="change_revision" id="change_revision" action="')
            # SOURCE LINE 112
            __M_writer(unicode(h.url_for( controller='repository', action='manage_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'" method="post" >\n                <div class="form-row">\n                    ')
            # SOURCE LINE 114
            __M_writer(unicode(changeset_revision_select_field.get_html()))
            __M_writer(u' <i>')
            __M_writer(unicode(tip_str))
            __M_writer(u'</i>\n                    <div class="toolParamHelp" style="clear: both;">\n')
            # SOURCE LINE 116
            if can_review_repository:
                # SOURCE LINE 117
                __M_writer(u'                            Select a revision to inspect for adding or managing a review or for download or installation.\n')
                # SOURCE LINE 118
            else:
                # SOURCE LINE 119
                __M_writer(u'                            Select a revision to inspect for download or installation.\n')
                pass
            # SOURCE LINE 121
            __M_writer(u'                    </div>\n                </div>\n            </form>\n        </div>\n    </div>\n    <p/>\n')
            pass
        # SOURCE LINE 128
        __M_writer(u'<div class="toolForm">\n    <div class="toolFormTitle">Repository \'')
        # SOURCE LINE 129
        __M_writer(filters.html_escape(unicode(repository.name )))
        __M_writer(u'\'</div>\n    <div class="toolFormBody">\n        <form name="edit_repository" id="edit_repository" action="')
        # SOURCE LINE 131
        __M_writer(unicode(h.url_for( controller='repository', action='manage_repository', id=trans.security.encode_id( repository.id ) )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>')
        # SOURCE LINE 133
        __M_writer(unicode(sharable_link_label))
        __M_writer(u'</label>\n                ')
        # SOURCE LINE 134
        __M_writer(unicode(render_sharable_str( repository, changeset_revision=sharable_link_changeset_revision )))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 136
        if can_download:
            # SOURCE LINE 137
            __M_writer(u'                <div class="form-row">\n                    <label>Clone this repository:</label>\n                    ')
            # SOURCE LINE 139
            __M_writer(unicode(render_clone_str( repository )))
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 142
        __M_writer(u'            <div class="form-row">\n                <label>Name:</label>\n')
        # SOURCE LINE 144
        if repository.times_downloaded > 0:
            # SOURCE LINE 145
            __M_writer(u'                    ')
            __M_writer(unicode(repository.name))
            __M_writer(u'\n')
            # SOURCE LINE 146
        else:
            # SOURCE LINE 147
            __M_writer(u'                    <input name="repo_name" type="textfield" value="')
            __M_writer(filters.html_escape(unicode(repository.name )))
            __M_writer(u'" size="40"/>\n')
            pass
        # SOURCE LINE 149
        __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    Repository names cannot be changed if the repository has been cloned.\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            ')
        # SOURCE LINE 154
        __M_writer(unicode(render_repository_type_select_field( repository_type_select_field, render_help=True )))
        __M_writer(u'\n            <div class="form-row">\n                <label>Synopsis:</label>\n                <input name="description" type="textfield" value="')
        # SOURCE LINE 157
        __M_writer(filters.html_escape(unicode(description )))
        __M_writer(u'" size="80"/>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Detailed description:</label>\n')
        # SOURCE LINE 162
        if long_description:
            # SOURCE LINE 163
            __M_writer(u'                    <pre><textarea name="long_description" rows="3" cols="80">')
            __M_writer(filters.html_escape(unicode(long_description )))
            __M_writer(u'</textarea></pre>\n')
            # SOURCE LINE 164
        else:
            # SOURCE LINE 165
            __M_writer(u'                    <textarea name="long_description" rows="3" cols="80"></textarea>\n')
            pass
        # SOURCE LINE 167
        __M_writer(u'                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Revision:</label>\n')
        # SOURCE LINE 171
        if can_view_change_log:
            # SOURCE LINE 172
            __M_writer(u'                    <a href="')
            __M_writer(unicode(h.url_for( controller='repository', action='view_changelog', id=trans.app.security.encode_id( repository.id ) )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(revision_label )))
            __M_writer(u'</a>\n')
            # SOURCE LINE 173
        else:
            # SOURCE LINE 174
            __M_writer(u'                    ')
            __M_writer(filters.html_escape(unicode(revision_label )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 176
        __M_writer(u'            </div>\n            <div class="form-row">\n                <label>Owner:</label>\n                ')
        # SOURCE LINE 179
        __M_writer(filters.html_escape(unicode(repository.user.username )))
        __M_writer(u'\n            </div>\n            <div class="form-row">\n                <label>Times downloaded:</label>\n                ')
        # SOURCE LINE 183
        __M_writer(filters.html_escape(unicode(repository.times_downloaded )))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 185
        if is_admin:
            # SOURCE LINE 186
            __M_writer(u'                <div class="form-row">\n                    <label>Location:</label>\n                    ')
            # SOURCE LINE 188
            __M_writer(filters.html_escape(unicode(repository.repo_path( trans.app ) )))
            __M_writer(u'\n                </div>\n                <div class="form-row">\n                    <label>Deleted:</label>\n                    ')
            # SOURCE LINE 192
            __M_writer(filters.html_escape(unicode(repository.deleted )))
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 195
        __M_writer(u'            <div class="form-row">\n                <input type="submit" name="edit_repository_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        # SOURCE LINE 201
        __M_writer(unicode(render_repository_items( metadata, containers_dict, can_set_metadata=True, render_repository_actions_for='tool_shed' )))
        __M_writer(u'\n')
        # SOURCE LINE 202
        if includes_tools:
            # SOURCE LINE 203
            __M_writer(u'    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">Automated tool tests</div>\n        <div class="toolFormBody">\n            <form name="skip_tool_tests" id="skip_tool_tests" action="')
            # SOURCE LINE 207
            __M_writer(unicode(h.url_for( controller='repository', action='manage_repository', id=trans.security.encode_id( repository.id ), changeset_revision=repository_metadata.changeset_revision )))
            __M_writer(u'" method="post" >\n                <div class="form-row">\n                    <label>Skip automated testing of tools in this revision:</label>\n                    ')
            # SOURCE LINE 210
            __M_writer(unicode(skip_tool_tests_check_box.get_html()))
            __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        Check the box and click <b>Save</b> to skip automated testing of the tools in this revision.\n                    </div>\n                </div>\n                <div style="clear: both"></div>\n                <div class="form-row">\n                <label>Reason for skipping automated testing:</label>\n')
            # SOURCE LINE 218
            if skip_tool_test:
                # SOURCE LINE 219
                __M_writer(u'                    <pre><textarea name="skip_tool_tests_comment" rows="3" cols="80">')
                __M_writer(filters.html_escape(unicode(skip_tool_test.comment )))
                __M_writer(u'</textarea></pre>\n')
                # SOURCE LINE 220
            else:
                # SOURCE LINE 221
                __M_writer(u'                    <textarea name="skip_tool_tests_comment" rows="3" cols="80"></textarea>\n')
                pass
            # SOURCE LINE 223
            __M_writer(u'                </div>\n                <div style="clear: both"></div>\n                <div class="form-row">\n                    <input type="submit" name="skip_tool_tests_button" value="Save"/>\n                </div>\n            </form>\n        </div>\n    </div>\n')
            pass
        # SOURCE LINE 232
        __M_writer(u'<p/>\n<div class="toolForm">\n    <div class="toolFormTitle">Manage categories</div>\n    <div class="toolFormBody">\n        <form name="categories" id="categories" action="')
        # SOURCE LINE 236
        __M_writer(unicode(h.url_for( controller='repository', action='manage_repository', id=trans.security.encode_id( repository.id ) )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Categories</label>\n                <select name="category_id" multiple>\n')
        # SOURCE LINE 240
        for category in categories:
            # SOURCE LINE 241
            if category.id in selected_categories:
                # SOURCE LINE 242
                __M_writer(u'                            <option value="')
                __M_writer(unicode(trans.security.encode_id( category.id )))
                __M_writer(u'" selected>')
                __M_writer(filters.html_escape(unicode(category.name )))
                __M_writer(u'</option>\n')
                # SOURCE LINE 243
            else:
                # SOURCE LINE 244
                __M_writer(u'                            <option value="')
                __M_writer(unicode(trans.security.encode_id( category.id )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(category.name )))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 247
        __M_writer(u'                </select>\n                <div class="toolParamHelp" style="clear: both;">\n                    Multi-select list - hold the appropriate key while clicking to select multiple categories.\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="manage_categories_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        # SOURCE LINE 259
        if trans.app.config.smtp_server:
            # SOURCE LINE 260
            __M_writer(u'    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">Notification on update</div>\n        <div class="toolFormBody">\n            <form name="receive_email_alerts" id="receive_email_alerts" action="')
            # SOURCE LINE 264
            __M_writer(unicode(h.url_for( controller='repository', action='manage_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'" method="post" >\n                <div class="form-row">\n                    <label>Receive email alerts:</label>\n                    ')
            # SOURCE LINE 267
            __M_writer(unicode(alerts_check_box.get_html()))
            __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        Check the box and click <b>Save</b> to receive email alerts when updates to this repository occur.\n                    </div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" name="receive_email_alerts_button" value="Save"/>\n                </div>\n            </form>\n        </div>\n    </div>\n')
            pass
        # SOURCE LINE 279
        __M_writer(u'<p/>\n<div class="toolForm">\n    <div class="toolFormTitle">Grant authority to make changes</div>\n    <div class="toolFormBody">\n        <table class="grid">\n            <tr>\n                <td>')
        # SOURCE LINE 285
        __M_writer(filters.html_escape(unicode(repository.user.username )))
        __M_writer(u'</td>\n                <td>owner</td>\n                <td>&nbsp;</td>\n            </tr>\n')
        # SOURCE LINE 289
        for username in current_allow_push_list:
            # SOURCE LINE 290
            if username != repository.user.username:
                # SOURCE LINE 291
                __M_writer(u'                    <tr>\n                        <td>')
                # SOURCE LINE 292
                __M_writer(filters.html_escape(unicode(username )))
                __M_writer(u'</td>\n                        <td>write</td>\n                        <td><a class="action-button" href="')
                # SOURCE LINE 294
                __M_writer(unicode(h.url_for( controller='repository', action='manage_repository', id=trans.security.encode_id( repository.id ), user_access_button='Remove', remove_auth=username )))
                __M_writer(u'">remove</a>\n                    </tr>\n')
                pass
            pass
        # SOURCE LINE 298
        __M_writer(u'        </table>\n        <br clear="left"/>\n        <form name="user_access" id="user_access" action="')
        # SOURCE LINE 300
        __M_writer(unicode(h.url_for( controller='repository', action='manage_repository', id=trans.security.encode_id( repository.id ) )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Username:</label>\n                ')
        # SOURCE LINE 303
        __M_writer(unicode(allow_push_select_field.get_html()))
        __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n                    Multi-select usernames to grant permission to make changes to this repository\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="user_access_button" value="Grant access"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        # SOURCE LINE 315
        if repository.ratings:
            # SOURCE LINE 316
            __M_writer(u'    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">Rating</div>\n        <div class="toolFormBody">\n            <div class="form-row">\n                <label>Times Rated:</label>\n                ')
            # SOURCE LINE 322
            __M_writer(filters.html_escape(unicode(num_ratings )))
            __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Average Rating:</label>\n                ')
            # SOURCE LINE 327
            __M_writer(unicode(render_star_rating( 'avg_rating', avg_rating, disabled=True )))
            __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n        </div>\n    </div>\n    <p/>\n    <div class="toolForm">\n        <div class="toolFormBody">\n')
            # SOURCE LINE 335
            if display_reviews:
                # SOURCE LINE 336
                __M_writer(u'                <div class="form-row">\n                    <a href="')
                # SOURCE LINE 337
                __M_writer(unicode(h.url_for( controller='repository', action='view_repository', id=trans.security.encode_id( repository.id ), display_reviews=False )))
                __M_writer(u'"><label>Hide Reviews</label></a>\n                </div>\n                <div style="clear: both"></div>\n                <div class="form-row">\n                    <table class="grid">\n                        <thead>\n                            <tr>\n                                <th>Rating</th>\n                                <th>Comments</th>\n                                <th>Reviewed</th>\n                                <th>User</th>\n                            </tr>\n                        </thead>\n                        ')
                # SOURCE LINE 350
                count = 0 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                # SOURCE LINE 351
                for review in repository.ratings:
                    # SOURCE LINE 352
                    __M_writer(u'                            ')

                    count += 1
                    name = 'rating%d' % count
                                                
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count','name'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 355
                    __M_writer(u'\n                            <tr>\n                                <td>')
                    # SOURCE LINE 357
                    __M_writer(unicode(render_star_rating( name, review.rating, disabled=True )))
                    __M_writer(u'</td>\n                                <td>')
                    # SOURCE LINE 358
                    __M_writer(unicode(render_review_comment( to_safe_string( review.comment, to_html=True ) )))
                    __M_writer(u'</td>\n                                <td>')
                    # SOURCE LINE 359
                    __M_writer(unicode(time_ago( review.update_time )))
                    __M_writer(u'</td>\n                                <td>')
                    # SOURCE LINE 360
                    __M_writer(filters.html_escape(unicode(review.user.username )))
                    __M_writer(u'</td>\n                            </tr>\n')
                    pass
                # SOURCE LINE 363
                __M_writer(u'                    </table>\n                </div>\n                <div style="clear: both"></div>\n')
                # SOURCE LINE 366
            else:
                # SOURCE LINE 367
                __M_writer(u'                <div class="form-row">\n                    <a href="')
                # SOURCE LINE 368
                __M_writer(unicode(h.url_for( controller='repository', action='view_repository', id=trans.security.encode_id( repository.id ), display_reviews=True )))
                __M_writer(u'"><label>Display Reviews</label></a>\n                </div>\n                <div style="clear: both"></div>\n')
                pass
            # SOURCE LINE 372
            __M_writer(u'        </div>\n    </div>\n')
            pass
        # SOURCE LINE 375
        __M_writer(u'<p/>\n')
        # SOURCE LINE 376
        if can_set_malicious:
            # SOURCE LINE 377
            __M_writer(u'    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">Malicious repository tip</div>\n        <div class="toolFormBody">\n            <form name="malicious" id="malicious" action="')
            # SOURCE LINE 381
            __M_writer(unicode(h.url_for( controller='repository', action='set_malicious', id=trans.security.encode_id( repository.id ), ctx_str=changeset_revision )))
            __M_writer(u'" method="post">\n                <div class="form-row">\n                    <label>Define repository tip as malicious:</label>\n                    ')
            # SOURCE LINE 384
            __M_writer(unicode(malicious_check_box.get_html()))
            __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        Check the box and click <b>Save</b> to define this repository\'s tip as malicious, restricting it from being download-able.\n                    </div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" name="malicious_button" value="Save"/>\n                </div>\n            </form>\n        </div>\n    </div>\n')
            pass
        # SOURCE LINE 396
        __M_writer(u'<p/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f72840781d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f7284078210')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        _mako_get_namespace(context, '__anon_0x7f7284078d90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f72940881d0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 85
        __M_writer(u'\n    ')
        # SOURCE LINE 86
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 87
        __M_writer(unicode(h.css('base','library','panel_layout','jquery.rating')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f72840781d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f7284078210')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        _mako_get_namespace(context, '__anon_0x7f7284078d90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f72940881d0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        container_javascripts = _import_ns.get('container_javascripts', context.get('container_javascripts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 90
        __M_writer(u'\n    ')
        # SOURCE LINE 91
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 92
        __M_writer(unicode(h.js("libs/jquery/jquery.rating", "libs/jquery/jstorage" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 93
        __M_writer(unicode(container_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


