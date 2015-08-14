function transformData(data) {
  return data.map(function (item) {
    var yearPrecipitations = {};
    yearPrecipitations.year = item.Year;
    yearPrecipitations.stations = [];

    Object.keys(item).forEach(function (stationName) {
      // Skip the year property, as it's not a station
      if (stationName === 'Year') {
        return;
      }

      yearPrecipitations.stations.push({
        stationName: stationName,
        mean: item[stationName]
      });
    });

    return yearPrecipitations;
  });
}

globalData = null;
d3.csv("actual_means.csv", function(error, data){
  console.log(data);
  globalData = transformData(data);
  console.log('transformed data:', globalData);

  data.forEach(function(d){
    d3.select(".slopegraph").append("p").text("Je suis un element");  
  });
});

