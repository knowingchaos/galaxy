# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383491729.91607
_template_filename=u'templates/webapps/tool_shed/common/common.mako'
_template_uri=u'/webapps/tool_shed/common/common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_review_comment', 'render_star_rating', 'common_misc_javascripts', 'render_long_description']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'\n\n')
        # SOURCE LINE 91
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_review_comment(context,comment_text):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n    <style type="text/css">\n        #reviews_table{ table-layout:fixed;\n                        width:100%;\n                        overflow-wrap:normal;\n                        overflow:hidden;\n                        border:0px; \n                        word-break:keep-all;\n                        word-wrap:break-word;\n                        line-break:strict; }\n    </style>\n    <table id="reviews_table">\n        <tr><td>')
        # SOURCE LINE 89
        __M_writer(unicode(comment_text))
        __M_writer(u'</td></tr>\n    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_star_rating(context,name,rating,disabled=False):
    context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n    ')
        # SOURCE LINE 42

        if disabled:
            disabled_str = ' disabled="disabled"'
        else:
            disabled_str = ''
        html = ''
        for index in range( 1, 6 ):
            html += '<input name="%s" type="radio" class="star" value="%s" %s' % ( str( name ), str( index ), disabled_str )
            if rating > ( index - 0.5 ) and rating < ( index + 0.5 ):
                html += ' checked="checked"'
            html += '/>'
            
        
        # SOURCE LINE 53
        __M_writer(u'\n    ')
        # SOURCE LINE 54
        __M_writer(unicode(html))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_common_misc_javascripts(context,element_id=None):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    <script type="text/javascript">\n        function checkAllFields( name, element_id=element_id )\n        {\n            if ( element_id )\n            {\n                chkAll = document.getElementById( element_id );\n            }\n            else\n            {\n                var chkAll = document.getElementById( \'checkAll\' );\n            }\n            var checks = document.getElementsByTagName( \'input\' );\n            var boxLength = checks.length;\n            var allChecked = false;\n            var totalChecked = 0;\n            if ( chkAll.checked == true )\n            {\n                for ( i=0; i < boxLength; i++ )\n                {\n                    if ( checks[i].name.indexOf( name ) != -1 )\n                    {\n                       checks[i].checked = true;\n                    }\n                }\n            }\n            else\n            {\n                for ( i=0; i < boxLength; i++ )\n                {\n                    if ( checks[i].name.indexOf( name ) != -1 )\n                    {\n                       checks[i].checked = false\n                    }\n                }\n            }\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_long_description(context,description_text):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n    <style type="text/css">\n        #description_table{ table-layout:fixed;\n                            width:100%;\n                            overflow-wrap:normal;\n                            overflow:hidden;\n                            border:0px; \n                            word-break:keep-all;\n                            word-wrap:break-word;\n                            line-break:strict; }\n    </style>\n    <div class="form-row">\n        <label>Detailed description:</label>\n        <table id="description_table">\n            <tr><td>')
        # SOURCE LINE 71
        __M_writer(unicode(description_text))
        __M_writer(u'</td></tr>\n        </table>\n        <div style="clear: both"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


