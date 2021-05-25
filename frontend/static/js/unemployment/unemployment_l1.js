var unemployment_l1 = echarts.init(document.getElementById('unemployment_l1'), 'macarons');


var unemployment_l1_option = {
	tooltip: {
		trigger: 'axis'
	},
	xAxis: {
		type: 'category',
		axisLabel: {
			color: "rgba(255, 255, 255, .6)",
			fontSize: 10
		},
		axisLine: {
			show:false
		},
		splitLine: {
			show: false
		},
		axisTick: {
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
	grid: {
		top: '2%',
		left: '2%',
		right: '3%',
		bottom: '0%',
		show: false,
		borderColor: ' #012f4a',
		containLabel: true
	},

	series: [{
		data: [150, 230, 224, 218, 135, 147, 260],
		type: 'line',
		smooth: true
	}]
};

window.addEventListener('resize', function() {
	unemployment_l1.resize()
})
