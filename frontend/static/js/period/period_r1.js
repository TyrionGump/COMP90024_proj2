var period_r1 = echarts.init(document.getElementById('period_r1'));
var period_r1_option;

period_r1_option = {
	baseOption: {
		timeline: {
			axisType: 'category',
			// realtime: false,
			// loop: false,
			autoPlay: true,
			playInterval: 1500,
			// controlStyle: {
			//     position: 'left'
			// },
			data: [
				'00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'
			
			],
			// label: {
			// 	formatter: function(s) {
			// 		return (new Date(s)).getFullYear();
			// 	}
			// }
		},
		color: ["#2f89cf"],
		grid: {
			top: '5%',
			left: '0%',
			right: '0%',
			bottom: '15%',
			show: false,
			containLabel: true
		},
		tooltip: {
			trigger: "axis",
			axisPointer: {
				type: "shadow"
			}
		},
		xAxis: [{
			type: 'category',
			axisLabel: {
				interval: 0,
				rotate: 15,
				color: "rgba(255, 255, 255, .6)",
				fontSize: 9	
			},
			data: ['Sydney', 'Melbourne', 'Brisbane', 'Perth (WA)', 'Adelaide',
                                'Gold Coast', 'Canberra', 'Newcastle'],
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
		series: [{
			name: 'Twiter Rate',
			type: 'bar',
			barWidth: "50%",
			itemStyle: {
				barBorderRadius: 3
			}
		}, ]
	},
	options: [{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		{
			series: [{
				data: []
			}, ]
		},
		
	]
};

window.addEventListener('resize', function() {
	period_r1.resize()
})