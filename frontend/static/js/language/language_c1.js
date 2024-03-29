var language_c1 = echarts.init(document.getElementById("language_c1"));
var language_c1_scatter = echarts.init(document.getElementById("language_c1"));
var language_map_data = [{name: 'melbourne', value: [144.96316, -37.81422, [10000, 20000]]}, {name: 'brisbane', value: [153.021072, -27.470125, [1000, 2000]]}]

var language_c1_option = {
	tooltip: {
		trigger: "item",
	},
	title: {
		text: "Sentiment Score Map for Language",
		left: "center",
		textStyle: {
			color: "white",
			fontSize:15
		}
	},
	"geo": {
		"map": "Australia",
		"roam": false,
		"label": {
			"emphasis": {
				"show": true,
				"textStyle": {
					"color": "#000",
				},
				
			}
		},
		"itemStyle": {
			"normal": {
				borderWidth: .5,
				borderColor: '#009fe8',
				areaColor: '#ffefd5' 
				
			},
			"emphasis": {
				borderWidth: .5,
				borderColor: '#4b0002',
				areaColor: '#fff',
			}
		},
		aspectScale: 1,
		zoom: 2.4,
		center: [133.78, -25.27]
	},
}

var language_c1_scatter_option = {
	z: 5,
	series: [{
		name: 'Average Polarity',
		type: 'scatter',
		coordinateSystem: 'geo',
		data: language_map_data,
		symbolSize: function(val) {
			return val[2] * 250;
		},
		encode: {
			tooltip: [2],
		},
		tooltip: {
			formatter: function(params) {
				return params.marker + ' ' + params.name + '<br/>' + 'Average Polarity for Language: '+ params.value[2]
			}
		}

	}],

}

language_c1.setOption(language_c1_option);

window.addEventListener('resize', function() {
	language_c1.resize()
})

// $(".panel_r2 h2").attr("display", "inline-block");  //设置p元素的class为 "high"
// $(".panel_r2 .dropdown").attr("display", "inline-block");  //设置p元素的class为 "high"