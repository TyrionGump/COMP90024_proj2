function get_period_l1_data() {
	$.ajax({
		url: "/period/l1",
		success: function(data) {
			period_l1.clear()
			period_l1_option.xAxis.data = data.xAxis;
			period_l1_option.series[0].data = data.data;
			period_l1.setOption(period_l1_option)
		},
		error: function() {
			alert("Error: cannot get data of period l1")
		}
	})
}

function get_period_l2_data() {
	$.ajax({
		url: "/period/l2",
		success: function(data) {
			period_l2.clear();
			period_l2_option.legend.data = data.legend;
			period_l2_option.xAxis.data = data.xAxis;
			for (var i = 0; i < data.legend.length; i++) {
				period_l2_option.series[i].name = data.legend[i];
				period_l2_option.series[i].data = data.data[i];
			}
			period_l2.setOption(period_l2_option);
		},
		error: function() {
			alert("Error: cannot get data of period l2")
		}
	})
}

function get_period_c1_data() {
	$.ajax({
		url: "/period/c1",
		success: function(data) {
			for (var i = 0; i < 23; i++) {
				period_c1_scatter_option.options[i].series[0].data = data.data[i];
				period_c1_scatter.setOption(period_c1_scatter_option);
			}
			
		},
		error: function() {
			alert("Error: cannot get data of period c1")
		}
	})
}

function get_period_r1_data() {

	$.ajax({
		url: "/period/r1",
		success: function(data) {
			period_r1.clear()
			series_data = data.data
			periods = data.periods
			period_r1_option.baseOption.timeline.data = periods
			period_r1_option.baseOption.xAxis.data = data.Axis
			period_idx = ['0 0', '0 1', '0 2', '0 3', '0 4', '0 5', '0 6', '0 7', '0 8', '0 9', '1 0', '1 1', '1 2',
             '1 3', '1 4', '1 5', '1 6', '1 7', '1 8', '1 9', '2 0', '2 1', '2 2', '2 3']
			for (var i = 0; i < 24; i++) {
				period_r1_option.options[i].series[0].data = series_data[i][period_idx[i]];
			}
			period_r1.setOption(period_r1_option);
		},
		error: function() {
			alert('Error: cannot get data of period r1')
		}
	})
}

function get_period_r2_data(time) {
	$.ajax({
		url: "/period/r2",
		type: "post",
		data: time,
		success: function(data) {
			period_r2.clear();
			time_name = time.name
			period_r2_option.series[0].data = data[time_name]
			period_r2.setOption(period_r2_option)
		},
		error: function() {
			alert('Error: cannot get data of period r2')
		}
	})
}
var morning_wordcloud_data = document.getElementById('morning_wordcloud');
morning_wordcloud_data.addEventListener("click", function() {
	get_period_r2_data({"name": "morning"})
})
var noon_wordcloud_data = document.getElementById('noon_wordcloud');
noon_wordcloud_data.addEventListener("click", function() {
	get_period_r2_data({"name": "afternoon"})
})
var evening_wordcloud_data = document.getElementById('evening_wordcloud');
evening_wordcloud_data.addEventListener("click", function() {
	get_period_r2_data({"name": "evening"})
})


get_period_l1_data()
get_period_l2_data()
get_period_c1_data()
get_period_r1_data()
get_period_r2_data({"name": "morning"})

