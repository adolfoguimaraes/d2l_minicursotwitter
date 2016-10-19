/**
 * Created by adolfoguimaraes on 28/09/16.
 */
//Baseado em: http://www.brettdangerfield.com/post/realtime_data_tag_cloud/
//http://stackoverflow.com/questions/26471497/d3-js-word-missing-from-word-cloud
//https://github.com/shprink/d3js-wordcloud/blob/master/word-cloud.js

(function() {

	/* D3  */

	var words_array = [];

	var width = 1000, height = 350;

	var typeFace = 'Impact';

	var colors = d3.scale.category20b();

	var svg = d3.select('#cloud').append('svg')
			.attr('width', width)
			.attr('height', height)
			.append('g')
			.attr('transform', "translate(" + [width >> 1, height >> 1] + ")");

	var cloud = null;

	function calculateCloud(wordCount) {

		var fontSize = d3.scale.linear()
                 .domain([0, d3.max(wordCount, function(d) { return d.size} )])
					.range([10, 90]);

		cloud = d3.layout.cloud()
			.size([width, height])
			.words(wordCount)
			.rotate(function() { return ~~(Math.random()*2) * 90;}) // 0 or 90deg
			.font(typeFace)
			.fontSize(function(d) { return fontSize(d.size) })
			.on('end', drawCloud)
			.start();
	}

	function drawCloud(words) {
		var vis = svg.selectAll('text').data(words);

		vis.enter().append('text')

			.style('font-size', function(d) {
				return d.size + 'px';
			})
			.style('font-family', function(d) {
				return d.font;
			})
			.style('fill', function(d, i) {
				return colors(i);
			})
			.attr('text-anchor', 'middle')
			.attr('transform', function(d) {
			  return 'translate(' + [d.x, d.y] + ')rotate(' + d.rotate + ')';
			})
			.text(function(d) { return d.text; });
	}




	// fetching last 100 chat room messages
	function getData() {

		d3.select("#loading").html("Carregando a nuvem de termos...");

		d3.json("/cloud/", function(error, json) {



			d3.select("#loading").html("");

			if (error) {
				return console.warn(error);
			}


			for (key in json){
				words_array.push({text: key, size: json[key]})
			}

			calculateCloud(words_array);
		});
	};



	getData();

	var interval = setInterval(function(){window.location.reload(1)}, 60000);

})();