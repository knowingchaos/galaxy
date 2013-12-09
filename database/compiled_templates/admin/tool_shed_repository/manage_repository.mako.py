# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384135870.700197
_template_filename='templates/admin/tool_shed_repository/manage_repository.mako'
_template_uri='/admin/tool_shed_repository/manage_repository.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f1ba03d9c50', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba03d9c50')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x7f1ba03d9690', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/repository_actions_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba03d9690')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f1ba03d94d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba03d94d0')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7f1ba03d9890', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba03d9890')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba03d9c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d9690')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d94d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d9890')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        containers_dict = _import_ns.get('containers_dict', context.get('containers_dict', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        render_galaxy_repository_actions = _import_ns.get('render_galaxy_repository_actions', context.get('render_galaxy_repository_actions', UNDEFINED))
        render_repository_items = _import_ns.get('render_repository_items', context.get('render_repository_items', UNDEFINED))
        repo_files_dir = _import_ns.get('repo_files_dir', context.get('repo_files_dir', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        in_error_state = _import_ns.get('in_error_state', context.get('in_error_state', UNDEFINED))
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
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(unicode(render_galaxy_repository_actions( repository )))
        __M_writer(u'\n\n')
        # SOURCE LINE 20
        if message:
            # SOURCE LINE 21
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 23
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Installed tool shed repository \'')
        # SOURCE LINE 25
        __M_writer(unicode(repository.name))
        __M_writer(u'\'</div>\n    <div class="toolFormBody">\n        <form name="edit_repository" id="edit_repository" action="')
        # SOURCE LINE 27
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=trans.security.encode_id( repository.id ) )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Tool shed:</label>\n                ')
        # SOURCE LINE 30
        __M_writer(unicode(repository.tool_shed))
        __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Name:</label>\n                ')
        # SOURCE LINE 35
        __M_writer(unicode(repository.name))
        __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Description:</label>\n')
        # SOURCE LINE 40
        if in_error_state:
            # SOURCE LINE 41
            __M_writer(u'                    ')
            __M_writer(unicode(description))
            __M_writer(u'\n')
            # SOURCE LINE 42
        else:
            # SOURCE LINE 43
            __M_writer(u'                    <input name="description" type="textfield" value="')
            __M_writer(unicode(description))
            __M_writer(u'" size="80"/>\n')
            pass
        # SOURCE LINE 45
        __M_writer(u'                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Revision:</label>\n                ')
        # SOURCE LINE 49
        __M_writer(unicode(repository.changeset_revision))
        __M_writer(u'\n            </div>\n            <div class="form-row">\n                <label>Owner:</label>\n                ')
        # SOURCE LINE 53
        __M_writer(unicode(repository.owner))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 55
        if in_error_state:
            # SOURCE LINE 56
            __M_writer(u'                <div class="form-row">\n                    <label>Repository installation error:</label>\n                    ')
            # SOURCE LINE 58
            __M_writer(unicode(repository.error_message))
            __M_writer(u'\n                </div>\n')
            # SOURCE LINE 60
        else:
            # SOURCE LINE 61
            __M_writer(u'                <div class="form-row">\n                    <label>Location:</label>\n                    ')
            # SOURCE LINE 63
            __M_writer(unicode(repo_files_dir))
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 66
        __M_writer(u'            <div class="form-row">\n                <label>Deleted:</label>\n                ')
        # SOURCE LINE 68
        __M_writer(unicode(repository.deleted))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 70
        if not in_error_state:
            # SOURCE LINE 71
            __M_writer(u'                <div class="form-row">\n                    <input type="submit" name="edit_repository_button" value="Save"/>\n                </div>\n')
            pass
        # SOURCE LINE 75
        __M_writer(u'        </form>\n    </div>\n</div>\n<p/>\n')
        # SOURCE LINE 79
        if not in_error_state:
            # SOURCE LINE 80
            __M_writer(u'    ')
            __M_writer(unicode(render_repository_items( repository.metadata, containers_dict, can_set_metadata=False, render_repository_actions_for='galaxy' )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba03d9c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d9690')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d94d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d9890')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 9
        __M_writer(unicode(h.css( "library" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba03d9c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d9690')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d94d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f1ba03d9890')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        container_javascripts = _import_ns.get('container_javascripts', context.get('container_javascripts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 14
        __M_writer(unicode(h.js("libs/jquery/jquery.rating", "libs/jquery/jstorage" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(unicode(container_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


