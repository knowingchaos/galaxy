# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383497263.923203
_template_filename='templates/webapps/tool_shed/category/edit_category.mako'
_template_uri='/webapps/tool_shed/category/edit_category.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f82a80adb90', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f82a80adb90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82a80adb90')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        category = _import_ns.get('category', context.get('category', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        if message:
            # SOURCE LINE 5
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 7
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Change category name and description</div>\n    <div class="toolFormBody">\n        <form name="edit_category" action="')
        # SOURCE LINE 11
        __M_writer(unicode(h.url_for( controller='admin', action='edit_category' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Name:</label>\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input type="text" name="name" value="')
        # SOURCE LINE 15
        __M_writer(filters.html_escape(unicode(category.name )))
        __M_writer(u'" size="40"/>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Description:</label>\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input  name="description" type="textfield" value="')
        # SOURCE LINE 22
        __M_writer(filters.html_escape(unicode(category.description )))
        __M_writer(u'" size=40"/>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input type="hidden" name="rename" value="submitted"/>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input type="hidden" name="id" value="')
        # SOURCE LINE 34
        __M_writer(unicode(trans.security.encode_id( category.id )))
        __M_writer(u'"/>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="edit_category_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


