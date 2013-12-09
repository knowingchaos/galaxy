# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383491728.7533171
_template_filename='templates/webapps/tool_shed/category/create_category.mako'
_template_uri='/webapps/tool_shed/category/create_category.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x6de62d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x6de62d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6de62d0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        name = _import_ns.get('name', context.get('name', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 13
        if message:
            # SOURCE LINE 14
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 16
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Create Category</div>\n    <div class="toolFormBody">\n        <form name="create_category_form" id="create_category_form" action="')
        # SOURCE LINE 20
        __M_writer(unicode(h.url_for(controller='admin', action='create_category' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Name:</label>\n                <input  name="name" type="textfield" value="')
        # SOURCE LINE 23
        __M_writer(filters.html_escape(unicode(name )))
        __M_writer(u'" size=40"/>\n            </div>\n            <div class="form-row">\n                <label>Description:</label>\n                <input  name="description" type="textfield" value="')
        # SOURCE LINE 27
        __M_writer(filters.html_escape(unicode(description )))
        __M_writer(u'" size=40"/>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="create_category_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x6de62d0')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    ')
        # SOURCE LINE 5
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            $("input:text:first").focus();\n        })\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


