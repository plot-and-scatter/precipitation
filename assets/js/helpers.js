"use strict";

// From http://stackoverflow.com/q/14167863/715870
d3.selection.prototype.moveToFront = function() {
  return this.each(function(){
    this.parentNode.appendChild(this);
  });
};

function drawGraph(transitionDuration) {

  highlightStation(station);
  
  x.domain(d3.extent(DATA, function(d) { return d.date; }));

  var y_domain = 900;

  if (!d3.select("#lock_y").property("checked")) {
    y_domain = d3.max(DATA, function(d) { return Math.max(d[station], d[station + " NORMALS"]); })
  }

  y.domain([
    0,
    y_domain
  ]);

  graph.datum(DATA);

  if (graph.selectAll(".x.axis")[0].length < 1) {
    graph.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis.tickSize(-height, 0, 0))
      .selectAll("text")
        .attr("dx", "1em");    
  } else {
    graph.selectAll(".x.axis")
      .transition().duration(transitionDuration)
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis.tickSize(-height, 0, 0));    
  }

  if (graph.selectAll(".y.axis")[0].length < 1) {
    graph.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Precipitation (mm)");
  } else {
    graph.selectAll(".y.axis")
      .transition().duration(transitionDuration)
      .call(yAxis);
  }

  if (graph.selectAll("#clip-below path")[0].length < 1) {
    graph.append("clipPath")
      .attr("id", "clip-below")
    .append("path")
      .attr("d", area.y0(height));    
  } else {
    graph.selectAll("#clip-below path")
      .transition()
      .duration(transitionDuration)
      .attr("d", area.y0(height));
  }
  
  if (graph.selectAll("#clip-above path")[0].length < 1) {
    graph.append("clipPath")
      .attr("id", "clip-above")
    .append("path")
      .attr("d", area.y0(0));
  } else {
    graph.selectAll("#clip-above path")
      .transition()
      .duration(transitionDuration)
      .attr("d", area.y0(0));
  }

  if (graph.selectAll(".area.below")[0].length < 1) {
    graph.append("path")
      .attr("class", "area below")
      .attr("clip-path", "url(#clip-above)") // Clip *below* the "above" path
      .attr("d", area.y0(function(d) { return y(d[station + " NORMALS"]); }));
  } else {
    graph.selectAll(".area.below")
      .transition()
      .duration(transitionDuration)
      .attr("d", area.y0(function(d) { return y(d[station + " NORMALS"]); }));
  }

  if (graph.selectAll(".area.above")[0].length < 1) {
    graph.append("path")
      .attr("class", "area above")
      .attr("clip-path", "url(#clip-below)") // Clip *above* the "below" path
      .attr("d", area);
  } else {
    graph.selectAll(".area.above")
      .transition()
      .duration(transitionDuration)
      .attr("d", area);
  }



  if (graph.selectAll(".line.actuals")[0].length < 1) {
    graph.append("path")
      .attr("class", "line actuals")
      .attr("d", actualsLine);
  } else {
    graph.selectAll(".line.actuals").transition().duration(transitionDuration).attr("d", actualsLine);
  }

}

// From http://stackoverflow.com/q/196972/715870
function titleCase(str) {
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

function prettyStationName(stationName) {
  stationName = titleCase(stationName);
  var length = stationName.length;
  var lastSpaceIndex = stationName.lastIndexOf(" ");
  if (lastSpaceIndex == length - 2) {
    // Trim off " A" suffix (e.g. "Abbotsford A" --> "Abbotsford")
    stationName = stationName.substring(0, lastSpaceIndex);
  }

  return stationName;

}

function drawSelect() {

  var optionsForSelect = [];

  for (key in DATA[0]) {
    if (key != "date" && key.indexOf("NORMALS") == -1) {
      optionsForSelect.push(key);
    }
  }
  
  options = options.data(optionsForSelect)
            .enter().append("option")
              .attr("value", function(d) { return d; })
              .text(function(d) { return prettyStationName(d); });
}

function highlightStation(station) {
  map.selectAll(".station").classed("highlight", false).transition().duration(DURATION).attr("r", getCircleRadius(map_width));
  map.selectAll('[data-name="' + station + '"]').classed("highlight", true).moveToFront().transition().duration(DURATION).attr("r", getCircleRadius(map_width) * 1.4);
}

function changeSelect() {
  var selectedIndex = select.property("selectedIndex");
  var selectedStation = options[0][selectedIndex].__data__;
  station = selectedStation;
  drawGraph(DURATION);
}

function clickCircle(stationName) {
  station = stationName;
  select.property("value", stationName);
  drawGraph(DURATION);
}

function getCircleRadius(mapWidth) {
  var radius = Math.max(5, mapWidth / 120);
  return radius;
}