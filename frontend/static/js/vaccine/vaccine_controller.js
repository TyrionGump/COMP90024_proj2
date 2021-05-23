function get_vaccine_l1_data() {
	$.ajax({
		url: "/vaccine/l1",
		success: function(data) {
			vaccine_l1.clear();
			vaccine_l1_option.xAxis.data = data.xAxis
			vaccine_l1_option.series[0].data = data.data;
			vaccine_l1.setOption(vaccine_l1_option);
		},
		error: function() {
			alert("Error: cannot get data of vaccine l1")
		}
	})
}

function get_vaccine_l2_data() {
	$.ajax({
		url: "/vaccine/l2",
		success: function(data) {
			vaccine_l2.clear();
			vaccine_l2_option.legend.data = data.legend;
			vaccine_l2_option.xAxis.data = data.xAxis;
			for (var i = 0; i < data.legend.length; i++) {
				vaccine_l2_option.series[i].name = data.legend[i];
				vaccine_l2_option.series[i].data = data.data[i];
			}
			vaccine_l2.setOption(vaccine_l2_option);
		},
		error: function() {
			alert("Error: cannot get data of vaccine l2")
		}
	})
}

function get_vaccine_c1_data() {
	$.ajax({
		url: "/vaccine/c1",
		success: function(data) {
			vaccine_c1_scatter_option.series[0].name = data.data_name
			vaccine_c1_scatter_option.series[0].data = data.data
			vaccine_c1_scatter.setOption(vaccine_c1_scatter_option)
		},
		error: function() {
			alert("Error: cannot get data of vaccine c1")
		}
	})
}

function get_vaccine_r1_data() {
	$.ajax({
		url: "/vaccine/r1",
		success: function(data) {
			vaccine_r1.clear();
			vaccine_r1_option.legend.data = data.legend
			for (var i = 0; i < data.legend.length; i++) {
				vaccine_r1_option.series[i].name = data.legend[i];
				vaccine_r1_option.series[i].data = data.data[i];
			}
			vaccine_r1.setOption(vaccine_r1_option)
		},
		error: function() {
			alert('Error: cannot get data of source r1')
		}
	})
}


function get_vaccine_r2_data() {
	$.ajax({
		url: "/vaccine/r2",
		success: function(data) {
			vaccine_r2.clear();
			vaccine_r2_option.series[0].data = data
			vaccine_r2.setOption(vaccine_r2_option)
		},
		error: function() {
			alert('Error: cannot get data of source r2')
		}
	})
}

get_vaccine_l1_data()
get_vaccine_l2_data()
get_vaccine_c1_data()
get_vaccine_r1_data()
get_vaccine_r2_data()