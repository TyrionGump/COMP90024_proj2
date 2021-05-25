var language_r1 = echarts.init(document.getElementById('language_r1'));

var language_r1_option = {
	grid: {
		top: '5%',
		left: '0%',
		right: '0%',
		bottom: '0%',
		show: false,
		containLabel: true
	},
	tooltip: {
		trigger: "axis",
		axisPointer: {
			type: "shadow"
		}
	},
	xAxis: {
		type: 'category',
		axisLabel: {
			interval: 0,
			rotate: 15,
			color: "rgba(255, 255, 255, .6)",
			fontSize: 9
		},
		data: ['Sydney', 'Melbourne', 'Brisbane', 'Perth (WA)', 'Adelaide',
			'Gold Coast', 'Canberra', 'Newcastle'
		],
		axisLine: {
			show: false
		},
		splitLine: {
			show: false
		},
	},
	yAxis: {
		type: 'value',
		axisLabel: {
			color: "rgba(255, 255, 255, .6)",
			fontSize: 10
		},
		axisLine: {
			lineStyle: {
				color: "rgba(255, 255, 255, .1)",
				width: 1
			}
		},
		splitLine: {
			lineStyle: {
				color: "rgba(255, 255, 255, .1)",
				width: 1
			}
		},
	},
	series: [{
		name: "Sort Rate",
		data: [2, 3, 4],
		type: 'bar'
	}]
};

window.addEventListener('resize', function() {
	language_r1.resize()
})
