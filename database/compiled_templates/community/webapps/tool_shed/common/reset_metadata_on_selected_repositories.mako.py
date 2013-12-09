# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383494643.6830299
_template_filename='templates/webapps/tool_shed/common/reset_metadata_on_selected_repositories.mako'
_template_uri='/webapps/tool_shed/common/reset_metadata_on_selected_repositories.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x7f82b82edc90', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f82b82edc90')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f82b82ed850', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f82b82ed850')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82b82edc90')._populate(_import_ns, [u'common_misc_javascripts'])
        _mako_get_namespace(context, '__anon_0x7f82b82ed850')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        repositories_select_field = _import_ns.get('repositories_select_field', context.get('repositories_select_field', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        if message:
            # SOURCE LINE 11
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 13
        __M_writer(u'\n<div class="warningmessage">\n    Resetting metadata may take a while because this process clones each change set in each selected repository\'s change log to a temporary location on disk.\n    Wait until this page redirects after clicking the <b>Reset metadata on selected repositories</b> button, as doing anything else will not be helpful.  Watch \n    the tool shed paster log to pass the time if necessary.\n</div>\n\n<div class="toolForm">\n    <div class="toolFormTitle">Reset all metadata on each selected repository</div>\n        ')
        # SOURCE LINE 22

        if trans.user_is_admin():
            controller = 'admin'
            action = 'reset_metadata_on_selected_repositories_in_tool_shed'
        else:
            controller = 'repository'
            action = 'reset_metadata_on_my_writable_repositories_in_tool_shed'
                
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['action','controller'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 29
        __M_writer(u'\n        <form name="reset_metadata_on_selected_repositories" id="reset_metadata_on_selected_repositories" action="')
        # SOURCE LINE 30
        __M_writer(unicode(h.url_for( controller=controller, action=action )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                Check each repository for which you want to reset metadata.  Repository names are followed by owners in parentheses.\n            </div>\n            <div style="clear: both"></div>\n            <div class="form-row">\n                <input type="checkbox" id="checkAll" name="select_all_repositories_checkbox" value="true" onclick="checkAllFields(\'repository_ids\');"/><input type="hidden" name="select_all_repositories_checkbox" value="true"/><b>Select/unselect all repositories</b>\n            </div>\n            <div style="clear: both"></div>\n            <div class="form-row">\n                ')
        # SOURCE LINE 40
        __M_writer(unicode(repositories_select_field.get_html()))
        __M_writer(u'\n            </div>\n            <div style="clear: both"></div>\n            <div class="form-row">\n                <input type="submit" name="reset_metadata_on_selected_repositories_button" value="Reset metadata on selected repositories"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f82b82edc90')._populate(_import_ns, [u'common_misc_javascripts'])
        _mako_get_namespace(context, '__anon_0x7f82b82ed850')._populate(_import_ns, [u'render_msg'])
        common_misc_javascripts = _import_ns.get('common_misc_javascripts', context.get('common_misc_javascripts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    ')
        # SOURCE LINE 6
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(common_misc_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


