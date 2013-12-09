# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383491729.3676829
_template_filename='templates/webapps/tool_shed/repository/create_repository.mako'
_template_uri='/webapps/tool_shed/repository/create_repository.mako'
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
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x704b850', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x704b850')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x704bed0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x704bed0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x704b850')._populate(_import_ns, [u'render_repository_type_select_field'])
        _mako_get_namespace(context, '__anon_0x704bed0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_repository_type_select_field = _import_ns.get('render_repository_type_select_field', context.get('render_repository_type_select_field', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        name = _import_ns.get('name', context.get('name', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        selected_categories = _import_ns.get('selected_categories', context.get('selected_categories', UNDEFINED))
        repository_type_select_field = _import_ns.get('repository_type_select_field', context.get('repository_type_select_field', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        long_description = _import_ns.get('long_description', context.get('long_description', UNDEFINED))
        categories = _import_ns.get('categories', context.get('categories', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        if message:
            # SOURCE LINE 15
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Create Repository</div>\n    <div class="toolFormBody">\n        <form name="create_repository_form" id="create_repository_form" action="')
        # SOURCE LINE 21
        __M_writer(unicode(h.url_for( controller='repository', action='create_repository' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Name:</label>\n                <input  name="name" type="textfield" value="')
        # SOURCE LINE 24
        __M_writer(filters.html_escape(unicode(name )))
        __M_writer(u'" size="40"/>\n                <div style="clear: both"></div>\n            </div>\n            ')
        # SOURCE LINE 27
        __M_writer(unicode(render_repository_type_select_field( repository_type_select_field, render_help=True )))
        __M_writer(u'\n            <div class="form-row">\n                <label>Synopsis:</label>\n                <input  name="description" type="textfield" value="')
        # SOURCE LINE 30
        __M_writer(filters.html_escape(unicode(description )))
        __M_writer(u'" size="80"/>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Detailed description:</label>\n')
        # SOURCE LINE 35
        if long_description:
            # SOURCE LINE 36
            __M_writer(u'                    <pre><textarea name="long_description" rows="3" cols="80">')
            __M_writer(filters.html_escape(unicode(long_description )))
            __M_writer(u'</textarea></pre>\n')
            # SOURCE LINE 37
        else:
            # SOURCE LINE 38
            __M_writer(u'                    <textarea name="long_description" rows="3" cols="80"></textarea>\n')
            pass
        # SOURCE LINE 40
        __M_writer(u'                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Categories</label>\n                <div class="form-row">\n                    <select name="category_id" multiple>\n')
        # SOURCE LINE 46
        for category in categories:
            # SOURCE LINE 47
            if category.id in selected_categories:
                # SOURCE LINE 48
                __M_writer(u'                                <option value="')
                __M_writer(unicode(trans.security.encode_id( category.id )))
                __M_writer(u'" selected>')
                __M_writer(filters.html_escape(unicode(category.name )))
                __M_writer(u'</option>\n')
                # SOURCE LINE 49
            else:
                # SOURCE LINE 50
                __M_writer(u'                                <option value="')
                __M_writer(unicode(trans.security.encode_id( category.id )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(category.name )))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 53
        __M_writer(u'                    </select>\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    Multi-select list - hold the appropriate key while clicking to select multiple categories.\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="create_repository_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x704b850')._populate(_import_ns, [u'render_repository_type_select_field'])
        _mako_get_namespace(context, '__anon_0x704bed0')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    ')
        # SOURCE LINE 6
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            $("input:text:first").focus();\n        })\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


