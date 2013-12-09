(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['template-visualization-chartControl'] = template(function (Handlebars,depth0,helpers,partials,data) {
  helpers = helpers || Handlebars.helpers;
  var buffer = "", stack1, stack2, foundHelper, tmp1, self=this, functionType="function", helperMissing=helpers.helperMissing, undef=void 0, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  
  return " checked=\"true\"";}

  buffer += "<p class=\"help-text\">\n        Use the following controls to how the chart is displayed.\n        The slide controls can be moved by the mouse or, if the 'handle' is in focus, your keyboard's arrow keys.\n        Move the focus between controls by using the tab or shift+tab keys on your keyboard.\n        Use the 'Draw' button to render (or re-render) the chart with the current settings.\n    </p>\n\n    <div id=\"datapointSize\" class=\"form-input numeric-slider-input\">\n        <label for=\"datapointSize\">Size of data point: </label>\n        <div class=\"slider-output\">";
  foundHelper = helpers.datapointSize;
  stack1 = foundHelper || depth0.datapointSize;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "datapointSize", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</div>\n        <div class=\"slider\"></div>\n        <p class=\"form-help help-text-small\">\n            Size of the graphic representation of each data point\n        </p>\n    </div>\n\n    <div id=\"animDuration\" class=\"form-input checkbox-input\">\n        <label for=\"animate-chart\">Animate chart transitions?: </label>\n        <input type=\"checkbox\" id=\"animate-chart\"\n            class=\"checkbox control\"";
  foundHelper = helpers.animDuration;
  stack1 = foundHelper || depth0.animDuration;
  stack2 = helpers['if'];
  tmp1 = self.program(1, program1, data);
  tmp1.hash = {};
  tmp1.fn = tmp1;
  tmp1.inverse = self.noop;
  stack1 = stack2.call(depth0, stack1, tmp1);
  if(stack1 || stack1 === 0) { buffer += stack1; }
  buffer += " />\n        <p class=\"form-help help-text-small\">\n            Uncheck this to disable the animations used on the chart\n        </p>\n    </div>\n\n    <div id=\"width\" class=\"form-input numeric-slider-input\">\n        <label for=\"width\">Chart width: </label>\n        <div class=\"slider-output\">";
  foundHelper = helpers.width;
  stack1 = foundHelper || depth0.width;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "width", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</div>\n        <div class=\"slider\"></div>\n        <p class=\"form-help help-text-small\">\n            (not including chart margins and axes)\n        </p>\n    </div>\n\n    <div id=\"height\" class=\"form-input numeric-slider-input\">\n        <label for=\"height\">Chart height: </label>\n        <div class=\"slider-output\">";
  foundHelper = helpers.height;
  stack1 = foundHelper || depth0.height;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "height", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</div>\n        <div class=\"slider\"></div>\n        <p class=\"form-help help-text-small\">\n            (not including chart margins and axes)\n        </p>\n    </div>\n\n    <div id=\"X-axis-label\"class=\"text-input form-input\">\n        <label for=\"X-axis-label\">Re-label the X axis: </label>\n        <input type=\"text\" name=\"X-axis-label\" id=\"X-axis-label\" value=\"";
  foundHelper = helpers.xLabel;
  stack1 = foundHelper || depth0.xLabel;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "xLabel", { hash: {} }); }
  buffer += escapeExpression(stack1) + "\" />\n        <p class=\"form-help help-text-small\"></p>\n    </div>\n\n    <div id=\"Y-axis-label\" class=\"text-input form-input\">\n        <label for=\"Y-axis-label\">Re-label the Y axis: </label>\n        <input type=\"text\" name=\"Y-axis-label\" id=\"Y-axis-label\" value=\"";
  foundHelper = helpers.yLabel;
  stack1 = foundHelper || depth0.yLabel;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "yLabel", { hash: {} }); }
  buffer += escapeExpression(stack1) + "\" />\n        <p class=\"form-help help-text-small\"></p>\n    </div>\n\n    <input id=\"render-button\" type=\"button\" value=\"Draw\" />";
  return buffer;});
})();