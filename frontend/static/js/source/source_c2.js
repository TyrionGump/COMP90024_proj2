var source_c2 = echarts.init(document.getElementById("source_c2"));
var source_c2_scatter = echarts.init(document.getElementById("source_c2"));

var source_map_data = [{name: 'melbourne', value: [144.96316, -37.81422, [10000, 20000]]}, 
					   {name: 'brisbane', value: [153.021072, -27.470125, [1000, 2000]]}]

var source_c2_option = {
	tooltip: {
		trigger: "item",
	},
	title: {
		text: "Sentiment Score Map for iPhone",
		left: "center",
		textStyle: {
			color: "white",
			fontSize:12
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
		zoom: 1.8,
		center: [133.78, -25.27]
	},
}

var source_c2_scatter_option = {
	z: 5,
	series: [{
		name: '销量', // series名称
		type: 'scatter', // series图表类型
		coordinateSystem: 'geo', // series坐标系类型
		data: source_map_data,
		symbolSize: function(val) {
			return val[2] * 200;
		},
		encode: {
			tooltip: [2],
		},
		tooltip: {
			formatter: function(params) {
				return params.marker + ' ' + params.name + '<br/>' + 'Average Polarity for IOS: ' + params.value[2]
			},
		}

	}],

}


source_c2.setOption(source_c2_option);
window.addEventListener('resize', function() {
	source_c2.resize()
})