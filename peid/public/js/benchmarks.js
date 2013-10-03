var margin = {top: 5, right: 75, bottom: 20, left: 110},
    width = 760 - margin.left - margin.right,
    height = 50 - margin.top - margin.bottom;


var chart = d3.bullet()
    .width(width)
    .height(height);

var source = ["engagement", "activity", "outcomes"];

$(document).ready(function() {    
    for(var d in source){
        draw(source[d],0);
    }
       
});

function update(n){
    for(var s in source){
        redraw(source[s], n);
    }   
}

function draw(source, n){
    d3.json("../public/data/benchmarks.json", function(error, data) {
      
      var svg = d3.select("#"+source).selectAll("svg")
          .data(eval("data["+n+"]."+source))
        .enter().append("svg")
          .attr("class", "bullet")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
        .append("g")
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
          .call(chart.duration(1000));
      
      var title = svg.append("g")
          .style("text-anchor", "end")
          .attr("transform", "translate(-6," + height / 2 + ")");
    
      title.append("text")
          .attr("class", "title")
          .text(function(d) { return d.title; });
    
      title.append("text")
          .attr("class", "subtitle")
          .attr("dy", "1.6em")
          .text(function(d) { return d.subtitle; });
    });
}

function redraw(source, n){
    d3.json("../public/data/benchmarks.json", function(error, data) {
		d3.select("#"+source).selectAll("svg")
			.datum(function (d, i) {
			    dt = eval("data["+n+"]."+source);
                console.log(dt[i]);
				d.ranges = dt[i].ranges;
				d.measures = dt[i].measures;
				d.markers = dt[i].markers;
				return d;
			})
			.call(chart.duration(1000));
        });    
}