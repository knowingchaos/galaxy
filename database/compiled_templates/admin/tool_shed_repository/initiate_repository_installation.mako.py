# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384082599.936492
_template_filename='templates/admin/tool_shed_repository/initiate_repository_installation.mako'
_template_uri='admin/tool_shed_repository/initiate_repository_installation.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['repository_installation_javascripts', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f1ba0049dd0', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1ba0049dd0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba0049dd0')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        tool_shed_repositories = _import_ns.get('tool_shed_repositories', context.get('tool_shed_repositories', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        if tool_shed_repositories:
            # SOURCE LINE 35
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">Monitor installing tool shed repositories</div>\n        <div class="toolFormBody">\n            <table class="grid">\n                <tr>\n                    <td>Name</td>\n                    <td>Description</td>\n                    <td>Owner</td>\n                    <td>Revision</td>\n                    <td>Status</td>\n                </tr>\n')
            # SOURCE LINE 46
            for tool_shed_repository in tool_shed_repositories:
                # SOURCE LINE 47
                __M_writer(u'                    ')

                encoded_repository_id = trans.security.encode_id( tool_shed_repository.id )
                ids_of_tool_dependencies_missing_or_being_installed = [ trans.security.encode_id( td.id ) for td in tool_shed_repository.tool_dependencies_missing_or_being_installed ]
                link_to_manage_tool_dependencies = tool_shed_repository.status in [ trans.model.ToolShedRepository.installation_status.INSTALLING_TOOL_DEPENDENCIES ]
                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['td','ids_of_tool_dependencies_missing_or_being_installed','link_to_manage_tool_dependencies','encoded_repository_id'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 51
                __M_writer(u'\n                    <tr>\n                        <td>\n')
                # SOURCE LINE 54
                if link_to_manage_tool_dependencies:
                    # SOURCE LINE 55
                    __M_writer(u'                                <a class="view-info" href="')
                    __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_tool_dependencies', tool_dependency_ids=ids_of_tool_dependencies_missing_or_being_installed )))
                    __M_writer(u'">\n                                    ')
                    # SOURCE LINE 56
                    __M_writer(unicode(tool_shed_repository.name))
                    __M_writer(u'\n                                </a>\n')
                    # SOURCE LINE 58
                else:
                    # SOURCE LINE 59
                    __M_writer(u'                                <a class="view-info" href="')
                    __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=encoded_repository_id )))
                    __M_writer(u'">\n                                    ')
                    # SOURCE LINE 60
                    __M_writer(unicode(tool_shed_repository.name))
                    __M_writer(u'\n                                </a>\n')
                    pass
                # SOURCE LINE 63
                __M_writer(u'                        </td>\n                        <td>')
                # SOURCE LINE 64
                __M_writer(unicode(tool_shed_repository.description))
                __M_writer(u'</td>\n                        <td>')
                # SOURCE LINE 65
                __M_writer(unicode(tool_shed_repository.owner))
                __M_writer(u'</td>\n                        <td>')
                # SOURCE LINE 66
                __M_writer(unicode(tool_shed_repository.changeset_revision))
                __M_writer(u'</td>\n                        <td><div id="RepositoryStatus-')
                # SOURCE LINE 67
                __M_writer(unicode(encoded_repository_id))
                __M_writer(u'">')
                __M_writer(unicode(tool_shed_repository.status))
                __M_writer(u'</div></td>\n                    </tr>\n')
                pass
            # SOURCE LINE 70
            __M_writer(u'            </table>\n            <br clear="left"/>\n        </div>\n    </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_repository_installation_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba0049dd0')._populate(_import_ns, [u'*'])
        reinstalling = _import_ns.get('reinstalling', context.get('reinstalling', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        initiate_repository_installation_ids = _import_ns.get('initiate_repository_installation_ids', context.get('initiate_repository_installation_ids', UNDEFINED))
        encoded_kwd = _import_ns.get('encoded_kwd', context.get('encoded_kwd', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n    <script type="text/javascript">\n        $(document).ready(function( ){\n            initiate_repository_installation( "')
        # SOURCE LINE 14
        __M_writer(unicode(initiate_repository_installation_ids))
        __M_writer(u'", "')
        __M_writer(unicode(encoded_kwd))
        __M_writer(u'", "')
        __M_writer(unicode(reinstalling))
        __M_writer(u'" );\n        });\n        var initiate_repository_installation = function ( iri_ids, encoded_kwd, reinstalling ) {\n            // Make ajax call\n            $.ajax( {\n                type: "POST",\n                url: "')
        # SOURCE LINE 20
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repositories' )))
        __M_writer(u'",\n                dataType: "html",\n                data: { operation: "install", tool_shed_repository_ids: iri_ids, encoded_kwd: encoded_kwd, reinstalling: reinstalling },\n                success : function ( data ) {\n                    //alert( "Initializing repository installation succeeded" );\n                },\n                error: function() {\n                    alert( "Initializing repository installation failed" );\n                },\n            });\n        };\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1ba0049dd0')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        repository_installation_status_updater = _import_ns.get('repository_installation_status_updater', context.get('repository_installation_status_updater', UNDEFINED))
        repository_installation_updater = _import_ns.get('repository_installation_updater', context.get('repository_installation_updater', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n   ')
        # SOURCE LINE 5
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n   ')
        # SOURCE LINE 6
        __M_writer(unicode(repository_installation_status_updater()))
        __M_writer(u'\n   ')
        # SOURCE LINE 7
        __M_writer(unicode(repository_installation_updater()))
        __M_writer(u'\n   ')
        # SOURCE LINE 8
        __M_writer(unicode(self.repository_installation_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


