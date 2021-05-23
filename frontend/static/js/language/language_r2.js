var language_r2 = echarts.init(document.getElementById("language_r2"));
var ddd = [{
	'name': '肺炎',
	"value": '1234670'
}, {
	"name": '实时',
	"value": "1234670"
}, {
	"name": "新型",
	"value": '1234570'
}]

var language_r2_option = {
	title: {
		text: "今日疫情热搜",
		textStyle: {
			color: 'white',
		},
		left: 'left'
	},
	tooltip: {
		show: false
	},
	series: [{
		type: 'wordCloud',
		gridSize: 10,
		sizeRange: [30, 200],
		rotationRange: [-45, 0, 45, 90],
		textStyle: {
			color: function() {
				// Random color
				return 'rgb(' + [
					Math.round(Math.random() * 255),
					Math.round(Math.random() * 255),
					Math.round(Math.random() * 255)
				].join(',') + ')';
			}

		},
		emphasis: {
			focus: 'self',

			textStyle: {
				shadowBlur: 10,
				shadowColor: '#333'
			}
		},
		right: null,
		bottom: null,
		data: ddd
	}]
}
language_r2.setOption(language_r2_option);
window.addEventListener('resize', function() {
	language_r2.resize()
})