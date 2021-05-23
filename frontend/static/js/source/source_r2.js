var source_r2 = echarts.init(document.getElementById("source_r2"));
var source_r2_text = [{
	'name': '肺炎',
	"value": '1234670'
}, {
	"name": '实时',
	"value": "1234670"
}, {
	"name": "新型",
	"value": '1234570',
}]

var source_r2_option = {
	title: {
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
		sizeRange: [10, 60],
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
		data: source_r2_text
	}]
}

window.addEventListener('resize', function() {
	source_r2.resize()
})