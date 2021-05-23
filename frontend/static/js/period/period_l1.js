var period_l1 = echarts.init(document.getElementById('period_l1'));


var period_l1_option = {
	tooltip: {
	    trigger: 'axis'
	},
	grid: {
	    left: '3%',
	    right: '4%',
	    bottom: '3%',
	    containLabel: true
	},
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [150, 230, 224, 218, 135, 147, 260],
        type: 'line'
    }]
};

window.addEventListener('resize', function() {
	period_l1.resize()
})