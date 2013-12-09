(function(b){function a(c){if(c.attr("title")||typeof(c.attr("original-title"))!="string"){c.attr("original-title",c.attr("title")||"").removeAttr("title")}}b.fn.tipsy=function(c){c=b.extend({},b.fn.tipsy.defaults,c);return this.each(function(){a(b(this));var d=b.fn.tipsy.elementOptions(this,c);var e=null;b(this).hover(function(){var f=this;e=setTimeout(function(){b.data(f,"cancel.tipsy",true);var o=b.data(f,"active.tipsy");if(!o){o=b('<div class="tipsy"><div class="tipsy-inner"/></div>');o.css({position:"absolute",zIndex:100000});b.data(f,"active.tipsy",o)}a(b(f));var m;if(typeof d.title=="string"){m=b(f).attr(d.title=="title"?"original-title":d.title)}else{if(typeof d.title=="function"){m=d.title.call(f)}}o.find(".tipsy-inner")[d.html?"html":"text"](m||d.fallback);var k=b.extend({},b(f).offset(),{width:f.offsetWidth,height:f.offsetHeight});o.get(0).className="tipsy";o.remove().css({top:0,left:0,visibility:"hidden",display:"block"}).appendTo(document.body);o.css({width:o.width()+1,height:o.height()});var h=o[0].offsetWidth,j=o[0].offsetHeight;var q=(typeof d.gravity=="function")?d.gravity.call(f):d.gravity;var l,i;switch(q.charAt(0)){case"n":l=k.top+k.height;i=k.left+k.width/2-h/2;o.addClass("tipsy-north");break;case"s":l=k.top-j;i=k.left+k.width/2-h/2;o.addClass("tipsy-south");break;case"e":l=k.top+k.height/2-j/2;i=k.left-h;o.addClass("tipsy-east");break;case"w":l=k.top+k.height/2-j/2;i=k.left+k.width;o.addClass("tipsy-west");break}var n=b(window);if(l<n.scrollTop()&&q.charAt(0)=="s"){l=k.top+k.height;q="north";o.removeClass("tipsy-south").addClass("tipsy-north")}l=Math.min(l,n.scrollTop()+n.height()-o.outerHeight());var g=0;if(i<n.scrollLeft()){g=i-n.scrollLeft()}var p=n.scrollLeft()+n.width()-o.outerWidth();if(i>p){g=i-p}i-=g;o.css({left:i,top:l});switch(q.charAt(0)){case"n":o.css("background-position",-(250-o.outerWidth()/2)+g+"px top");break;case"s":o.css("background-position",-(250-o.outerWidth()/2)+g+"px bottom");break;case"e":break;case"w":break}if(d.fade){o.stop().css({opacity:0,display:"block",visibility:"visible"}).animate({opacity:d.opacity})}else{o.css({visibility:"visible",opacity:d.opacity})}},d.delayIn)},function(){b.data(this,"cancel.tipsy",false);var f=this;clearTimeout(e);setTimeout(function(){if(b.data(this,"cancel.tipsy")){return}var g=b.data(f,"active.tipsy");if(d.fade){g.stop().fadeOut(function(){b(this).remove()})}else{if(g){g.remove()}}},d.delayOut)})})};b.fn.tipsy.elementOptions=function(d,c){return b.metadata?b.extend({},c,b(d).metadata()):c};b.fn.tipsy.defaults={delayIn:0,delayOut:100,fade:false,fallback:"",gravity:"n",html:false,opacity:0.8,title:"title"};b.fn.tipsy.autoNS=function(){return b(this).offset().top>(b(document).scrollTop()+b(window).height()/2)?"s":"n"};b.fn.tipsy.autoWE=function(){return b(this).offset().left>(b(document).scrollLeft()+b(window).width()/2)?"e":"w"}})(jQuery);