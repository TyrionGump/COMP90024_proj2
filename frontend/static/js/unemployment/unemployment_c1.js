var unemployment_c1 = echarts.init(document.getElementById("unemployment_c1"));
var unemployment_c1_scatter = echarts.init(document.getElementById("unemployment_c1"));

var unemployment_map_data = [{name: 'melbourne', value: [144.96316, -37.81422, [10000, 20000]]}, 
					   {name: 'brisbane', value: [153.021072, -27.470125, [1000, 2000]]}]

var unemployment_c1_option = {
	"title": {
		"text": "Android"
	},
	tooltip: {
		trigger: "item",
	},
	"toolbox": {
		"show": true,
		"orient": "vertical",
		"left": "right",
		"top": "center",
		"feature": {
			"restore": {},
			"saveAsImage": {}
		}
	},
	"geo": {
		"map": "澳大利亚",
		"roam": false,
		"label": {
			"emphasis": {
				"show": true,
				"textStyle": {
					"color": "#000"
				}
			}
		},
		"itemStyle": {
			"normal": {
				"areaColor": "#293C55",
				"borderColor": "#fff"
			},
			"emphasis": {
				"areaColor": "yellow"
			}
		},
		aspectScale: 1,
		zoom: 1.5,
		center: [133.78, -25.27]
	},
}

var unemployment_c1_scatter_option = {
	z: 5,
	series: [{
		name: '销量', // series名称
		type: 'scatter', // series图表类型
		coordinateSystem: 'geo', // series坐标系类型
		data: unemployment_map_data,
		symbolSize: function(val) {
			return val[2][0] * 200;
		},
		encode: {
			tooltip: [2],
		},
		tooltip: {
			formatter: function(params) {
				return params.marker + ' ' + params.name + '<br/>' + 'Average Polarity for unemployment: ' + params.value[2]
			},
		}

	}],

}


unemployment_c1.setOption(unemployment_c1_option);
window.addEventListener('resize', function() {
	unemployment_c1.resize()
})