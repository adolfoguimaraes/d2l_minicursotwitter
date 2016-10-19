// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 1000 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%Y%m%d").parse;

// Set the ranges
var x = d3.time.scale().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(8);

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(10);

// Define the line
var priceline = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.count); });

// Adds the svg canvas
var svg = d3.select("#graph")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("static/js/graph/hashtags.csv", function(error, data) {
    data.forEach(function(d) {
		d.date = parseDate(d.date);
		d.count = +d.count;
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.count; })]);

    // Nest the entries by symbol
    var dataNest = d3.nest()
        .key(function(d) {return d.hashtag;})
        .entries(data);

    var color = d3.scale.category10();  // set the colour scale

    // Loop through each symbol / key
    dataNest.forEach(function(d) {

        svg.append("path")
            .attr("class", "line")
            .attr("data-legend",function() { return d.key})
            .style("stroke", function() { // Add dynamically
                return d.color = color(d.key); })
            .attr("d", priceline(d.values));

    });

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    legend = svg.append("g")
        .attr("class","legend")
        .attr("transform","translate(800,30)")
        .style("font-size","12px")
        .call(d3.legend);
});