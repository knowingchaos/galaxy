# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383202403.987179
_template_filename=u'templates/webapps/galaxy/library/common/library_item_info.mako'
_template_uri=u'/library/common/library_item_info.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_library_item_info']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        ldda = context.get('ldda', UNDEFINED)
        def render_library_item_info(ldda):
            return render_render_library_item_info(context.locals_(__M_locals),ldda)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(unicode(render_library_item_info( ldda )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_library_item_info(context,ldda):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        if ldda.state == 'error':
            # SOURCE LINE 3
            __M_writer(u'                                <div class="libraryItem-')
            __M_writer(unicode(ldda.state))
            __M_writer(u'">Job error <i>(click name for more info)</i></div>\n')
            # SOURCE LINE 4
        elif ldda.state == 'queued':
            # SOURCE LINE 5
            __M_writer(u'                                <div class="libraryItem-')
            __M_writer(unicode(ldda.state))
            __M_writer(u'">This job is queued</div>\n')
            # SOURCE LINE 6
        elif ldda.state == 'running':
            # SOURCE LINE 7
            __M_writer(u'                                <div class="libraryItem-')
            __M_writer(unicode(ldda.state))
            __M_writer(u'">This job is running</div>\n')
            # SOURCE LINE 8
        elif ldda.state == 'upload':
            # SOURCE LINE 9
            __M_writer(u'                                <div class="libraryItem-')
            __M_writer(unicode(ldda.state))
            __M_writer(u'">This dataset is uploading</div>\n')
            # SOURCE LINE 10
        else:
            # SOURCE LINE 11
            __M_writer(u'                                ')
            __M_writer(unicode(ldda.message))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


