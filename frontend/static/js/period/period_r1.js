var period_r1 = echarts.init(document.getElementById('period_r1'));
var period_r1_option;

var dataMap = {};

// function dataFormatter(obj) {
// 	var pList = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Canberra", "Newcastle"];
// 	var temp;
// 	for (var year = 2002; year <= 2011; year++) {
// 		var max = 0;
// 		var sum = 0;
// 		temp = obj[year];
// 		for (var i = 0, l = temp.length; i < l; i++) {
// 			max = Math.max(max, temp[i]);
// 			sum += temp[i];
// 			obj[year][i] = {
// 				name: pList[i],
// 				value: temp[i]
// 			};
// 		}
// 		obj[year + 'max'] = Math.floor(max / 100) * 100;
// 		obj[year + 'sum'] = sum;
// 	}
// 	return obj;
// }

// dataMap.dataGDP = dataFormatter({
// 	//max : 60000,
// 	2011: [16251.93, 11307.28, 24515.76, 11237.55, 14359.88, 22226.7, 10568.83, 12582],
// 	2010: [14113.58, 9224.46, 20394.26, 9200.86, 11672, 18457.27, 8667.58, 10368.6],
// 	2009: [12153.03, 7521.85, 17235.48, 7358.31, 9740.25, 15212.49, 7278.75, 8587],
// 	2008: [11115, 6719.01, 16011.97, 7315.4, 8496.2, 13668.58, 6426.1, 8314.37],
// 	2007: [9846.81, 5252.76, 13607.32, 6024.45, 6423.18, 11164.3, 5284.69, 7104],
// 	2006: [8117.78, 4462.74, 11467.6, 4878.61, 4944.25, 9304.52, 4275.12, 6211.8],
// 	2005: [6969.52, 3905.64, 10012.11, 4230.53, 3905.03, 8047.26, 3620.27, 5513.7],
// 	2004: [6033.21, 3110.97, 8477.63, 3571.37, 3041.07, 6672, 3122.01, 4750.6],
// 	2003: [5007.21, 2578.03, 6921.29, 2855.23, 2388.38, 6002.54, 2662.08, 4057.4],
// 	2002: [4315, 2150.76, 6018.28, 2324.8, 1940.94, 5458.22, 2348.54, 3637.2]
// });

dataMap.dataGDP = {
	"2011": [{
		'name': "Sydney",
		"value": 16251.93
	}, {
		"name": "Melbourne",
		"value": 11307.28
	}],
	"2012": [{
		'name': "Sydney",
		"value": 14113.58
	}, {
		"name": "Melbourne",
		"value": 9224.46
	}],
	"2013": [{
		'name': "Sydney",
		"value": 12153.03
	}, {
		"name": "Melbourne",
		"value": 7521.85
	}],
}


period_r1_option = {
	baseOption: {
		timeline: {
			axisType: 'category',
			// realtime: false,
			// loop: false,
			autoPlay: true,
			// currentIndex: 2,
			playInterval: 3000,
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
		// calculable: true,
		// grid: {
		// 	top: 80,
		// 	bottom: 100,
		// 	tooltip: {
		// 		trigger: 'axis',
		// 		axisPointer: {
		// 			type: 'shadow',
		// 			label: {
		// 				show: true,
		// 				formatter: function(params) {
		// 					return params.value.replace('\n', '');
		// 				}
		// 			}
		// 		}
		// 	}
		// },
		xAxis: [{
			'type': 'category',
			'axisLabel': {
				'interval': 0,
				rotate: 15
			},
			'data': ['Sydney', 'Melbourne', 'Brisbane', 'Perth (WA)', 'Adelaide',
                                'Gold Coast', 'Canberra', 'Newcastle'],
			splitLine: {
				show: false
			}
		}],
		yAxis: [{
			type: 'value',
			name: '推特比例'
		}],
		series: [{
			name: '推特比例',
			type: 'bar'
		}, ]
	},
	options: [{
			series: [{
				data: dataMap.dataGDP['2011']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2012']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		{
			series: [{
				data: dataMap.dataGDP['2013']
			}, ]
		},
		
	]
};

window.addEventListener('resize', function() {
	period_r1.resize()
})