var ec_center_2 = echarts.init(document.getElementById('c2'));
var myData = [
	{name: 'melbourne', value: [144.96316, -37.81422, 10000]},
	{name: 'brisbane', value: [153.021072, -27.470125, 1000]},
]

var ec_center_option_2 = {
    "title": {
        "text": "白云示意图"
    },
    "tooltip": {
        "trigger": "item"
    },
    "toolbox": {
        "show": false,
        "orient": "vertical",
        "left": "right",
        "top": "center",
        "feature": {
            "restore": {},
            "saveAsImage": {}
        }
    },
    "geo": {
        "map": "澳大利亚",
        "roam": false,
        "label": {
            "emphasis": {
                "show": true,
                "textStyle": {
                    "color": "#000"
                }
            }
        },
        "itemStyle": {
            "normal": {
                "areaColor": "#293C55",
                "borderColor": "#fff"
            },
            "emphasis": {
                "areaColor": "yellow"
            }
        },
		aspectScale: 1
    }, 
	series: [{
			name: '销量', // series名称
			type: 'scatter', // series图表类型
			coordinateSystem: 'geo' ,// series坐标系类型
			data: myData,
			symbolSize: function (val) {
				return val[2] / 100;
			}
		}]
}
ec_center_2.setOption(ec_center_option_2)