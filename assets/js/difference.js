var $graphic = $('#graphic');
var graphic_data_url = 'difference.csv';
var graphic_data;
var graphic_aspect_width = 16;
var graphic_aspect_height = 9;
var mobile_threshold= 500;
    

function drawGraphic() {
  var margin = { top: 10, right: 15, bottom: 25, left: 35 }; 
  var width = $graphic.width() - margin.left - margin.right;
  var height = Math.ceil((wdith * graphic_aspect_height)/ graphic_aspect_width)- margin.top - margin.bottom;
  var num_ticks = 14;
  
  if (width < mobile_threshold) {
    num_ticks = 5;
  }
}

//clear out existing graphics
$graphic.empty();
    
  
// Continue reading 
//http://blog.apps.npr.org/2014/05/19/responsive-charts.html
// * https://www.thatdatadude.com/how-to-make-d3-charts-responsive/