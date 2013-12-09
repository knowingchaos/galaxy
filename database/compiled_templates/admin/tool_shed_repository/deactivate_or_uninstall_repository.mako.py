# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384082660.029283
_template_filename='templates/admin/tool_shed_repository/deactivate_or_uninstall_repository.mako'
_template_uri='/admin/tool_shed_repository/deactivate_or_uninstall_repository.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x7f1ba064c210', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba064c210')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f1ba0641cd0', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba0641cd0')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7f1ba0641450', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/repository_actions_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba0641450')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba064c210')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f1ba0641cd0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f1ba0641450')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        remove_from_disk_check_box = _import_ns.get('remove_from_disk_check_box', context.get('remove_from_disk_check_box', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        render_galaxy_repository_actions = _import_ns.get('render_galaxy_repository_actions', context.get('render_galaxy_repository_actions', UNDEFINED))
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
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(unicode(render_galaxy_repository_actions( repository )))
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        if message:
            # SOURCE LINE 9
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 11
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">')
        # SOURCE LINE 13
        __M_writer(unicode(repository.name))
        __M_writer(u'</div>\n    <div class="toolFormBody">\n        <form name="deactivate_or_uninstall_repository" id="deactivate_or_uninstall_repository" action="')
        # SOURCE LINE 15
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='deactivate_or_uninstall_repository', id=trans.security.encode_id( repository.id ) )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Description:</label>\n                ')
        # SOURCE LINE 18
        __M_writer(unicode(repository.description))
        __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Revision:</label>\n                ')
        # SOURCE LINE 23
        __M_writer(unicode(repository.changeset_revision))
        __M_writer(u'</a>\n            </div>\n            <div class="form-row">\n                <label>Tool shed:</label>\n                ')
        # SOURCE LINE 27
        __M_writer(unicode(repository.tool_shed))
        __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Owner:</label>\n                ')
        # SOURCE LINE 32
        __M_writer(unicode(repository.owner))
        __M_writer(u'\n            </div>\n            <div class="form-row">\n                <label>Deleted:</label>\n                ')
        # SOURCE LINE 36
        __M_writer(unicode(repository.deleted))
        __M_writer(u'\n            </div>\n            <div class="form-row">\n')
        # SOURCE LINE 39
        if repository.can_deactivate:
            # SOURCE LINE 40
            __M_writer(u'                    ')
            deactivate_uninstall_button_text = "Deactivate or Uninstall" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['deactivate_uninstall_button_text'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n                    ')
            # SOURCE LINE 41
            __M_writer(unicode(remove_from_disk_check_box.get_html()))
            __M_writer(u'\n                    <label for="repository" style="display: inline;font-weight:normal;">Check to uninstall or leave blank to deactivate</label>\n                    <br/><br/>\n                    <label>Deactivating this repository will result in the following:</label>\n                    <div class="toolParamHelp" style="clear: both;">\n                            * The repository and all of it\'s contents will remain on disk.\n                    </div>\n')
            # SOURCE LINE 48
            if repository.includes_tools_for_display_in_tool_panel:
                # SOURCE LINE 49
                __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s tools will not be loaded into the tool panel.\n                        </div>\n')
                pass
            # SOURCE LINE 53
            if repository.includes_tool_dependencies:
                # SOURCE LINE 54
                __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s installed tool dependencies will remain on disk.\n                        </div>\n')
                pass
            # SOURCE LINE 58
            if repository.includes_datatypes:
                # SOURCE LINE 59
                __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s datatypes, datatype converters and display applications will be eliminated from the datatypes registry.\n                        </div>\n')
                pass
            # SOURCE LINE 63
            __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        * The repository record\'s deleted column in the tool_shed_repository database table will be set to True.\n                    </div>\n                    <br/>\n')
            # SOURCE LINE 67
        else:
            # SOURCE LINE 68
            __M_writer(u'                    ')
            deactivate_uninstall_button_text = "Uninstall" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['deactivate_uninstall_button_text'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            # SOURCE LINE 70
            __M_writer(u'                    <input type="hidden" name="remove_from_disk" value="true"/><input type="hidden" name="remove_from_disk" value="true"/>\n')
            pass
        # SOURCE LINE 72
        __M_writer(u'                <label>Uninstalling this repository will result in the following:</label>\n                <div class="toolParamHelp" style="clear: both;">\n                    * The repository and all of it\'s contents will be removed from disk.\n                </div>\n')
        # SOURCE LINE 76
        if repository.includes_tools_for_display_in_tool_panel:
            # SOURCE LINE 77
            __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        * The repository\'s tool tag sets will be removed from the tool config file in which they are defined.\n                    </div>\n')
            pass
        # SOURCE LINE 81
        if repository.includes_tool_dependencies:
            # SOURCE LINE 82
            __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        * The repository\'s installed tool dependencies will be removed from disk.\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        * Each associated tool dependency record\'s status column in the tool_dependency database table will be set to \'Uninstalled\'.\n                    </div>\n')
            pass
        # SOURCE LINE 89
        if repository.includes_datatypes:
            # SOURCE LINE 90
            __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        * The repository\'s datatypes, datatype converters and display applications will be eliminated from the datatypes registry.\n                    </div>\n')
            pass
        # SOURCE LINE 94
        __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    * The repository record\'s deleted column in the tool_shed_repository database table will be set to True.\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    * The repository record\'s uninstalled column in the tool_shed_repository database table will be set to True.\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="deactivate_or_uninstall_repository_button" value="')
        # SOURCE LINE 103
        __M_writer(unicode(deactivate_uninstall_button_text))
        __M_writer(u'"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


