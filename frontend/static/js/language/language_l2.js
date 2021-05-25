var app = {};

var language_l2 = echarts.init(document.getElementById('language_l2'));



var language_l2_option = {
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
	grid: {
		top: '15%',
		left: '0%',
		right: '0%',
		bottom: '0%',
		show: false,
		containLabel: true
	},
    series: [
        {
            name: 'Forest',
            type: 'bar',
            barGap: 0,
            emphasis: {
                focus: 'series'
            },
            data: [320, 332]
        },
        {
            name: 'Steppe',
            type: 'bar',
            emphasis: {
                focus: 'series'
            },
            data: [220, 182]
        }
    ]
};

window.addEventListener('resize', function() {
	language_l2.resize()
})