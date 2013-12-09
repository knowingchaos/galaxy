# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383034056.2657261
_template_filename='templates/webapps/galaxy/cloud/index.mako'
_template_uri='cloud/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'init', 'javascripts', 'center_panel']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 56
        __M_writer(u'\n\n')
        # SOURCE LINE 171
        __M_writer(u'\n\n')
        # SOURCE LINE 300
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 14
        __M_writer(unicode(h.css( "autocomplete_tagging" )))
        __M_writer(u'\n    <style type="text/css">\n    #new_history_p{\n        line-height:2.5em;\n        margin:0em 0em .5em 0em;\n    }\n    #new_history_cbx{\n        margin-right:.5em;\n    }\n    #new_history_input{\n        display:none;\n        line-height:1em;\n    }\n    #ec_button_container{\n        float:right;\n    }\n    #hidden_options{\n        display:none;\n    }\n    div.toolForm{\n        margin-top: 10px;\n        margin-bottom: 10px;\n    }\n    div.toolFormTitle{\n        cursor:pointer;\n    }\n    .title_ul_text{\n        text-decoration:underline;\n    }\n    .step-annotation {\n        margin-top: 0.25em;\n        font-weight: normal;\n        font-size: 97%;\n    }\n    .workflow-annotation {\n        margin-bottom: 1em;\n    }\n    #loading_indicator{\n            position:fixed;\n            top:40px;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="shared"
        self.message_box_visible=False
        
        
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        default_keypair = context.get('default_keypair', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\n    ')
        # SOURCE LINE 59
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n        var ACCOUNT_URL = "')
        # SOURCE LINE 61
        __M_writer(unicode(h.url_for( controller='/cloudlaunch', action='get_account_info')))
        __M_writer(u'";\n        var PKEY_DL_URL = "')
        # SOURCE LINE 62
        __M_writer(unicode(h.url_for( controller='/cloudlaunch', action='get_pkey')))
        __M_writer(u'";\n        var cloudlaunch_clusters = [];\n\n        $(document).ready(function(){\n            $(\'#id_existing_instance\').change(function(){\n                var ei_name = $(this).val();\n                if (ei_name === "New Cluster"){\n                    //For new instances, need to see the cluster name field.\n                    $(\'#id_cluster_name\').val("New Cluster")\n                    $(\'#cluster_name_wrapper\').show(\'fast\');\n                }else{\n                    //Hide the Cluster Name field, but set the value\n                    $(\'#id_cluster_name\').val($(this).val());\n                    $(\'#cluster_name_wrapper\').hide(\'fast\');\n                }\n            });\n             //When id_secret and id_key are complete, submit to get_account_info\n            $("#id_secret, #id_key_id").bind("paste input propertychange", function(){\n                secret_el = $("#id_secret");\n                key_el = $("#id_key_id");\n                if (secret_el.val().length === 40 && key_el.val().length === 20){\n                    //Submit these to get_account_info, unhide fields, and update as appropriate\n                    $.ajax({type: "POST",\n                            url: ACCOUNT_URL,\n                            dataType: \'json\',\n                            data: {key_id: key_el.val(),secret:secret_el.val()},\n                            success: function(result){\n                                    cloudlaunch_clusters = result.clusters;\n                                    var kplist = $("#id_keypair");\n                                    var clusterlist = $("#id_existing_instance");\n                                    kplist.find(\'option\').remove();\n                                    clusterlist.find(\'option\').remove();\n                                    //Update fields with appropriate elements\n                                    clusterlist.append($(\'<option/>\').val(\'New Cluster\').text(\'New Cluster\'));\n                                    if (_.size(result.clusters) > 0){\n                                        _.each(result.clusters, function(cluster, index){\n                                            clusterlist.append($(\'<option/>\').val(cluster.name).text(cluster.name));\n                                        });\n                                        $(\'#existing_instance_wrapper\').show();\n                                    }\n                                    if (!_.include(result.keypairs, \'')
        # SOURCE LINE 102
        __M_writer(unicode(default_keypair))
        __M_writer(u"')){\n                                        kplist.append($('<option/>').val('")
        # SOURCE LINE 103
        __M_writer(unicode(default_keypair))
        __M_writer(u"').text('Create New - ")
        __M_writer(unicode(default_keypair))
        __M_writer(u'\'));\n                                    }\n                                    _.each(result.keypairs, function(keypair, index){\n                                        kplist.append($(\'<option/>\').val(keypair).text(keypair));\n                                    });\n                                    $(\'#hidden_options\').show(\'fast\');\n                                }\n                            });\n                }\n            });\n            $(\'#loading_indicator\').ajaxStart(function(){\n                $(this).show(\'fast\');\n            }).ajaxStop(function(){\n                $(this).hide(\'fast\');\n            });\n            $(\'form\').ajaxForm({\n                    type: \'POST\',\n                    dataType: \'json\',\n                    beforeSubmit: function(data, form){\n                        if ($(\'#id_password\').val() != $(\'#id_password_confirm\').val()){\n                            //Passwords don\'t match.\n                            form.prepend(\'<div class="errormessage">Passwords do not match</div>\');\n                            return false;\n                        }else{\n                            //Clear errors\n                            $(\'.errormessage\').remove()\n                            //Hide the form, show pending box with spinner.\n                            $(\'#launchFormContainer\').hide(\'fast\');\n                            $(\'#responsePanel\').show(\'fast\');\n                        }\n                        //Dig up zone info for selected cluster, set hidden input.\n                        //This is not necessary to present to the user though the interface may prove useful.\n                        var ei_val = _.find(data, function(f_obj){return f_obj.name === \'existing_instance\'});\n                        if( ei_val && (ei_val.value !== "New Cluster")){\n                            var cluster = _.find(cloudlaunch_clusters, function(cluster){return cluster.name === ei_val.value});\n                            var zdata = _.find(data, function(f_obj){return f_obj.name === \'zone\'});\n                            zdata.value = cluster.zone;\n                        }\n                    },\n                    success: function(data){\n                        //Success Message, link to key download if required, link to server itself.\n                        $(\'#launchPending\').hide(\'fast\');\n                        //Set appropriate fields (dns, key, ami) and then display.\n                        if(data.kp_material_tag){\n                            var kp_download_link = $(\'<a/>\').attr(\'href\', PKEY_DL_URL + \'?kp_material_tag=\' + data.kp_material_tag)\n                                                            .attr(\'target\',\'_blank\')\n                                                            .text("Download your key now");\n                            $(\'#keypairInfo\').append(kp_download_link);\n                            $(\'#keypairInfo\').show();\n                        }\n                        $(\'.kp_name\').text(data.kp_name);\n                        $(\'#instance_id\').text(data.instance_id);\n                        $(\'#image_id\').text(data.image_id);\n                        $(\'#instance_link\').html($(\'<a/>\')\n                            .attr(\'href\', \'http://\' + data.public_dns_name + \'/cloud\')\n                            .attr(\'target\',\'_blank\')\n                            .text(data.public_dns_name + \'/cloud\'));\n                        $(\'#instance_dns\').text(data.public_dns_name);\n                        $(\'#launchSuccess\').show(\'fast\');\n                    },\n                    error: function(jqXHR, textStatus, errorThrown){\n                       $(\'#launchFormContainer\').prepend(\'<div class="errormessage">\' + errorThrown + " : " + jqXHR.responseText + \'</div>\');\n                       $(\'#responsePanel\').hide(\'fast\');\n                       $(\'#launchFormContainer\').show(\'fast\');\n                    }\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        ami = context.get('ami', UNDEFINED)
        h = context.get('h', UNDEFINED)
        bucket_default = context.get('bucket_default', UNDEFINED)
        share_string = context.get('share_string', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 173
        __M_writer(u'\n    <div style="overflow: auto; height: 100%;">\n        <div class="page-container" style="padding: 10px;">\n        <div id="loading_indicator"></div>\n            <h2>Launch a Galaxy Cloud Instance</h2>\n              <div id="launchFormContainer" class="toolForm">\n                    <form id="cloudlaunch_form" action="')
        # SOURCE LINE 179
        __M_writer(unicode(h.url_for( controller='/cloudlaunch', action='launch_instance')))
        __M_writer(u'" method="post">\n\n                    <p>To launch a Galaxy Cloud Cluster, enter your AWS Secret Key ID, and Secret Key.  Galaxy will use\n                    these to present appropriate options for launching your cluster.   Note that using this form to\n                    launch computational resources in the Amazon Cloud will result in   costs to the account indicated\n                    above.  See <a href="http://aws.amazon.com/ec2/pricing/">Amazon\'s pricing</a> for more information.\n                    options for launching your cluster.</p> </p>\n\n                    <div class="form-row">\n                        <label for="id_key_id">Key ID</label>\n                        <input type="text" size="30" maxlength="20" name="key_id" id="id_key_id" value="" tabindex="1"/><br/>\n                        <div class="toolParamHelp">\n                            This is the text string that uniquely identifies your account, found in the\n                            <a href="https://portal.aws.amazon.com/gp/aws/securityCredentials">Security Credentials section of the AWS Console</a>.\n                        </div>\n                    </div>\n\n                    <div class="form-row">\n                        <label for="id_secret">Secret Key</label>\n                        <input type="text" size="50" maxlength="40" name="secret" id="id_secret" value="" tabindex="2"/><br/>\n                        <div class="toolParamHelp">\n                            This is your AWS Secret Key, also found in the <a href="https://portal.aws.amazon.com/gp/aws/securityCredentials">Security\nCredentials section of the AWS Console</a>.  </div>\n                    </div>\n\n                    <div id="hidden_options">\n')
        # SOURCE LINE 205
        if not share_string:
            # SOURCE LINE 206
            __M_writer(u'                        <div id=\'existing_instance_wrapper\' style="display:none;" class="form-row">\n                                <label for="id_existing_instance">Instances in your account</label>\n                                <select name="existing_instance" id="id_existing_instance" style="min-width: 228px">\n                                </select>\n                                <input id=\'id_zone\' type=\'hidden\' name=\'zone\' value=\'\'/>\n                        </div>\n')
            pass
        # SOURCE LINE 213
        __M_writer(u'                        <div id=\'cluster_name_wrapper\' class="form-row">\n                            <label for="id_cluster_name">Cluster Name</label>\n                            <input type="text" size="40" class="text-and-autocomplete-select" name="cluster_name" id="id_cluster_name"/><br/>\n                            <div class="toolParamHelp">\n                                This is the name for your cluster.  You\'ll use this when you want to restart.\n                            </div>\n                        </div>\n\n                        <div class="form-row">\n                            <label for="id_password">Cluster Password</label>\n                            <input type="password" size="40" name="password" id="id_password"/><br/>\n                        </div>\n\n                        <div class="form-row">\n                            <label for="id_password_confirm">Cluster Password - Confirmation</label>\n                            <input type="password" size="40" name="password_confirm" id="id_password_confirm"/><br/>\n                        </div>\n\n\n                        <div class="form-row">\n                            <label for="id_keypair">Key Pair</label>\n                            <select name="keypair" id="id_keypair" style="min-width: 228px">\n                                <option name="Create" value="cloudman_keypair">cloudman_keypair</option>\n                            </select>\n                        </div>\n\n')
        # SOURCE LINE 239
        if share_string:
            # SOURCE LINE 240
            __M_writer(u"                            <input type='hidden' name='share_string' value='")
            __M_writer(unicode(share_string))
            __M_writer(u"'/>\n")
            # SOURCE LINE 241
        else:
            # SOURCE LINE 242
            __M_writer(u'                        <!-- DBEDIT temporary hide share string due to it being broken on the cloudman end -->\n                        <div class="form-row" style="display:none;">\n                            <label for="id_share_string">Instance Share String (optional)</label>\n                            <input type="text" size="120" name="share_string" id="id_share_string"/><br/>\n                        </div>\n')
            pass
        # SOURCE LINE 248
        __M_writer(u'\n')
        # SOURCE LINE 249
        if ami:
            # SOURCE LINE 250
            __M_writer(u"                            <input type='hidden' name='ami' value='")
            __M_writer(unicode(ami))
            __M_writer(u"'/>\n")
            pass
        # SOURCE LINE 252
        __M_writer(u'\n')
        # SOURCE LINE 253
        if bucket_default:
            # SOURCE LINE 254
            __M_writer(u"                            <input type='hidden' name='bucket_default' value='")
            __M_writer(unicode(bucket_default))
            __M_writer(u"'/>\n")
            pass
        # SOURCE LINE 256
        __M_writer(u'\n                        <div class="form-row">\n                            <label for="id_instance_type">Instance Type</label>\n                            <select name="instance_type" id="id_instance_type">\n                                <option value="m1.large">Large</option>\n                                <option value="m1.xlarge">Extra Large</option>\n                                <option value="m2.4xlarge">High-Memory Quadruple Extra Large</option>\n                            </select>\n                        </div>\n                        <div class="form-row">\n                            <p>Requesting the instance may take a moment, please be patient.  Do not refresh your browser or navigate away from the page</p>\n                            <input type="submit" value="Submit" id="id_submit"/>\n                        </div>\n                    </div>\n                        <div class="form-row">\n                        <div id="loading_indicator" style="position:relative;left:10px;right:0px"></div>\n                        </div>\n                    </form>\n                </div>\n                <div id="responsePanel" class="toolForm" style="display:none;">\n                        <div id="launchPending">Launch Pending, please be patient.</div>\n                        <div id="launchSuccess" style="display:none;">\n                            <div id="keypairInfo" style="display:none;margin-bottom:20px;">\n                                <h3>Very Important Key Pair Information</h3>\n                                <p>A new key pair named <strong><span class="kp_name">kp_name</span></strong> has been created in your AWS\n                                account and will be used to access this instance via ssh. It is\n                                <strong>very important</strong> that you save the following private key\n                                as it is not saved on this Galaxy instance and will be permanently lost if not saved.  Additionally, this link will\n                                only allow a single download, after which the key is removed from the Galaxy server permanently.<br/>\n                            </div>\n                            <div>\n                                <h3>Access Information</h3>\n                                <ul>\n                                    <li>Your instance \'<span id="instance_id">undefined</span>\' has been successfully launched using the\n                                \'<span id="image_id">undefined</span>\' AMI.</li>\n                                <li>While it may take a few moments to boot, you will be able to access the cloud control\n                                panel at <span id="instance_link">undefined.</span>.</li>\n                            <li>SSH access is also available using your private key.  From the terminal, you would execute something like:</br>&nbsp;&nbsp;&nbsp;&nbsp;`ssh -i <span class="kp_name">undefined</span>.pem ubuntu@<span\nid="instance_dns">undefined</span>`</li>\n                                </ul>\n                        </div>\n                </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


