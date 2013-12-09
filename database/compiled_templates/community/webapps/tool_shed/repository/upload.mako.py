# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383539800.5598791
_template_filename='templates/webapps/tool_shed/repository/upload.mako'
_template_uri='/webapps/tool_shed/repository/upload.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts']


# SOURCE LINE 9

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
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7f729407d950', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f729407d950')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f729407ddd0', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f729407ddd0')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f729407df90', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/common/repository_actions_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f729407df90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f729407d950')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f729407ddd0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f729407df90')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        uncompress_file = _import_ns.get('uncompress_file', context.get('uncompress_file', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        render_tool_shed_repository_actions = _import_ns.get('render_tool_shed_repository_actions', context.get('render_tool_shed_repository_actions', UNDEFINED))
        commit_message = _import_ns.get('commit_message', context.get('commit_message', UNDEFINED))
        remove_repo_files_not_in_tar = _import_ns.get('remove_repo_files_not_in_tar', context.get('remove_repo_files_not_in_tar', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 5

        is_new = repository.is_new( trans.app )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_new'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 7
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(u'\n\n')
        # SOURCE LINE 17
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        if message:
            # SOURCE LINE 38
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        __M_writer(unicode(render_tool_shed_repository_actions( repository=repository)))
        __M_writer(u'\n\n<div class="toolForm">\n    <div class="toolFormTitle">Repository \'')
        # SOURCE LINE 44
        __M_writer(filters.html_escape(unicode(repository.name )))
        __M_writer(u'\'</div>\n    <div class="toolFormBody">\n        <div class="form-row">\n            <div class="warningmessage">\n                Upload a single file or tarball.  Uploading may take a while, depending upon the size of the file.\n                Wait until a message is displayed in your browser after clicking the <b>Upload</b> button below.\n            </div>\n            <div style="clear: both"></div>\n        </div>\n        <form id="upload_form" name="upload_form" action="')
        # SOURCE LINE 53
        __M_writer(unicode(h.url_for( controller='upload', action='upload', repository_id=trans.security.encode_id( repository.id ) )))
        __M_writer(u'" enctype="multipart/form-data" method="post">\n            <div class="form-row">\n                <label>File:</label>\n                <div class="form-row-input">\n                    <input type="file" name="file_data"/>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Url:</label>\n                <div class="form-row-input">\n                    <input name="url" type="textfield" value="')
        # SOURCE LINE 64
        __M_writer(filters.html_escape(unicode(url )))
        __M_writer(u'" size="40"/>\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                     Enter a url to upload your files.  In addition to http and ftp urls, urls that point to mercurial repositories (urls that start\n                     with hg:// or hgs://) are allowed.  This mechanism results in the tip revision of an external mercurial repository being added\n                     to the tool shed repository as a single new changeset.  The revision history of the originating external mercurial repository is\n                     not uploaded to the tool shed repository.\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                ')
        # SOURCE LINE 75

        if uncompress_file:
            yes_selected = 'selected'
            no_selected = ''
        else:
            yes_selected = ''
            no_selected = 'selected'
                        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['no_selected','yes_selected'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 82
        __M_writer(u'\n                <label>Uncompress files?</label>\n                <div class="form-row-input">\n                    <select name="uncompress_file">\n                        <option value="true" ')
        # SOURCE LINE 86
        __M_writer(unicode(yes_selected))
        __M_writer(u'>Yes\n                        <option value="false" ')
        # SOURCE LINE 87
        __M_writer(unicode(no_selected))
        __M_writer(u'>No\n                    </select>\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    Supported compression types are gz and bz2.  If <b>Yes</b> is selected, the uploaded file will be uncompressed.  However,\n                    if the uploaded file is an archive that contains compressed files, the contained files will not be uncompressed.  For\n                    example, if the uploaded compressed file is some_file.tar.gz, some_file.tar will be uncompressed and extracted, but if\n                    some_file.tar contains some_contained_file.gz, the contained file will not be uncompressed.\n                </div>\n            </div>\n')
        # SOURCE LINE 97
        if not is_new:
            # SOURCE LINE 98
            __M_writer(u'                <div class="form-row">\n                    ')
            # SOURCE LINE 99

            if remove_repo_files_not_in_tar:
                yes_selected = 'selected'
                no_selected = ''
            else:
                yes_selected = ''
                no_selected = 'selected'
                                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['no_selected','yes_selected'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 106
            __M_writer(u'\n                    <label>Remove files in the repository (relative to the root or selected upload point) that are not in the uploaded archive?</label>\n                    <div class="form-row-input">\n                        <select name="remove_repo_files_not_in_tar">\n                            <option value="true" ')
            # SOURCE LINE 110
            __M_writer(unicode(yes_selected))
            __M_writer(u'>Yes\n                            <option value="false" ')
            # SOURCE LINE 111
            __M_writer(unicode(no_selected))
            __M_writer(u'>No\n                        </select>\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        This selection pertains only to uploaded tar archives, not to single file uploads.  If <b>Yes</b> is selected, files\n                        that exist in the repository (relative to the root or selected upload point) but that are not in the uploaded archive\n                        will be removed from the repository.  Otherwise, all existing repository files will remain and the uploaded archive\n                        files will be added to the repository.\n                    </div>\n                </div>\n')
            pass
        # SOURCE LINE 122
        __M_writer(u'            <div class="form-row">\n                <label>Change set commit message:</label>\n                <div class="form-row-input">\n')
        # SOURCE LINE 125
        if commit_message:
            # SOURCE LINE 126
            __M_writer(u'                        <pre><textarea name="commit_message" rows="3" cols="35">')
            __M_writer(filters.html_escape(unicode(commit_message )))
            __M_writer(u'</textarea></pre>\n')
            # SOURCE LINE 127
        else:
            # SOURCE LINE 128
            __M_writer(u'                        <textarea name="commit_message" rows="3" cols="35"></textarea>\n')
            pass
        # SOURCE LINE 130
        __M_writer(u'                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    This is the commit message for the mercurial change set that will be created by this upload.\n                </div>\n                <div style="clear: both"></div>\n            </div>\n')
        # SOURCE LINE 136
        if not repository.is_new( trans.app ):
            # SOURCE LINE 137
            __M_writer(u'                <div class="form-row" >\n                    <label>Contents:</label>\n                    <div id="tree" >\n                        Loading...\n                    </div>\n                    <input type="hidden" id="upload_point" name="upload_point" value=""/>\n                    <div class="toolParamHelp" style="clear: both;">\n                        Select a location within the repository to upload your files by clicking a check box next to the location.  The \n                        selected location is considered the upload point.  If a location is not selected, the upload point will be the \n                        repository root.\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n')
            pass
        # SOURCE LINE 151
        __M_writer(u'            <div class="form-row">\n                <input type="submit" class="primary-button" name="upload_button" value="Upload">\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f729407d950')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f729407ddd0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f729407df90')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n    ')
        # SOURCE LINE 20
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 21
        __M_writer(unicode(h.css( "libs/jquery/jquery.rating", "dynatree_skin/ui.dynatree" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f729407d950')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f729407ddd0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f729407df90')._populate(_import_ns, [u'render_tool_shed_repository_actions'])
        common_javascripts = _import_ns.get('common_javascripts', context.get('common_javascripts', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n    ')
        # SOURCE LINE 25
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 26
        __M_writer(unicode(h.js( "libs/jquery/jquery-ui", "libs/jquery/jquery.cookie", "libs/jquery/jquery.dynatree" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 27
        __M_writer(unicode(common_javascripts(repository)))
        __M_writer(u'\n    <script type="text/javascript">\n    $( function() {\n        $( "select[refresh_on_change=\'true\']").change( function() {\n            $( "#upload_form" ).submit();\n        });\n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


