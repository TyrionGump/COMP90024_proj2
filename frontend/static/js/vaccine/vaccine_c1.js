var vaccine_c1 = echarts.init(document.getElementById("vaccine_c1"));
var vaccine_c1_scatter = echarts.init(document.getElementById("vaccine_c1"));

var vaccine_map_data = [{name: 'melbourne', value: [144.96316, -37.81422, [10000, 20000]]}, {name: 'brisbane', value: [153.021072, -27.470125, [1000, 2000]]}]

var vaccine_c1_option = {
	tooltip: {
		trigger: "item",
	},
	title: {
		text: "Sentiment Score Map for Vaccine",
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

var vaccine_c1_scatter_option = {
	z: 5,
	series: [{
		name: 'Average Polarity', // series名称
		type: 'scatter', // series图表类型
		coordinateSystem: 'geo', // series坐标系类型
		data: vaccine_map_data,
		symbolSize: function(val) {
			return val[2][0] * 200;
		},
		encode: {
			tooltip: [2],
		},
		tooltip: {
			formatter: function(params) {
				return params.marker + ' ' + params.name + '<br/>' + "Average polarity about vaccine: " + params.value[2][0]
			}
		}

	}],

}
vaccine_c1.setOption(vaccine_c1_option);

window.addEventListener('resize', function() {
	vaccine_c1.resize()
})