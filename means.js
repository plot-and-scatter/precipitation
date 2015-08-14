function transformData(data) {
  return data.map(function (item) {
    var yearPrecipitations = {};
    yearPrecipitations.year = item.Year;
    yearPrecipitations.stations = [];

    Object.keys(item).forEach(function (stationName) {
      // Skip the year property, as it's not a station
      if (stationName === "Year") {
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

var margin = {top: 10, right: 10, bottom: 20, left: 10};
var width = 500;
var height = 600;


d3.csv("actual_means.csv", function(error, data){
  //console.log(data);
  //Grab data, transform it and put it in a variable called Global Data
  globalData = transformData(data);
  console.log("transformed data:", globalData);
  
  
  

  var leftStation = globalData[0];
  var rightStation = globalData[4];
  var chart = d3.select('#slopegraph').append("svg")
    .attr("width", width)
    .attr("height", height);
  
  console.log("I work till here");
  
  /*
  renderStandings(chart, leftStation, rightStation, 
  {'key': 'year', 'title': 'Year'});
  */
   

   data.forEach(function(d){
    d3.select(".slopegraph").append("p").text("Je suis un element"); 
    
   
     
   });
  
});


function renderStandings(chart, leftStation, rightStation, year) {
  


}


/*Funtion stationMean with parameters name and mean
function stationMean (name, mean) {
  name = globalData.stations.stationName;
  mean = globalData.stations.mean;
}

var year = 
            
            */
            


   