# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383550959.0389481
_template_filename='templates/webapps/tool_shed/repository/browse_repository.mako'
_template_uri='/webapps/tool_shed/repository/browse_repository.mako'
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
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x88e2e50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x88e2e50')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7ee9750', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ee9750')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x8a2fd90', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x8a2fd90')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x88e21d0', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/repository_actions_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x88e21d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x88e2e50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7ee9750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x8a2fd90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x88e21d0')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_clone_str = _import_ns.get('render_clone_str', context.get('render_clone_str', UNDEFINED))
        render_repository_type_select_field = _import_ns.get('render_repository_type_select_field', context.get('render_repository_type_select_field', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        render_tool_shed_repository_actions = _import_ns.get('render_tool_shed_repository_actions', context.get('render_tool_shed_repository_actions', UNDEFINED))
        is_malicious = _import_ns.get('is_malicious', context.get('is_malicious', UNDEFINED))
        repository_type_select_field = _import_ns.get('repository_type_select_field', context.get('repository_type_select_field', UNDEFINED))
        commit_message = _import_ns.get('commit_message', context.get('commit_message', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
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

        is_new = repository.is_new( trans.app )
        can_push = trans.app.security_agent.can_push( trans.app, trans.user, repository )
        can_download = not is_new and ( not is_malicious or can_push )
        can_browse_contents = not is_new
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['can_push','can_browse_contents','is_new','can_download'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        __M_writer(unicode(render_tool_shed_repository_actions( repository )))
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        if message:
            # SOURCE LINE 37
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 39
        __M_writer(u'\n')
        # SOURCE LINE 40
        if can_browse_contents:
            # SOURCE LINE 41
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">Repository \'')
            # SOURCE LINE 42
            __M_writer(filters.html_escape(unicode(repository.name )))
            __M_writer(u"' revision ")
            __M_writer(filters.html_escape(unicode(repository.tip( trans.app ) )))
            __M_writer(u' (repository tip)</div>\n')
            # SOURCE LINE 43
            if can_download:
                # SOURCE LINE 44
                __M_writer(u'            <div class="form-row">\n                <label>Clone this repository:</label>\n                ')
                # SOURCE LINE 46
                __M_writer(unicode(render_clone_str( repository )))
                __M_writer(u'\n            </div>\n')
                pass
            # SOURCE LINE 49
            __M_writer(u'        <form name="repository_type">\n            ')
            # SOURCE LINE 50
            __M_writer(unicode(render_repository_type_select_field( repository_type_select_field, render_help=False )))
            __M_writer(u'\n        </form>\n')
            # SOURCE LINE 52
            if can_push:
                # SOURCE LINE 53
                __M_writer(u'            <form name="select_files_to_delete" id="select_files_to_delete" action="')
                __M_writer(unicode(h.url_for( controller='repository', action='select_files_to_delete', id=trans.security.encode_id( repository.id ))))
                __M_writer(u'" method="post" >\n                <div class="form-row" >\n                    <label>Contents:</label>\n                    <div id="tree" >\n                        Loading...\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        Click on a file to display it\'s contents below.  You may delete files from the repository by clicking the check box next to each file and clicking the <b>Delete selected files</b> button.\n                    </div>\n                    <input id="selected_files_to_delete" name="selected_files_to_delete" type="hidden" value=""/>\n                </div>\n                <div class="form-row">\n                    <label>Message:</label>\n                    <div class="form-row-input">\n')
                # SOURCE LINE 67
                if commit_message:
                    # SOURCE LINE 68
                    __M_writer(u'                            <textarea name="commit_message" rows="3" cols="35">')
                    __M_writer(filters.html_escape(unicode(commit_message )))
                    __M_writer(u'</textarea>\n')
                    # SOURCE LINE 69
                else:
                    # SOURCE LINE 70
                    __M_writer(u'                            <textarea name="commit_message" rows="3" cols="35"></textarea>\n')
                    pass
                # SOURCE LINE 72
                __M_writer(u'                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        This is the commit message for the mercurial change set that will be created if you delete selected files.\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" name="select_files_to_delete_button" value="Delete selected files"/>\n                </div>\n                <div class="form-row">\n                    <div id="file_contents" class="toolParamHelp" style="clear: both;background-color:#FAFAFA;"></div>\n                </div>\n            </form>\n')
                # SOURCE LINE 85
            else:
                # SOURCE LINE 86
                __M_writer(u'            <div class="toolFormBody">\n                <div class="form-row" >\n                    <label>Contents:</label>\n                    <div id="tree" >\n                        Loading...\n                    </div>\n                </div>\n                <div class="form-row">\n                    <div id="file_contents" class="toolParamHelp" style="clear: both;background-color:#FAFAFA;"></div>\n                </div>\n            </div>\n')
                pass
            # SOURCE LINE 98
            __M_writer(u'    </div>\n    <p/>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x88e2e50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7ee9750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x8a2fd90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x88e21d0')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n    ')
        # SOURCE LINE 17
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(unicode(h.css( "jquery.rating", "dynatree_skin/ui.dynatree" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x88e2e50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7ee9750')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x8a2fd90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x88e21d0')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        common_javascripts = _import_ns.get('common_javascripts', context.get('common_javascripts', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\n    ')
        # SOURCE LINE 22
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 23
        __M_writer(unicode(h.js( "libs/jquery/jquery.rating", "libs/jquery/jquery-ui", "libs/jquery/jquery.cookie", "libs/jquery/jquery.dynatree" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 24
        __M_writer(unicode(common_javascripts(repository)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


