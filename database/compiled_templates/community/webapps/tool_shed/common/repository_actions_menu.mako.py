# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383491729.8931291
_template_filename=u'templates/webapps/tool_shed/common/repository_actions_menu.mako'
_template_uri=u'/webapps/tool_shed/common/repository_actions_menu.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_galaxy_repository_actions', 'render_tool_shed_repository_actions']


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
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 184
        __M_writer(u'\n\n')
        # SOURCE LINE 204
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_galaxy_repository_actions(context,repository=None):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        changeset_revision = context.get('changeset_revision', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 186
        __M_writer(u'\n    <br/><br/>\n    <ul class="manage-table-actions">\n')
        # SOURCE LINE 189
        if repository:
            # SOURCE LINE 190
            __M_writer(u'            <li><a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='repository', action='install_repositories_by_revision', repository_ids=trans.security.encode_id( repository.id ), changeset_revisions=changeset_revision )))
            __M_writer(u'">Install to Galaxy</a></li>\n            <li><a class="action-button" target="galaxy_main" href="')
            # SOURCE LINE 191
            __M_writer(unicode(h.url_for( controller='repository', action='preview_tools_in_changeset', repository_id=trans.security.encode_id( repository.id ), changeset_revision=changeset_revision )))
            __M_writer(u'">Browse repository</a></li>\n            <li><a class="action-button" id="repository-')
            # SOURCE LINE 192
            __M_writer(unicode(repository.id))
            __M_writer(u'-popup" class="menubutton">Tool Shed Actions</a></li>\n            <div popupmenu="repository-')
            # SOURCE LINE 193
            __M_writer(unicode(repository.id))
            __M_writer(u'-popup">\n                <a class="action-button" target="galaxy_main" href="')
            # SOURCE LINE 194
            __M_writer(unicode(h.url_for( controller='repository', action='browse_valid_categories' )))
            __M_writer(u'">Browse valid repositories</a>\n                <a class="action-button" target="galaxy_main" href="')
            # SOURCE LINE 195
            __M_writer(unicode(h.url_for( controller='repository', action='find_tools' )))
            __M_writer(u'">Search for valid tools</a>\n                <a class="action-button" target="galaxy_main" href="')
            # SOURCE LINE 196
            __M_writer(unicode(h.url_for( controller='repository', action='find_workflows' )))
            __M_writer(u'">Search for workflows</a>\n            </div>\n')
            # SOURCE LINE 198
        else:
            # SOURCE LINE 199
            __M_writer(u'            <li><a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='repository', action='browse_valid_categories' )))
            __M_writer(u'">Browse valid repositories</a></li>\n            <a class="action-button" target="galaxy_main" href="')
            # SOURCE LINE 200
            __M_writer(unicode(h.url_for( controller='repository', action='find_tools' )))
            __M_writer(u'">Search for valid tools</a>\n            <li><a class="action-button" target="galaxy_main" href="')
            # SOURCE LINE 201
            __M_writer(unicode(h.url_for( controller='repository', action='find_workflows' )))
            __M_writer(u'">Search for workflows</a></li>\n')
            pass
        # SOURCE LINE 203
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_shed_repository_actions(context,repository,metadata=None,changeset_revision=None):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4

        from tool_shed.util.review_util import can_browse_repository_reviews, changeset_revision_reviewed_by_user, get_review_by_repository_id_changeset_revision_user_id
        from tool_shed.util.shed_util_common import changeset_is_malicious
        
        if repository.metadata_revisions:
            has_metadata = True
        else:
            has_metadata = False
        
        is_admin = trans.user_is_admin()
        
        if repository.deprecated:
            is_deprecated = True
        else:
            is_deprecated = False
        
        if repository.is_new( trans.app ):
            is_new = True
        else:
            is_new = False
        
        if changeset_is_malicious( trans, trans.security.encode_id( repository.id ), repository.tip( trans.app ) ):
            is_malicious = True
        else:
            is_malicious = False
        
        can_browse_contents = not is_new
        
        if can_browse_repository_reviews( trans, repository ):
            can_browse_reviews = True
        else:
            can_browse_reviews = False
        
        if trans.user and trans.user != repository.user:
            can_contact_owner = True
        else:
            can_contact_owner = False
        
        if not is_new and trans.user and ( is_admin or repository.user == trans.user ) and not is_deprecated:
            can_deprecate = True
        else:
            can_deprecate = False
        
        if not is_deprecated and trans.app.security_agent.can_push( trans.app, trans.user, repository ):
            can_push = True
        else:
            can_push = False
        
        if not is_deprecated and not is_new and ( not is_malicious or can_push ):
            can_download = True
        else:
            can_download = False
        
        if ( is_admin or ( trans.user and trans.user == repository.user ) ) and not repository.deleted and not repository.deprecated and not is_new:
            can_reset_all_metadata = True
        else:
            can_reset_all_metadata = False
        
        if can_push and not is_deprecated:
            can_upload = True
        else:
            can_upload = False
        
        if not is_new and not is_deprecated and trans.user and repository.user != trans.user:
            can_rate = True
        else:
            can_rate = False
        
        if changeset_revision is not None:
            if has_metadata and not is_deprecated and trans.app.security_agent.user_can_review_repositories( trans.user ):
                can_review_repository = True
            else:
                can_review_repository = False
            if changeset_revision_reviewed_by_user( trans, trans.user, repository, changeset_revision ):
                reviewed_by_user = True
            else:
                reviewed_by_user = False
        else:
            can_review_repository = False
            reviewed_by_user = False
        
        if reviewed_by_user:
            review = get_review_by_repository_id_changeset_revision_user_id( trans=trans,
                                                                             repository_id=trans.security.encode_id( repository.id ),
                                                                             changeset_revision=changeset_revision,
                                                                             user_id=trans.security.encode_id( trans.user.id ) )
            review_id = trans.security.encode_id( review.id )
        else:
            review_id = None
        
        if not is_new and not is_deprecated:
            can_set_metadata = True
        else:
            can_set_metadata = False
        
        if changeset_revision is not None:
            if changeset_revision == repository.tip( trans.app ):
                changeset_revision_is_repository_tip = True
            else:
                changeset_revision_is_repository_tip = False
        else:
            changeset_revision_is_repository_tip = False
        
        if trans.user and ( is_admin or repository.user == trans.user ) and is_deprecated:
            can_undeprecate = True
        else:
            can_undeprecate = False
        
        if is_admin or repository.user == trans.user:
            can_manage = True
        else:
            can_manage = False
        
        can_view_change_log = not is_new
        
        if can_push:
            browse_label = 'Browse or delete repository tip files'
        else:
            browse_label = 'Browse repository tip files'
            
        
        # SOURCE LINE 123
        __M_writer(u'\n\n    <br/><br/>\n    <ul class="manage-table-actions">\n')
        # SOURCE LINE 127
        if is_new:
            # SOURCE LINE 128
            if can_upload:
                # SOURCE LINE 129
                __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='upload', action='upload', repository_id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Upload files to repository</a>\n')
                pass
            # SOURCE LINE 131
            if can_undeprecate:
                # SOURCE LINE 132
                __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='deprecate', id=trans.security.encode_id( repository.id ), mark_deprecated=False )))
                __M_writer(u'">Mark repository as not deprecated</a>\n')
                pass
            # SOURCE LINE 134
        else:
            # SOURCE LINE 135
            __M_writer(u'            <li><a class="action-button" id="repository-')
            __M_writer(unicode(repository.id))
            __M_writer(u'-popup" class="menubutton">Repository Actions</a></li>\n            <div popupmenu="repository-')
            # SOURCE LINE 136
            __M_writer(unicode(repository.id))
            __M_writer(u'-popup">\n')
            # SOURCE LINE 137
            if can_review_repository:
                # SOURCE LINE 138
                if reviewed_by_user:
                    # SOURCE LINE 139
                    __M_writer(u'                        <a class="action-button" target="galaxy_main" href="')
                    __M_writer(unicode(h.url_for( controller='repository_review', action='edit_review', id=review_id )))
                    __M_writer(u'">Manage my review of this revision</a>\n')
                    # SOURCE LINE 140
                else:
                    # SOURCE LINE 141
                    __M_writer(u'                        <a class="action-button" target="galaxy_main" href="')
                    __M_writer(unicode(h.url_for( controller='repository_review', action='create_review', id=trans.app.security.encode_id( repository.id ), changeset_revision=changeset_revision )))
                    __M_writer(u'">Add a review to this revision</a>\n')
                    pass
                pass
            # SOURCE LINE 144
            if can_browse_reviews:
                # SOURCE LINE 145
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository_review', action='manage_repository_reviews', id=trans.app.security.encode_id( repository.id ) )))
                __M_writer(u'">Browse reviews of this repository</a>\n')
                pass
            # SOURCE LINE 147
            if can_upload:
                # SOURCE LINE 148
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='upload', action='upload', repository_id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Upload files to repository</a>\n')
                pass
            # SOURCE LINE 150
            if can_manage:
                # SOURCE LINE 151
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='manage_repository', id=trans.app.security.encode_id( repository.id ), changeset_revision=repository.tip( trans.app ) )))
                __M_writer(u'">Manage repository</a>\n')
                # SOURCE LINE 152
            else:
                # SOURCE LINE 153
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='view_repository', id=trans.app.security.encode_id( repository.id ), changeset_revision=repository.tip( trans.app ) )))
                __M_writer(u'">View repository</a>\n')
                pass
            # SOURCE LINE 155
            if can_view_change_log:
                # SOURCE LINE 156
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='view_changelog', id=trans.app.security.encode_id( repository.id ) )))
                __M_writer(u'">View change log</a>\n')
                pass
            # SOURCE LINE 158
            if can_browse_contents:
                # SOURCE LINE 159
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='browse_repository', id=trans.app.security.encode_id( repository.id ) )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(browse_label )))
                __M_writer(u'</a>\n')
                pass
            # SOURCE LINE 161
            if can_rate:
                # SOURCE LINE 162
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='rate_repository', id=trans.app.security.encode_id( repository.id ) )))
                __M_writer(u'">Rate repository</a>\n')
                pass
            # SOURCE LINE 164
            if can_contact_owner:
                # SOURCE LINE 165
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='contact_owner', id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Contact repository owner</a>\n')
                pass
            # SOURCE LINE 167
            if can_reset_all_metadata:
                # SOURCE LINE 168
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='reset_all_metadata', id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Reset all repository metadata</a>\n')
                pass
            # SOURCE LINE 170
            if can_deprecate:
                # SOURCE LINE 171
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='deprecate', id=trans.security.encode_id( repository.id ), mark_deprecated=True )))
                __M_writer(u'" confirm="Click Ok to deprecate this repository.">Mark repository as deprecated</a>\n')
                pass
            # SOURCE LINE 173
            if can_undeprecate:
                # SOURCE LINE 174
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='deprecate', id=trans.security.encode_id( repository.id ), mark_deprecated=False )))
                __M_writer(u'">Mark repository as not deprecated</a>\n')
                pass
            # SOURCE LINE 176
            if can_download:
                # SOURCE LINE 177
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='download', repository_id=trans.app.security.encode_id( repository.id ), changeset_revision=repository.tip( trans.app ), file_type='gz' )))
                __M_writer(u'">Download as a .tar.gz file</a>\n                    <a class="action-button" href="')
                # SOURCE LINE 178
                __M_writer(unicode(h.url_for( controller='repository', action='download', repository_id=trans.app.security.encode_id( repository.id ), changeset_revision=repository.tip( trans.app ), file_type='bz2' )))
                __M_writer(u'">Download as a .tar.bz2 file</a>\n                    <a class="action-button" href="')
                # SOURCE LINE 179
                __M_writer(unicode(h.url_for( controller='repository', action='download', repository_id=trans.app.security.encode_id( repository.id ), changeset_revision=repository.tip( trans.app ), file_type='zip' )))
                __M_writer(u'">Download as a zip file</a>\n')
                pass
            # SOURCE LINE 181
            __M_writer(u'            </div>\n')
            pass
        # SOURCE LINE 183
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


