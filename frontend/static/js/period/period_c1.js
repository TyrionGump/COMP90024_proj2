var period_c1 = echarts.init(document.getElementById("period_c1"));
var period_c1_scatter = echarts.init(document.getElementById("period_c1"));
var period_map_data = [{name: 'melbourne', value: [144.96316, -37.81422, [10000, 20000]]}, {name: 'brisbane', value: [153.021072, -27.470125, [1000, 2000]]}]

var period_c1_option = {
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
		zoom: 2.4,
		center: [133.78, -25.27]
	},
}

var period_c1_scatter_option = {
	baseOption: {
		timeline: {
			axisType: 'category',
			// realtime: false,
			// loop: false,
			autoPlay: true,
			// currentIndex: 2,
			playInterval: 1500,
			// controlStyle: {
			//     position: 'left'
			// },
			data: [
				'00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'

			],
			// label: {
			// 	formatter: function(s) {
			// 		return (new Date(s)).getFullYear();
			// 	}
			// }
		},
		tooltip: {},

		series: [{
			name: 'polarity',
			type: 'scatter', // series图表类型
			coordinateSystem: 'geo', // series坐标系类型
			tooltip: {
				formatter: function(params) {
					return params.marker + ' ' + params.name + '<br/>' + 'Average Polarity for Time: ' + params.value[2]
				},
			},
			symbolSize: function(val) {
				return val[2] * 250;
			},
		}, ]
	},
	options: [{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		{
			series: [{
				data: period_map_data
			}, ]
		},
		
	]
};

period_c1.setOption(period_c1_option)
window.addEventListener('resize', function() {
	period_c1.resize()
})

// {
// 	z: 5,
// 	series: [{
// 		name: '销量', // series名称
// 		type: 'scatter', // series图表类型
// 		coordinateSystem: 'geo', // series坐标系类型
// 		data: period_map_data,
// 		symbolSize: function(val) {
// 			return val[2][0] / 100;
// 		},
// 		encode: {
// 			tooltip: [2],
// 		},
// 		tooltip: {
// 			formatter: function(params) {
// 				return params.marker + ' ' + params.name + '<br/>' + params.value[2][0] + '<br/>' + params.value[2][1]
// 			}
// 		}

// 	}],

// }