var source_l2 = echarts.init(document.getElementById('source_l2'));

var source_l2_option = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        textStyle: {
    		color: "white"
    	},
    },
	grid: {
		top: '15%',
		left: '0%',
		right: '0%',
		bottom: '0%',
		show: false,
		containLabel: true
	},
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    xAxis: [{
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
    }],
    yAxis: [{
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
    }],
    series: [
        {
            type: 'bar',
            barGap: 0,
            emphasis: {
                focus: 'series'
            },
            data: [320, 332],
			barWidth: "30%",
			itemStyle: {
				barBorderRadius: 3
			}
        },
        {
            type: 'bar',
            emphasis: {
                focus: 'series'
            },
            data: [220, 182],
			barWidth: "30%",
			itemStyle: {
				barBorderRadius: 3
			}
        }
    ]
};

window.addEventListener('resize', function() {
	source_l2.resize()
})
