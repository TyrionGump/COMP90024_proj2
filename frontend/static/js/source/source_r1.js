var source_r1 = echarts.init(document.getElementById('source_r1'));

var source_r1_option = {
    // title: {
    //     text: '世界人口总量',
    //     subtext: '数据来自网络'
    // },
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
		top: "10%",
        left: '1%',
        right: '2%',
        bottom: '0%',
        containLabel: true
    },
    xAxis: {
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
		boundaryGap: [0, 0.01]
    },
	
    yAxis: {
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
    },
    series: [
        {
            type: 'bar',
            data: [18203, 23489, 29034, 104970, 131744, 630230],
			itemStyle: {
				barBorderRadius: 3
			}
        },
        {
            type: 'bar',
            data: [19325, 23438, 31000, 121594, 134141, 681807],
			itemStyle: {
				barBorderRadius: 3
			}
        }
    ]
};

window.addEventListener('resize', function() {
	source_r1.resize()
})