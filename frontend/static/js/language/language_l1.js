var language_l1 = echarts.init(document.getElementById("language_l1"));
var language_data = {
	"first_4": {
		"Sydney": [{
			"name": "english",
			"value": 11
		}, {
			"name": "chinese",
			"value": 22
		}],
		"Melbourne": [{
			"name": "english",
			"value": 33
		}, {
			"name": "chinese",
			"value": 44
		}],
		"Brisbane": [{
			"name": "english",
			"value": 55
		}, {
			"name": "chinese",
			"value": 66
		}],
		"Perth": [{
			"name": "english",
			"value": 77
		}, {
			"name": "chinese",
			"value": 88
		}]
	},
	"last_4": {
		"Adelaide": [{
			"name": "english",
			"value": 99
		}, {
			"name": "chinese",
			"value": 11
		}],
		"Gold Coast": [{
			"name": "english",
			"value": 22
		}, {
			"name": "chinese",
			"value": 33
		}],
		"Canberra": [{
			"name": "english",
			"value": 44
		}, {
			"name": "chinese",
			"value": 55
		}],
		"Newcastle": [{
			"name": "english",
			"value": 66
		}, {
			"name": "chinese",
			"value": 77
		}]
	}
}
var language_l1_option = {
	baseOption: {
		timeline: {
			axisType: 'category',
			// realtime: false,
			// loop: false,
			autoPlay: true,
			// currentIndex: 2,
			playInterval: 5000,
			data: [
				"first 4 cities", "last 4 cities"
			]
		},
		
		tooltip: {},
		legend: {
			show:false
		},

		calculable: true,
		series: [{
			label: {
				normal: {
					position: 'inner',
					show: false
				}
			},
			type: 'pie',
			radius: "33%",
			center: ["25%", "20%"],
		}, {
			label: {
				normal: {
					position: 'inner',
					show: false
				}
			},
			type: 'pie',
			radius: "33%",
			center: ["75%", "20%"]
		}, {
			label: {
				normal: {
					position: 'inner',
					show: false
				}
			},
			type: 'pie',
			radius: "33%",
			center: ["25%", "65%"],
		}, {
			label: {
				normal: {
					position: 'inner',
					show: false
				}
			},
			type: 'pie',
			radius: "33%",
			center: ["75%", "65%"]
		}]
	},
	options: [{

			series: [{
				title: {
					text: "Sydney",
					show:true
				},
				name: 'Sydney',
				data: language_data['first_4']['Sydney']
			}, {
				name: 'Melbourne',
				data: language_data['first_4']['Melbourne']
			}, {
				name: 'Brisbane',
				data: language_data['first_4']['Brisbane']
			}, {
				name: 'Perth',
				data: language_data['first_4']['Perth']
			}]
		},
		{
			series: [{
				name: 'Adelaide',
				data: language_data['last_4']['Adelaide']
			}, {
				name: 'Gold Coast',
				data: language_data['last_4']['Gold Coast']
			}, {
				name: 'Canberra',
				data: language_data['last_4']['Canberra']
			}, {
				name: 'Newcastle',
				data: language_data['last_4']['Newcastle']
			}]
		},

	]
};

window.addEventListener('resize', function() {
	language_l1.resize()
})


// {
// 	legend: {
// 		top: 'bottom'
// 	},
// 	tooltip: {
// 		trigger: 'item',
// 		formatter: '{a} <br/> ({d}%)'
// 	},
// 	// toolbox: {
// 	//     show: true,
// 	//     feature: {
// 	//         mark: {show: true},
// 	//         dataView: {show: true, readOnly: false},
// 	//         restore: {show: true},
// 	//         saveAsImage: {show: true}
// 	//     }
// 	// },
// 	series: [{
// 			name: '面积模式',
// 			type: 'pie',
// 			radius: "20%",
// 			center: ['25%', '30%'],
// 			// roseType: 'area',
// 			// itemStyle: {
// 			//     borderRadius: 8
// 			// },
// 			minAngle: 50,
// 			data: [{
// 					value: 40,
// 					name: 'rose 1'
// 				},
// 				{
// 					value: 38,
// 					name: 'rose 2'
// 				},
// 				{
// 					value: 32,
// 					name: 'rose 3'
// 				},
// 				{
// 					value: 30,
// 					name: 'rose 4'
// 				},
// 				{
// 					value: 28,
// 					name: 'rose 5'
// 				},
// 				{
// 					value: 26,
// 					name: 'rose 6'
// 				},
// 				{
// 					value: 22,
// 					name: 'rose 7'
// 				},
// 				{
// 					value: 18,
// 					name: 'rose 8'
// 				}
// 			]
// 		},
// 		{
// 			name: '面积模式',
// 			type: 'pie',
// 			radius: "20%",
// 			center: ['50%', '30%'],
// 			// roseType: 'area',
// 			// itemStyle: {
// 			//     borderRadius: 8
// 			// },
// 			minAngle: 50,
// 			data: [{
// 					value: 40,
// 					name: 'rose 1'
// 				},
// 				{
// 					value: 38,
// 					name: 'rose 2'
// 				},
// 				{
// 					value: 32,
// 					name: 'rose 3'
// 				},
// 				{
// 					value: 30,
// 					name: 'rose 4'
// 				},
// 				{
// 					value: 28,
// 					name: 'rose 5'
// 				},
// 				{
// 					value: 26,
// 					name: 'rose 6'
// 				},
// 				{
// 					value: 22,
// 					name: 'rose 7'
// 				},
// 				{
// 					value: 18,
// 					name: 'rose 8'
// 				}
// 			]
// 		},
// 		{
// 			name: '面积模式',
// 			type: 'pie',
// 			radius: "20%",
// 			center: ['80%', '30%'],
// 			// roseType: 'area',
// 			// itemStyle: {
// 			//     borderRadius: 8
// 			// },
// 			data: [{
// 					value: 40,
// 					name: 'rose 1'
// 				},
// 				{
// 					value: 38,
// 					name: 'rose 2'
// 				},
// 				{
// 					value: 32,
// 					name: 'rose 3'
// 				},
// 				{
// 					value: 30,
// 					name: 'rose 4'
// 				},
// 				{
// 					value: 28,
// 					name: 'rose 5'
// 				},
// 				{
// 					value: 26,
// 					name: 'rose 6'
// 				},
// 				{
// 					value: 22,
// 					name: 'rose 7'
// 				},
// 				{
// 					value: 18,
// 					name: 'rose 8'
// 				}
// 			]
// 		}
// 	],

// };
