# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383618102.0917921
_template_filename='templates/webapps/tool_shed/repository/preview_tools_in_changeset.mako'
_template_uri='/webapps/tool_shed/repository/preview_tools_in_changeset.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts']


# SOURCE LINE 7

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
    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7f11d8230a50', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f11d8230a50')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x7f11d8230b90', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/repository_actions_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f11d8230b90')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f11d8230410', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f11d8230410')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f11d8230d10', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f11d8230d10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f11d8230a50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f11d8230b90')._populate(_import_ns, [u'render_galaxy_repository_actions'])
        _mako_get_namespace(context, '__anon_0x7f11d8230410')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f11d8230d10')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        containers_dict = _import_ns.get('containers_dict', context.get('containers_dict', UNDEFINED))
        revision_label = _import_ns.get('revision_label', context.get('revision_label', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        render_galaxy_repository_actions = _import_ns.get('render_galaxy_repository_actions', context.get('render_galaxy_repository_actions', UNDEFINED))
        render_repository_items = _import_ns.get('render_repository_items', context.get('render_repository_items', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        changeset_revision_select_field = _import_ns.get('changeset_revision_select_field', context.get('changeset_revision_select_field', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        changeset_revision = _import_ns.get('changeset_revision', context.get('changeset_revision', UNDEFINED))
        metadata = _import_ns.get('metadata', context.get('metadata', UNDEFINED))
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
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14
        __M_writer(u'\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(unicode(render_galaxy_repository_actions( repository=repository )))
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        if message:
            # SOURCE LINE 30
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 32
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Repository \'')
        # SOURCE LINE 34
        __M_writer(filters.html_escape(unicode(repository.name )))
        __M_writer(u'\'</div>\n    <div class="toolFormBody">\n')
        # SOURCE LINE 36
        if len( changeset_revision_select_field.options ) > 1:
            # SOURCE LINE 37
            __M_writer(u'            <form name="change_revision" id="change_revision" action="')
            __M_writer(unicode(h.url_for( controller='repository', action='preview_tools_in_changeset', repository_id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'" method="post" >\n                <div class="form-row">\n                    ')
            # SOURCE LINE 39

            if changeset_revision == repository.tip( trans.app ):
                tip_str = 'repository tip'
            else:
                tip_str = ''
                                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tip_str'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 44
            __M_writer(u'\n                    ')
            # SOURCE LINE 45
            __M_writer(unicode(changeset_revision_select_field.get_html()))
            __M_writer(u' <i>')
            __M_writer(filters.html_escape(unicode(tip_str )))
            __M_writer(u'</i>\n                    <div class="toolParamHelp" style="clear: both;">\n                        Select a revision to inspect and download versions of Galaxy utilities from this repository.\n                    </div>\n                </div>\n            </form>\n')
            # SOURCE LINE 51
        else:
            # SOURCE LINE 52
            __M_writer(u'            <div class="form-row">\n                <label>Revision:</label>\n                ')
            # SOURCE LINE 54
            __M_writer(filters.html_escape(unicode(revision_label )))
            __M_writer(u'\n            </div>\n')
            pass
        # SOURCE LINE 57
        __M_writer(u'    </div>\n</div>\n<p/>\n')
        # SOURCE LINE 60
        __M_writer(unicode(render_repository_items( metadata, containers_dict, can_set_metadata=False, render_repository_actions_for='galaxy' )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f11d8230a50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f11d8230b90')._populate(_import_ns, [u'render_galaxy_repository_actions'])
        _mako_get_namespace(context, '__anon_0x7f11d8230410')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f11d8230d10')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n    ')
        # SOURCE LINE 17
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(unicode(h.css( "library" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f11d8230a50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f11d8230b90')._populate(_import_ns, [u'render_galaxy_repository_actions'])
        _mako_get_namespace(context, '__anon_0x7f11d8230410')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f11d8230d10')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        container_javascripts = _import_ns.get('container_javascripts', context.get('container_javascripts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\n    ')
        # SOURCE LINE 22
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 23
        __M_writer(unicode(h.js("libs/jquery/jquery.rating", "libs/jquery/jstorage" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 24
        __M_writer(unicode(container_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


