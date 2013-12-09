# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383551940.669874
_template_filename='templates/webapps/tool_shed/admin/statistics.mako'
_template_uri='/webapps/tool_shed/admin/statistics.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x7f69b085e190', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f69b085e190')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f69b085e190')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
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
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Tool shed statistics generated on ')
        # SOURCE LINE 9
        __M_writer(unicode(trans.app.shed_counter.generation_time))
        __M_writer(u'</div>\n        <form name="regenerate_statistics" id="regenerate_statistics" action="')
        # SOURCE LINE 10
        __M_writer(unicode(h.url_for( controller='admin', action='regenerate_statistics' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <table class="grid">\n                    <tr>\n                        <th>Item</th>\n                        <th>Count</th>\n                    </tr>\n                    <tr>\n                        <td>Total repositories</td>\n                        <td>')
        # SOURCE LINE 19
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.repositories )))
        __M_writer(u'</td>\n                    </tr>\n')
        # SOURCE LINE 25
        __M_writer(u'                    <tr>\n                        <td>Deleted repositories</td>\n                        <td>')
        # SOURCE LINE 27
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.deleted_repositories )))
        __M_writer(u'</td>\n                    </tr>\n                    <tr>\n                        <td>Valid tools</td>\n                        <td>')
        # SOURCE LINE 31
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.valid_tools )))
        __M_writer(u'</td>\n                    </tr>\n                    <tr>\n                        <td>Invalid tools</td>\n                        <td>')
        # SOURCE LINE 35
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.invalid_tools )))
        __M_writer(u'</td>\n                    </tr>\n                    <tr>\n                        <td>Workflows</td>\n                        <td>')
        # SOURCE LINE 39
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.workflows )))
        __M_writer(u'</td>\n                    </tr>\n                    <tr>\n                        <td>Proprietary datatypes</td>\n                        <td>')
        # SOURCE LINE 43
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.proprietary_datatypes )))
        __M_writer(u'</td>\n                    </tr>\n                    <tr>\n                        <td>Total clones</td>\n                        <td>')
        # SOURCE LINE 47
        __M_writer(filters.html_escape(unicode(trans.app.shed_counter.total_clones )))
        __M_writer(u'</td>\n                    </tr>\n                </table>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="regenerate_statistics_button" value="Regenerate statistics"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


