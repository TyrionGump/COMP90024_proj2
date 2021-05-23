var vaccine_l1 = echarts.init(document.getElementById('vaccine_l1'));


var vaccine_l1_option = {
	tooltip: {
	    trigger: 'axis'
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
	vaccine_l1.resize()
})