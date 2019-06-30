const TableV = {};

var d3;

TableV.create = (el, dataset) => {
    d3 = require("d3"); 

    var margin = { 
         top: 0.1 * window.innerHeight,
         right: 0.1 * window.innerWidth, 
         bottom: 0.1 * window.innerHeight,
         left: 0.1 * window.innerWidth },
    width = 1 * window.innerWidth - margin.left - margin.right,
    height = 1 * window.innerHeight - margin.top - margin.bottom,
    colors = ["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#253494","#081d58"],
    areas = ["Desktop", "Soft Skills", "ML", "Front", "Back", "DevOps", "Mobile", 
                "Game", "Test", "Personality"];
    var step;
    for (step = 0; step < 100; step++) {
        var element = dataset[step];
        console.log(element);
        areas[element[3] - 1] = element[0];  // здесь ошибка они не записываются
    }
    
    var table_size = Math.min(width, height);
    var gridSize = Math.floor(table_size / 10)
    var legendElementWidth = gridSize * 2;

    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var areaLabels = svg.selectAll(".areaLabels")
        .data(areas)
        .enter().append("text")
          .text(function (d) { console.log(d); return d; })
          .attr("x", function (d, i) { return  10+i * 2*gridSize; })
          .attr("y", function (d, i) { return (-1)**i * 10 - 30; })
          .attr("class", function (d, i) { return "mono"; });


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
            .attr("x", function(d) { return (d.x - 1) * 2*gridSize; })
            .attr("y", function(d) { return (d.y - 1) * gridSize; })
            .attr("rx", 4)
            .attr("ry", 4)
            .attr("class", "y bordered")
            .attr("width", 2*gridSize)
            .attr("height", gridSize)
            .style("fill", function(d) {
                return colorScale[d.value]; 
            })
        
        cards.enter()
            .append("text")
            .text(function (d) { return d.tech; })
            .attr("x", function (d, i) { return  (d.x - 1) * 2*gridSize; })
            .attr("y", function (d, i) { return (d.y) * gridSize - 2; })
            .attr("class", function(d, i) { return (d.y > 4 ? 
                                            "blackFont" :
                                            "whiteFont"); });

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