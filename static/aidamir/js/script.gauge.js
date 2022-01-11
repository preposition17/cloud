var gauges_div = document.getElementsByClassName("gauges")[0];
console.log(gauges_div)

var gauge_opts = {
  angle: 0.25, // The span of the gauge arc
  lineWidth: 0.1, // The line thickness
  radiusScale: 1, // Relative radius
  pointer: {
    length: 0.6, // // Relative to gauge radius
    strokeWidth: 0.035, // The thickness
    color: '#000000' // Fill color
  },
  limitMax: false,     // If false, max value increases automatically if value > maxValue
  limitMin: false,     // If true, the min value of the gauge will be fixed
  colorStart: 'rgb(255, 99, 132)',   // Colors
  colorStop: '#C0C0DB',    // just experiment with them
  strokeColor: '#EEEEEE',  // to see which ones work best for you
  generateGradient: true,
  highDpiSupport: true,     // High resolution support

};

temp_gauge_canvas = document.getElementById('temp_gauge');
gauge_opts.colorStart = 'rgb(255, 99, 132)';
var tempGauge = new Donut(temp_gauge_canvas).setOptions(gauge_opts);
tempGauge.maxValue = 40; // set max gauge value
tempGauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
tempGauge.animationSpeed = 32; // set animation speed (32 is default value)
tempGauge.setTextField(document.getElementById('temp_gauge_value'), 1);


ligh_gauge_canvas = document.getElementById('light_gauge');
gauge_opts.colorStart = 'rgb(85,255,167)';
var lightGauge = new Donut(ligh_gauge_canvas).setOptions(gauge_opts);
lightGauge.maxValue = 100; // set max gauge value
lightGauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
lightGauge.animationSpeed = 32; // set animation speed (32 is default value)
lightGauge.setTextField(document.getElementById('light_gauge_value'), 1);


range_gauge_canvas = document.getElementById('range_gauge');
gauge_opts.colorStart = 'rgb(0,0,0)';
var rangeGauge = new Donut(range_gauge_canvas).setOptions(gauge_opts);
rangeGauge.maxValue = 20; // set max gauge value
rangeGauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
rangeGauge.animationSpeed = 32; // set animation speed (32 is default value)
rangeGauge.setTextField(document.getElementById('range_gauge_value'), 1);


hum_gauge_canvas = document.getElementById('hum_gauge');
gauge_opts.colorStart = 'rgb(253,126,11)';
var humGauge = new Donut(hum_gauge_canvas).setOptions(gauge_opts);
humGauge.maxValue = 40; // set max gauge value
humGauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
humGauge.animationSpeed = 32; // set animation speed (32 is default value)
humGauge.setTextField(document.getElementById('hum_gauge_value'), 1);


setInterval(function() {
  tempGauge.set(temp);
  lightGauge.set(light);
  rangeGauge.set(range);
  humGauge.set(hum);
}, 100);
