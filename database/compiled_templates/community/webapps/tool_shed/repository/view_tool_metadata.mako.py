# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383556738.780926
_template_filename='templates/webapps/tool_shed/repository/view_tool_metadata.mako'
_template_uri='/webapps/tool_shed/repository/view_tool_metadata.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


# SOURCE LINE 15

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
    ns = runtime.TemplateNamespace('__anon_0x7f69b0543c10', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f69b0543c10')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7f69b0543b50', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f69b0543b50')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x7f69b0543d10', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/repository_actions_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f69b0543d10')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f69b0543350', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f69b0543350')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f69b0543c10')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f69b0543b50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f69b0543d10')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f69b0543350')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        revision_label = _import_ns.get('revision_label', context.get('revision_label', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        tool = _import_ns.get('tool', context.get('tool', UNDEFINED))
        render_clone_str = _import_ns.get('render_clone_str', context.get('render_clone_str', UNDEFINED))
        render_tool_shed_repository_actions = _import_ns.get('render_tool_shed_repository_actions', context.get('render_tool_shed_repository_actions', UNDEFINED))
        render_repository_actions_for = _import_ns.get('render_repository_actions_for', context.get('render_repository_actions_for', UNDEFINED))
        tool_lineage = _import_ns.get('tool_lineage', context.get('tool_lineage', UNDEFINED))
        is_malicious = _import_ns.get('is_malicious', context.get('is_malicious', UNDEFINED))
        render_galaxy_repository_actions = _import_ns.get('render_galaxy_repository_actions', context.get('render_galaxy_repository_actions', UNDEFINED))
        changeset_revision = _import_ns.get('changeset_revision', context.get('changeset_revision', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        tool_metadata_dict = _import_ns.get('tool_metadata_dict', context.get('tool_metadata_dict', UNDEFINED))
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
        # SOURCE LINE 7

        is_new = repository.is_new( trans.app )
        
        can_push = trans.app.security_agent.can_push( trans.app, trans.user, repository )
        can_download = not is_new and ( not is_malicious or can_push )
        can_view_change_log = trans.webapp.name == 'tool_shed' and not is_new
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['can_push','is_new','can_view_change_log','can_download'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 13
        __M_writer(u'\n\n')
        # SOURCE LINE 21
        __M_writer(u'\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        if render_repository_actions_for == 'tool_shed':
            # SOURCE LINE 25
            __M_writer(u'    ')
            __M_writer(unicode(render_tool_shed_repository_actions( repository=repository, changeset_revision=changeset_revision )))
            __M_writer(u'\n')
            # SOURCE LINE 26
        else:
            # SOURCE LINE 27
            __M_writer(u'    ')
            __M_writer(unicode(render_galaxy_repository_actions( repository=repository )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        if message:
            # SOURCE LINE 31
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 33
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Repository revision</div>\n    <div class="toolFormBody">\n        <div class="form-row">\n            <label>Revision:</label>\n')
        # SOURCE LINE 39
        if can_view_change_log:
            # SOURCE LINE 40
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='repository', action='view_changelog', id=trans.app.security.encode_id( repository.id ) )))
            __M_writer(u'">')
            __M_writer(unicode(revision_label))
            __M_writer(u'</a>\n')
            # SOURCE LINE 41
        else:
            # SOURCE LINE 42
            __M_writer(u'                ')
            __M_writer(unicode(revision_label))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 44
        __M_writer(u'        </div>\n    </div>\n</div>\n<p/>\n')
        # SOURCE LINE 48
        if can_download:
            # SOURCE LINE 49
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">Repository \'')
            # SOURCE LINE 50
            __M_writer(filters.html_escape(unicode(repository.name )))
            __M_writer(u'\'</div>\n        <div class="toolFormBody">\n            <div class="form-row">\n                <label>Clone this repository:</label>\n                ')
            # SOURCE LINE 54
            __M_writer(unicode(render_clone_str( repository )))
            __M_writer(u'\n            </div>\n        </div>\n    </div>\n')
            # SOURCE LINE 58
        else:
            # SOURCE LINE 59
            __M_writer(u'    <b>Repository name:</b><br/>\n    ')
            # SOURCE LINE 60
            __M_writer(unicode(repository.name))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 62
        if tool_metadata_dict:
            # SOURCE LINE 63
            __M_writer(u'    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">')
            # SOURCE LINE 65
            __M_writer(unicode(tool_metadata_dict[ 'name' ]))
            __M_writer(u' tool metadata</div>\n        <div class="toolFormBody">\n            <div class="form-row">\n                <table width="100%">\n                    <tr bgcolor="#D8D8D8" width="100%"><td><b>Miscellaneous</td></tr>\n                </table>\n            </div>\n            <div class="form-row">\n                <label>Name:</label>\n                <a href="')
            # SOURCE LINE 74
            __M_writer(unicode(h.url_for( controller='repository', action='display_tool', repository_id=trans.security.encode_id( repository.id ), tool_config=tool_metadata_dict[ 'tool_config' ], changeset_revision=changeset_revision )))
            __M_writer(u'">')
            __M_writer(unicode(tool_metadata_dict[ 'name' ]))
            __M_writer(u'</a>\n                <div style="clear: both"></div>\n            </div>\n')
            # SOURCE LINE 77
            if 'description' in tool_metadata_dict:
                # SOURCE LINE 78
                __M_writer(u'                <div class="form-row">\n                    <label>Description:</label>\n                    ')
                # SOURCE LINE 80
                __M_writer(filters.html_escape(unicode(tool_metadata_dict[ 'description' ] )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n')
                pass
            # SOURCE LINE 84
            if 'id' in tool_metadata_dict:
                # SOURCE LINE 85
                __M_writer(u'                <div class="form-row">\n                    <label>Id:</label>\n                    ')
                # SOURCE LINE 87
                __M_writer(filters.html_escape(unicode(tool_metadata_dict[ 'id' ] )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n')
                pass
            # SOURCE LINE 91
            if 'guid' in tool_metadata_dict:
                # SOURCE LINE 92
                __M_writer(u'                <div class="form-row">\n                    <label>Guid:</label>\n                    ')
                # SOURCE LINE 94
                __M_writer(filters.html_escape(unicode(tool_metadata_dict[ 'guid' ] )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n')
                pass
            # SOURCE LINE 98
            if 'version' in tool_metadata_dict:
                # SOURCE LINE 99
                __M_writer(u'                <div class="form-row">\n                    <label>Version:</label>\n                    ')
                # SOURCE LINE 101
                __M_writer(filters.html_escape(unicode(tool_metadata_dict[ 'version' ] )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n')
                pass
            # SOURCE LINE 105
            if 'version_string_cmd' in tool_metadata_dict:
                # SOURCE LINE 106
                __M_writer(u'                <div class="form-row">\n                    <label>Version command string:</label>\n                    ')
                # SOURCE LINE 108
                __M_writer(filters.html_escape(unicode(tool_metadata_dict[ 'version_string_cmd' ] )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n')
                pass
            # SOURCE LINE 112
            if 'add_to_tool_panel' in tool_metadata_dict:
                # SOURCE LINE 113
                __M_writer(u'                <div class="form-row">\n                    <label>Display in tool panel:</label>\n                    ')
                # SOURCE LINE 115
                __M_writer(filters.html_escape(unicode(tool_metadata_dict[ 'add_to_tool_panel' ] )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n')
                pass
            # SOURCE LINE 119
            __M_writer(u'            <div class="form-row">\n                <table width="100%">\n                    <tr bgcolor="#D8D8D8" width="100%"><td><b>Version lineage of this tool (guids ordered most recent to oldest)</td></tr>\n                </table>\n            </div>\n            <div class="form-row">\n')
            # SOURCE LINE 125
            if tool_lineage:
                # SOURCE LINE 126
                __M_writer(u'                    <table class="grid">\n')
                # SOURCE LINE 127
                for guid in tool_lineage:
                    # SOURCE LINE 128
                    __M_writer(u'                            <tr>\n                                <td>\n')
                    # SOURCE LINE 130
                    if guid == tool_metadata_dict[ 'guid' ]:
                        # SOURCE LINE 131
                        __M_writer(u'                                        ')
                        __M_writer(filters.html_escape(unicode(guid )))
                        __M_writer(u' <b>(this tool)</b>\n')
                        # SOURCE LINE 132
                    else:
                        # SOURCE LINE 133
                        __M_writer(u'                                        ')
                        __M_writer(filters.html_escape(unicode(guid )))
                        __M_writer(u'\n')
                        pass
                    # SOURCE LINE 135
                    __M_writer(u'                                </td>\n                            </tr>\n')
                    pass
                # SOURCE LINE 138
                __M_writer(u'                    </table>\n')
                # SOURCE LINE 139
            else:
                # SOURCE LINE 140
                __M_writer(u'                    No tool versions are defined for this tool so it is critical that you <b>Reset all repository metadata</b> from the\n                    <b>Manage repository</b> page.\n')
                pass
            # SOURCE LINE 143
            __M_writer(u'            </div>\n            <div class="form-row">\n                <table width="100%">\n                    <tr bgcolor="#D8D8D8" width="100%"><td><b>Requirements (dependencies defined in the &lt;requirements&gt; tag set)</td></tr>\n                </table>\n            </div>\n            ')
            # SOURCE LINE 149

            if 'requirements' in tool_metadata_dict:
                requirements = tool_metadata_dict[ 'requirements' ]
            else:
                requirements = None
                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['requirements'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 154
            __M_writer(u'\n')
            # SOURCE LINE 155
            if requirements:
                # SOURCE LINE 156
                __M_writer(u'                <div class="form-row">\n                    <label>Requirements:</label>\n                    <table class="grid">\n                        <tr>\n                            <td><b>name</b></td>\n                            <td><b>version</b></td>\n                            <td><b>type</b></td>\n                        </tr>\n')
                # SOURCE LINE 164
                for requirement_dict in requirements:
                    # SOURCE LINE 165
                    __M_writer(u'                            ')

                    requirement_name = requirement_dict[ 'name' ] or 'not provided'
                    requirement_version = requirement_dict[ 'version' ] or 'not provided'
                    requirement_type = requirement_dict[ 'type' ] or 'not provided'
                                                
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['requirement_version','requirement_type','requirement_name'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 169
                    __M_writer(u'\n                            <tr>\n                                <td>')
                    # SOURCE LINE 171
                    __M_writer(filters.html_escape(unicode(requirement_name )))
                    __M_writer(u'</td>\n                                <td>')
                    # SOURCE LINE 172
                    __M_writer(filters.html_escape(unicode(requirement_version )))
                    __M_writer(u'</td>\n                                <td>')
                    # SOURCE LINE 173
                    __M_writer(filters.html_escape(unicode(requirement_type )))
                    __M_writer(u'</td>\n                            </tr>\n')
                    pass
                # SOURCE LINE 176
                __M_writer(u'                    </table>\n                    <div style="clear: both"></div>\n                </div>\n')
                # SOURCE LINE 179
            else:
                # SOURCE LINE 180
                __M_writer(u'                <div class="form-row">\n                    No requirements defined\n                </div>\n')
                pass
            # SOURCE LINE 184
            if tool:
                # SOURCE LINE 185
                __M_writer(u'                <div class="form-row">\n                    <table width="100%">\n                        <tr bgcolor="#D8D8D8" width="100%"><td><b>Additional information about this tool</td></tr>\n                    </table>\n                </div>\n                <div class="form-row">\n                    <label>Command:</label>\n                    <pre>')
                # SOURCE LINE 192
                __M_writer(filters.html_escape(unicode(tool.command )))
                __M_writer(u'</pre>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <label>Interpreter:</label>\n                    ')
                # SOURCE LINE 197
                __M_writer(filters.html_escape(unicode(tool.interpreter )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <label>Is multi-byte:</label>\n                    ')
                # SOURCE LINE 202
                __M_writer(filters.html_escape(unicode(tool.is_multi_byte )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <label>Forces a history refresh:</label>\n                    ')
                # SOURCE LINE 207
                __M_writer(filters.html_escape(unicode(tool.force_history_refresh )))
                __M_writer(u'\n                    <div style="clear: both"></div>\n                </div>\n                ')
                # SOURCE LINE 210
                parallelism_info = tool.parallelism 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['parallelism_info'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                # SOURCE LINE 211
                if parallelism_info:
                    # SOURCE LINE 212
                    __M_writer(u'                    <div class="form-row">\n                        <table width="100%">\n                            <tr bgcolor="#D8D8D8" width="100%"><td><b>Parallelism</td></tr>\n                        </table>\n                    </div>\n                    <div class="form-row">\n                        <label>Method:</label>\n                        ')
                    # SOURCE LINE 219
                    __M_writer(filters.html_escape(unicode(parallelism_info.method )))
                    __M_writer(u'\n                        <div style="clear: both"></div>\n                    </div>\n')
                    # SOURCE LINE 222
                    for key, val in parallelism_info.attributes.items():
                        # SOURCE LINE 223
                        __M_writer(u'                        <div class="form-row">\n                            <label>')
                        # SOURCE LINE 224
                        __M_writer(unicode(key))
                        __M_writer(u':</label>\n                            ')
                        # SOURCE LINE 225
                        __M_writer(filters.html_escape(unicode(val )))
                        __M_writer(u'\n                            <div style="clear: both"></div>\n                        </div>\n')
                        pass
                    pass
                pass
            # SOURCE LINE 231
            __M_writer(u'            <div class="form-row">\n                <table width="100%">\n                    <tr bgcolor="#D8D8D8" width="100%"><td><b>Functional tests</td></tr>\n                </table>\n            </div>\n            ')
            # SOURCE LINE 236

            if 'tests' in tool_metadata_dict:
                tests = tool_metadata_dict[ 'tests' ]
            else:
                tests = None
                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tests'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 241
            __M_writer(u'\n')
            # SOURCE LINE 242
            if tests:
                # SOURCE LINE 243
                __M_writer(u'                <div class="form-row">\n                    <table class="grid">\n                        <tr>\n                            <td><b>name</b></td>\n                            <td><b>inputs</b></td>\n                            <td><b>outputs</b></td>\n                            <td><b>required files</b></td>\n                        </tr>\n')
                # SOURCE LINE 251
                for test_dict in tests:
                    # SOURCE LINE 252
                    __M_writer(u'                            ')

                    inputs = test_dict[ 'inputs' ]
                    outputs = test_dict[ 'outputs' ]
                    required_files = test_dict[ 'required_files' ]
                                                
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['inputs','required_files','outputs'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 256
                    __M_writer(u'\n                            <tr>\n                                <td>')
                    # SOURCE LINE 258
                    __M_writer(unicode(test_dict[ 'name' ]))
                    __M_writer(u'</td>\n                                <td>\n')
                    # SOURCE LINE 260
                    for input in inputs:
                        # SOURCE LINE 261
                        __M_writer(u'                                        <b>')
                        __M_writer(unicode(input[0]))
                        __M_writer(u':</b> ')
                        __M_writer(filters.html_escape(unicode(input[1] )))
                        __M_writer(u'<br/>\n')
                        pass
                    # SOURCE LINE 263
                    __M_writer(u'                                </td>\n                                <td>\n')
                    # SOURCE LINE 265
                    for output in outputs:
                        # SOURCE LINE 266
                        __M_writer(u'                                        <b>')
                        __M_writer(unicode(output[0]))
                        __M_writer(u':</b> ')
                        __M_writer(filters.html_escape(unicode(output[1] )))
                        __M_writer(u'<br/>\n')
                        pass
                    # SOURCE LINE 268
                    __M_writer(u'                                </td>\n                                <td>\n')
                    # SOURCE LINE 270
                    for required_file in required_files:
                        # SOURCE LINE 271
                        __M_writer(u'                                        ')
                        __M_writer(filters.html_escape(unicode(required_file )))
                        __M_writer(u'<br/>\n')
                        pass
                    # SOURCE LINE 273
                    __M_writer(u'                                </td>\n                            </tr>\n')
                    pass
                # SOURCE LINE 276
                __M_writer(u'                    </table>\n                </div>\n')
                # SOURCE LINE 278
            else:
                # SOURCE LINE 279
                __M_writer(u'                <div class="form-row">\n                    No functional tests defined\n                </div>\n')
                pass
            # SOURCE LINE 283
            __M_writer(u'        </div>\n    </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


