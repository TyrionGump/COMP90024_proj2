var source_c1 = echarts.init(document.getElementById("source_c1"));
var source_c1_scatter = echarts.init(document.getElementById("source_c1"));

var source_map_data = [{name: 'melbourne', value: [144.96316, -37.81422, [10000, 20000]]}, 
					   {name: 'brisbane', value: [153.021072, -27.470125, [1000, 2000]]}]

var source_c1_option = {
	tooltip: {
		trigger: "item",
	},
	// "toolbox": {
	// 	"show": true,
	// 	"orient": "vertical",
	// 	"left": "right",
	// 	"top": "center",
	// 	"feature": {
	// 		"restore": {},
	// 		"saveAsImage": {}
	// 	}
	// },
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

var source_c1_scatter_option = {
	z: 5,
	series: [{
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
				return params.marker + ' ' + params.name + '<br/>' + 'Average Polarity for Android: ' + params.value[2]
			},
		}

	}],

}


source_c1.setOption(source_c1_option);
window.addEventListener('resize', function() {
	source_c1.resize()
})









// $(".panel_r2 h2").attr("display", "inline-block");  //设置p元素的class为 "high"
// $(".panel_r2 .dropdown").attr("display", "inline-block");  //设置p元素的class为 "high"
