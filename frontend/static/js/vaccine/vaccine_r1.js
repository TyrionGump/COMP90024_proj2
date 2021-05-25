var vaccine_r1 = echarts.init(document.getElementById("vaccine_r1"));
var vaccine_r1_option = {
	legend: {
	    textStyle: {
	    	color: "white",
			fontSize: 9
	    },
	},
    xAxis: {
    	axisLabel: {
    		color: "rgba(255, 255, 255, .6)",
    		fontSize: 10
    	},
    	axisTick: {
    		show: false
    	},
    	axisLine: {
    		show: false
    	},
		splitLine: {
			lineStyle: {
				color: "rgba(255, 255, 255, .1)",
			}
		}
    },
    yAxis: {
    	axisLabel: {
    		color: "rgba(255, 255, 255, .6)",
    		fontSize: 10
    	},
    	axisTick: {
    		show: false
    	},
    	axisLine: {
    		show: false
    	},
    	splitLine: {
    		lineStyle: {
    			color: "rgba(255, 255, 255, .1)",
    		}
    	}
    },
	
	grid: {
		top: '20%',
		left: '2%',
		right: '2%',
		bottom: '0%',
		show: true,
		borderColor: "rgba(255, 255, 255, .1)",
		containLabel: true
	},
    series: [{
        symbolSize: 10,
        data: [
            [10.0, 8.04],
            [8.07, 6.95],
            [13.0, 7.58],
            [9.05, 8.81],
        ],
        type: 'scatter'
    },
	{
	    symbolSize: 10,
	    data: [
	        [9, 7],
	        [7, 6],
	        [11, 6],
	        [8, 7],
	    ],
	    type: 'scatter'
	},
	{
	    symbolSize: 10,
	    data: [
	        [11, 9],
	        [9, 8],
	        [14, 9],
	        [10, 9],
	    ],
	    type: 'scatter'
	},
	{
	    symbolSize: 10,
	    data: [
	        [11, 13],
	        [13, 6],
	        [8, 12],
	        [5, 15],
	    ],
	    type: 'scatter'
	},
	{
	    symbolSize: 10,
	    data: [
	        [10.0, 5],
	        [8, 9],
	        [12, 16],
	        [14, 13],
	    ],
	    type: 'scatter'
	},
	{
	    symbolSize: 10,
	    data: [
	        [11, 14],
	        [9, 8],
	        [5, 13],
	        [10, 7],
	    ],
	    type: 'scatter'
	}]
}; 
window.addEventListener('resize', function() {
	vaccine_r1.resize()
})