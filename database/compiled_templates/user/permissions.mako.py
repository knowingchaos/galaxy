# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383217683.4282601
_template_filename='templates/user/permissions.mako'
_template_uri='user/permissions.mako'
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
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f973417d5d0', context._clean_inheritance_tokens(), templateuri=u'/dataset/security_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f973417d5d0')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f971c05d050', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f971c05d050')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f973417d5d0')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x7f971c05d050')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_permission_form = _import_ns.get('render_permission_form', context.get('render_permission_form', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
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
        __M_writer(u'\n<br/><br/>\n<ul class="manage-table-actions">\n    <li>\n        <a class="action-button"  href="')
        # SOURCE LINE 14
        __M_writer(unicode(h.url_for( controller='user', cntrller=cntrller, action='index')))
        __M_writer(u'">User preferences</a>\n    </li>\n</ul>\n')
        # SOURCE LINE 17
        if trans.user:
            # SOURCE LINE 18
            __M_writer(u'    ')
            __M_writer(unicode(render_permission_form( trans.user, trans.user.email, h.url_for( controller='user', action='set_default_permissions', cntrller=cntrller ), trans.user.all_roles() )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f973417d5d0')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x7f971c05d050')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'Change Default Permissions on New Histories')
        return ''
    finally:
        context.caller_stack._pop_frame()


