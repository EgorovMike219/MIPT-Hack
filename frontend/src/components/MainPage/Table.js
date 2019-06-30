const TableV = {};

var d3;

TableV.create = (el, dataset) => {
    d3 = require("d3"); 

    // var margin = { top: 50, right: 50, bottom: 50, left: 50 },
    // width = 960 - margin.left - margin.right,
    // height = 960 - margin.top - margin.bottom,
    // gridSize = Math.floor(width / 15),
    var legendElementWidth = gridSize * 2,
    colors = ["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#253494","#081d58"],
    areas = ["Desktop", "Soft Skills", "ML", "Front", "Back", "DevOps", "Mobile", 
                "Game", "Test", "Personality"];
    dataset.forEach(arr_element => {
        arr_element.forEach(element => {
            areas[element.x] = element.areas;
        })
    });
    
    var width = 0.8 * window.innerWidth;
    var height = 0.9 * window.innerHeight; 
    var table_size = Math.min(width, height);
    var margin_width = (window.innerWidth - table_size) / 2;
    var margin_height = (window.innerHeight - table_size) / 2 
    var gridSize = Math.floor(table_size / 10)

    var svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("transform", "translate(" + margin_width + "," + margin_height + ")");

    var areaLabels = svg.selectAll(".areaLabels")
        .data(areas)
        .enter().append("text")
          .text(function (d) { return d; })
          .attr("x", function (d, i) { return i * gridSize; })
          .attr("y", 0)
          .style("text-anchor", "end")
          .attr("transform", "translate(-6," + gridSize / 1.5 + ")")
          .attr("class", function (d, i) { return ((i >= 0 && i <= 4) ? "dayLabel mono axis axis-workweek" : "dayLabel mono axis"); });


    var heatmapChart = function(data_array) {
        var data = data_array.map(function(arr) {
            return {x: arr[3], y: arr[4], value: arr[1], area: arr[0], tech: arr[2]};
        });


        var colorScale = {0: "#ffffed", 1: "#ffffd9", 2: "#edf8b1", 3: "#c7e9b4", 
                            4: "#7fcdbb", 5: "#41b6c4", 6: "#1d91c0", 
                            7: "#225ea8", 8: "#253494", 9: "#081d58"}

        var cards = svg.selectAll(".y")
            .data(data, function(d) {return d.x+':'+d.y;});

        cards.enter().append("title");

        cards.enter().append("rect")
            .attr("x", function(d) { return (d.x - 1) * gridSize; })
            .attr("y", function(d) { return (d.y - 1) * gridSize; })
            .attr("rx", 4)
            .attr("ry", 4)
            .attr("class", "y bordered")
            .attr("width", gridSize)
            .attr("height", gridSize)
            .style("fill", function(d) {
                return colorScale[d.value]; 
            });

        // cards.transition().duration(0)
        //     .style("fill", function(d) { 
        //         console.log(d.value)
        //         return colorScale[d.value]; });

        cards.select("title").text(function(d) { return d.tech; });

        // cards.append("title");
            
        cards.exit().remove();

        // var legend = svg.selectAll(".legend")
        //     .data([0].concat(colorScale.quantiles()), function(d) { return d; });

        // legend.enter().append("g")
        //     .attr("class", "legend");

        // legend.append("rect")
        //     .attr("x", function(d, i) { return legendElementWidth * i; })
        //     .attr("y", height)
        //     .attr("width", legendElementWidth)
        //     .attr("height", gridSize / 2)
        //     .style("fill", function(d, i) { return colors[i]; });

        // legend.append("text")
        //     .attr("class", "mono")
        //     .text(function(d) { return "≥ " + Math.round(d); })
        //     .attr("x", function(d, i) { return legendElementWidth * i; })
        //     .attr("y", height + gridSize);

        // legend.exit().remove();  
    };

    heatmapChart(dataset);
};

export default TableV;