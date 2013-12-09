# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383494624.1085529
_template_filename='templates/webapps/tool_shed/admin/center.mako'
_template_uri='/webapps/tool_shed/admin/center.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f82a405a2d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f82a405a2d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a405a2d0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        if message:
            # SOURCE LINE 8
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 10
        __M_writer(u'\n<h2>Administration</h2>\n\n<p>The menu on the left provides the following features</p>\n<ul>\n    <li>\n        <strong>Categories</strong>\n        <p/>\n        <ul>\n            <li>\n                <strong>Manage categories</strong>\n            </li>\n            <p/>\n        </ul>\n    </li>\n    <li>\n        <strong>Security</strong>\n        <p/>\n        <ul>\n            <li>\n                <strong>Manage users</strong> - provides a view of the registered users and all groups and non-private roles associated \n                with each user.  \n            </li>\n            <p/>\n            <li>\n                <strong>Manage groups</strong> - provides a view of all groups along with the members of the group and the roles associated with\n                each group (both private and non-private roles).  The group names include a link to a page that allows you to manage the users and \n                roles that are associated with the group.\n            </li>\n            <p/>\n            <li>\n                <strong>Manage roles</strong> - provides a view of all non-private roles along with the role type, and the users and groups that\n                are associated with the role.  The role names include a link to a page that allows you to manage the users and groups that are associated \n                with the role.  The page also includes a view of the data library datasets that are associated with the role and the permissions applied \n                to each dataset.\n            </li>\n        </ul>\n    </li>\n    <p/>\n</ul>\n<br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a405a2d0')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'Galaxy Administration')
        return ''
    finally:
        context.caller_stack._pop_frame()


