var vaccine_l2 = echarts.init(document.getElementById('vaccine_l2'));


var vaccine_l2_option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        textStyle: {
			color: "white"
		},
    },
    toolbox: {
		top: "0%",
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
    	type: 'category',
    	axisLabel: {
    		color: "rgba(255, 255, 255, .6)",
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
    	top: '15%',
    	left: '2%',
    	right: '3%',
    	bottom: '0%',
    	show: false,
    	borderColor: ' #012f4a',
    	containLabel: true
    },
	color: ["#00f2f1", "#ed3f35"],
    series: [
        {
            type: 'line',
            data: [120, 132, 101, 134, 90, 230, 210],
			smooth: true
        },
        {
            type: 'line',
            data: [220, 182, 191, 234, 290, 330, 310],
			smooth: true
        }
    ]
};

window.addEventListener('resize', function() {
	vaccine_l2.resize()
})