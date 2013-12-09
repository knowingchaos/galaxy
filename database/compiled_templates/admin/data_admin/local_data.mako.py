# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384254540.7863779
_template_filename='templates/admin/data_admin/local_data.mako'
_template_uri='/admin/data_admin/local_data.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'init', 'javascripts', 'center_panel']


# SOURCE LINE 5

def inherit(context):
    if context.get('use_panels'):
        return '/webapps/galaxy/base_panels.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x70052d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x70052d0')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7005ed0', context._clean_inheritance_tokens(), templateuri=u'/library/common/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7005ed0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x70052d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7005ed0')._populate(_import_ns, [u'common_javascripts'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        styles = _import_ns.get('styles', context.get('styles', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        jobgrid = _import_ns.get('jobgrid', context.get('jobgrid', UNDEFINED))
        labels = _import_ns.get('labels', context.get('labels', UNDEFINED))
        indexfuncs = _import_ns.get('indexfuncs', context.get('indexfuncs', UNDEFINED))
        dbkeys = _import_ns.get('dbkeys', context.get('dbkeys', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        indextable = _import_ns.get('indextable', context.get('indextable', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 41
        __M_writer(u'\n<style type="text/css">\n    .params-block { display: none; }\n    td, th { padding-left: 10px; padding-right: 10px; }\n    td.state-color-new { text-decoration: underline; }\n    td.panel-done-message { background-image: none; padding: 0px 10px 0px 10px; }\n    td.panel-error-message { background-image: none; padding: 0px 10px 0px 10px; }\n</style>\n<div class="toolForm">\n')
        # SOURCE LINE 50
        if message:
            # SOURCE LINE 51
            __M_writer(u'        <div class="')
            __M_writer(unicode(status))
            __M_writer(u'">')
            __M_writer(unicode(message))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 53
        __M_writer(u'    <div class="toolFormTitle">Currently tracked builds <a class="action-button" href="')
        __M_writer(unicode(h.url_for( controller='data_admin', action='add_genome' )))
        __M_writer(u'">Add new</a></div>\n    <div class="toolFormBody">\n        <h2>Locally cached data:</h2>\n        <h3>NOTE: Indexes generated here will not be reflected in the table until Galaxy is restarted.</h3>\n        <table id="locfiles">\n            <tr>\n                <th>DB Key</th>\n                <th>Name</th>\n')
        # SOURCE LINE 61
        for label in labels:
            # SOURCE LINE 62
            __M_writer(u'                    <th>')
            __M_writer(unicode(labels[label]))
            __M_writer(u'</th>\n')
            pass
        # SOURCE LINE 64
        __M_writer(u'            </tr>\n')
        # SOURCE LINE 65
        for dbkey in sorted(dbkeys):
            # SOURCE LINE 66
            __M_writer(u'                <tr>\n                    <td>')
            # SOURCE LINE 67
            __M_writer(unicode(dbkey))
            __M_writer(u'</td>\n                    <td>')
            # SOURCE LINE 68
            __M_writer(unicode(indextable[dbkey]['name']))
            __M_writer(u'</td>\n')
            # SOURCE LINE 69
            for label in labels:
                # SOURCE LINE 70
                __M_writer(u'                        <td id="')
                __M_writer(unicode(dbkey))
                __M_writer(u'-')
                __M_writer(unicode(indexfuncs[label]))
                __M_writer(u'" class="indexcell ')
                __M_writer(unicode(styles[indextable[dbkey]['indexes'][label]]))
                __M_writer(u'" data-fapath="')
                __M_writer(unicode(indextable[dbkey]['path']))
                __M_writer(u'" data-longname="')
                __M_writer(unicode(indextable[dbkey]['name']))
                __M_writer(u'" data-index="')
                __M_writer(unicode(indexfuncs[label]))
                __M_writer(u'" data-dbkey="')
                __M_writer(unicode(dbkey))
                __M_writer(u'">')
                __M_writer(unicode(indextable[dbkey]['indexes'][label]))
                __M_writer(u'</td>\n')
                pass
            # SOURCE LINE 72
            __M_writer(u'\n                </tr>\n')
            pass
        # SOURCE LINE 75
        __M_writer(u'        </table>\n        <h2>Recent jobs:</h2>\n        <p>Click the job ID to see job details and the status of any individual sub-jobs. Note that this list only shows jobs initiated by your account.</p>\n        <div id="recentJobs">\n')
        # SOURCE LINE 79
        for job in jobgrid:
            # SOURCE LINE 80
            __M_writer(u'            <div id="job-')
            __M_writer(unicode(job['deferred']))
            __M_writer(u'" data-dbkey="')
            __M_writer(unicode(job['dbkey']))
            __M_writer(u'" data-name="')
            __M_writer(unicode(job['intname']))
            __M_writer(u'" data-indexes="')
            __M_writer(unicode(job['indexers']))
            __M_writer(u'" data-jobid="')
            __M_writer(unicode(job['deferred']))
            __M_writer(u'" data-state="')
            __M_writer(unicode(job['state']))
            __M_writer(u'" class="historyItem-')
            __M_writer(unicode(job['state']))
            __M_writer(u' historyItemWrapper historyItem">\n                <p>Job ID <a href="')
            # SOURCE LINE 81
            __M_writer(unicode(h.url_for( controller='data_admin', action='monitor_status', job=job['deferred'] )))
            __M_writer(u'">')
            __M_writer(unicode(job['deferred']))
            __M_writer(u'</a>:\n')
            # SOURCE LINE 82
            if job['jobtype'] == 'download':
                # SOURCE LINE 83
                __M_writer(u'                    Download <em>')
                __M_writer(unicode(job['intname']))
                __M_writer(u'</em>\n')
                # SOURCE LINE 84
                if job['indexers']:
                    # SOURCE LINE 85
                    __M_writer(u'                    and index with ')
                    __M_writer(unicode(job['indexers']))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 87
            else:
                # SOURCE LINE 88
                __M_writer(u'                    Index <em>')
                __M_writer(unicode(job['intname']))
                __M_writer(u'</em> with ')
                __M_writer(unicode(job['indexers']))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 90
            __M_writer(u'                </p>\n            </div>\n')
            pass
        # SOURCE LINE 93
        __M_writer(u'        </div>\n</div>\n<script type="text/javascript">\n    finalstates = new Array(\'done\', \'error\', \'ok\');\n    $(\'.indexcell\').click(function() {\n        status = $(this).html();\n        elem = $(this);\n        if (status != \'Generate\') {\n            return;\n        }\n        longname = $(this).attr(\'data-longname\');\n        dbkey = $(this).attr(\'data-dbkey\');\n        indexes = $(this).attr(\'data-index\');\n        path = $(this).attr(\'data-fapath\');\n        $.post(\'')
        # SOURCE LINE 107
        __M_writer(unicode(h.url_for( controller='data_admin', action='index_build' )))
        __M_writer(u'\', { longname: longname, dbkey: dbkey, indexes: indexes, path: path }, function(data) {\n            if (data == \'ERROR\') {\n                alert(\'There was an error.\');\n            }\n            else {\n                elem.html(\'Generating\');\n                elem.attr(\'class\', \'indexcell state-color-running\');\n            }\n            newhtml = \'<div data-dbkey="\' + dbkey + \'" data-name="\' + longname + \'" data-indexes="\' + indexes + \'" id="job-\' + data + \'" class="historyItem-new historyItemWrapper historyItem">\' +\n                \'<p>Job ID <a href="')
        # SOURCE LINE 116
        __M_writer(unicode(h.url_for( controller='data_admin', action='monitor_status')))
        __M_writer(u'?job=\' + data + \'">\' + data + \'</a>: \' +\n                \'Index <em>\' + longname + \'</em> with \' + indexes + \'</p></div>\';\n            $(\'#recentJobs\').prepend(newhtml);\n            $(\'#job-\' + data).delay(3000).queue(function(n) {\n                checkJob(data);\n                n();\n            });\n        });\n    });\n    \n    function checkJob(jobid) {\n        $.get(\'')
        # SOURCE LINE 127
        __M_writer(unicode(h.url_for( controller='data_admin', action='get_jobs' )))
        __M_writer(u'\', { jobid: jobid }, function(data) {\n            jsondata = JSON.parse(data)[0];\n            jsondata["name"] = $(\'#job-\' + jobid).attr(\'data-name\');\n            jsondata["dbkey"] = $(\'#job-\' + jobid).attr(\'data-dbkey\');\n            jsondata["indexes"] = $(\'#job-\' + jobid).attr(\'data-indexes\');\n            tdid = jq(jsondata["dbkey"] + \'-\' + jsondata["indexes"]);\n            newhtml = makeNewHTML(jsondata);\n            $(\'#job-\' + jobid).replaceWith(newhtml);\n            if ($.inArray(jsondata["status"], finalstates) == -1) {\n                $(\'#job-\' + jobid).delay(3000).queue(function(n) {\n                    checkJob(jobid);\n                    n();\n                });\n            }\n            if (jsondata["status"] == \'done\' || jsondata["status"] == \'ok\') {\n                elem = $(tdid);\n                elem.html(\'Generated\');\n                elem.attr(\'class\', \'indexcell panel-done-message\');\n            }\n        });\n    }\n    \n    function makeNewHTML(jsondata) {\n        newhtml = \'<div data-dbkey="\' + jsondata["dbkey"] + \'" data-name="\' + jsondata["name"] + \'" data-indexes="\' + jsondata["indexes"] + \'" id="job-\' + jsondata["jobid"] + \'" class="historyItem-\' + jsondata["status"] + \' historyItemWrapper historyItem">\' +\n            \'<p>Job ID <a href="')
        # SOURCE LINE 151
        __M_writer(unicode(h.url_for( controller='data_admin', action='monitor_status')))
        __M_writer(u'?job=\' + jsondata["jobid"] + \'">\' + jsondata["jobid"] + \'</a>: \' +\n            \'Index <em>\' + jsondata["name"] + \'</em> with \' + jsondata["indexes"] + \'</p></div>\';\n        return newhtml;\n    }\n    \n    $(document).ready(function() {\n        $(\'.historyItem\').each(function() {\n            state = $(this).attr(\'data-state\');\n            jobid = $(this).attr(\'data-jobid\');\n            if ($.inArray(state, finalstates) == -1) {\n                checkJob(jobid);\n            }\n        });\n    });\n    \n    function jq(id) { \n        return \'#\' + id.replace(/(:|\\.)/g,\'\\\\$1\');\n    }\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x70052d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7005ed0')._populate(_import_ns, [u'common_javascripts'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n    ')
        # SOURCE LINE 25
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 26
        __M_writer(unicode(h.css( "autocomplete_tagging" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x70052d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7005ed0')._populate(_import_ns, [u'common_javascripts'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n')
        # SOURCE LINE 15

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        self.active_view="user"
        self.overlay_visible=False
        self.has_accessible_datasets = False
        
        
        # SOURCE LINE 22
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x70052d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7005ed0')._populate(_import_ns, [u'common_javascripts'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n    ')
        # SOURCE LINE 29
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 30
        __M_writer(unicode(h.js("libs/jquery/jquery.autocomplete", "galaxy.autocom_tagging" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x70052d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7005ed0')._populate(_import_ns, [u'common_javascripts'])
        render_content = _import_ns.get('render_content', context.get('render_content', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n   <div style="overflow: auto; height: 100%;">\n       <div class="page-container" style="padding: 10px;">\n           ')
        # SOURCE LINE 38
        __M_writer(unicode(render_content()))
        __M_writer(u'\n       </div>\n   </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


