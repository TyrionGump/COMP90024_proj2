var vaccine_r2 = echarts.init(document.getElementById("vaccine_r2"));

var vaccine_r2_option = {
	tooltip: {
		show: false
	},
	series: [{
		type: 'wordCloud',
		grid: 10,
		sizeRange: [15, 45],
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
		data: [],
	}]
}

window.addEventListener('resize', function() {
	vaccine_r2.resize()
})