var unemployment_r1 = echarts.init(document.getElementById('unemployment_r1'));
var colors = ['#5470C6', '#EE6666'];

var unemployment_r1_option = {
    color: colors,

    tooltip: {
        trigger: 'none',
        axisPointer: {
            type: 'cross'
        }
    },
    legend: {
        textStyle: {
        	color: "white"
        },
    },
    grid: {
    	top: '20%',
    	left: '3%',
    	right: '3%',
    	bottom: '0%',
    	show: true,
    	borderColor: "rgba(255, 255, 255, .1)",
    	containLabel: true
    },
    xAxis: [
        {	axisLabel: {
			interval: 0,
			color: "rgba(255, 255, 255, .6)",
			fontSize: 10
		},
            type: 'category',
			splitLine: {
				lineStyle: {
					color: "rgba(255, 255, 255, .1)"
				}
			},
            axisTick: {
				show: false,
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: colors[1]
                }
            },
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return 'Unemployment Rate  ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: ['2016-1', '2016-2', '2016-3', '2016-4', '2016-5', '2016-6', '2016-7', '2016-8', '2016-9', '2016-10', '2016-11', '2016-12']
        },
        {
            type: 'category',
            splitLine: {
            	lineStyle: {
            		color: "rgba(255, 255, 255, .1)"
            		
            	}
            },
            axisTick: {
            	show: false,
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: colors[0]
                }
            },
			axisLabel: {
				interval: 0,
				color: "rgba(255, 255, 255, .6)",
				fontSize: 10
			},
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return 'Unemployment Rate  ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: ['2015-1', '2015-2', '2015-3', '2015-4', '2015-5', '2015-6', '2015-7', '2015-8', '2015-9', '2015-10', '2015-11', '2015-12']
        }
    ],
    yAxis: [
        {
            type: 'value',
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
					color: '#012f4a'
				}
			}
        }
    ],
    series: [
        {
            name: '',
            type: 'line',
            xAxisIndex: 1,
            smooth: true,
            emphasis: {
                focus: 'series'
            },
            data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
        },
        {
            name: '',
            type: 'line',
            smooth: true,
            emphasis: {
                focus: 'series'
            },
            data: [3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7]
        }
    ]
};


window.addEventListener('resize', function() {
	unemployment_r1.resize()
})