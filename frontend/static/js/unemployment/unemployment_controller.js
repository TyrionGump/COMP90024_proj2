function get_unemployment_l1_data() {
	$.ajax({
		url: "/unemployment/l1",
		success: function(data) {
			unemployment_l1.clear();
			unemployment_l1_option.xAxis.data = data.xAxis
			unemployment_l1_option.series[0].data = data.data;
			unemployment_l1.setOption(unemployment_l1_option);
		},
		error: function() {
			alert("Error: cannot get data of unemployment l1")
		}
	})
}

function get_unemployment_l2_data() {
	$.ajax({
		url: "/unemployment/l2",
		success: function(data) {
			unemployment_l2.clear();
			unemployment_l2_option.legend.data = data.legend;
			unemployment_l2_option.xAxis.data = data.xAxis;
			for (var i = 0; i < data.legend.length; i++) {
				unemployment_l2_option.series[i].name = data.legend[i];
				unemployment_l2_option.series[i].data = data.data[i];
			}
			unemployment_l2.setOption(unemployment_l2_option);
		},
		error: function() {
			alert("Error: cannot get data of unemployment l2")
		}
	})
}

function get_unemployment_c1_data() {
	$.ajax({
		url: "/unemployment/c1",
		success: function(data) {
			unemployment_c1_scatter_option.series[0].name = data.data_name
			unemployment_c1_scatter_option.series[0].data = data.data
			unemployment_c1_scatter.setOption(unemployment_c1_scatter_option)
		},
		error: function() {
			alert("Error: cannot get data of unemployment c1")
		}
	})
}

function get_unemployment_r1_data() {
	$.ajax({
		url: "/unemployment/r1",
		success: function(data) {
			unemployment_r1.clear();
			unemployment_r1_option.legend.data = data.legend;
			
			for (var i = 0; i < data.legend.length; i++) {
				unemployment_r1_option.xAxis[i].data = data.xAxis[i];
				unemployment_r1_option.series[i].name = data.legend[i];
				unemployment_r1_option.series[i].data = data.data[i];
			}
			unemployment_r1.setOption(unemployment_r1_option);
		},
		error: function() {
			alert("Error: cannot get data of unemployment r1")
		}
	})
}

function get_unemployment_r2_data() {
	$.ajax({
		url: "/unemployment/r2",
		success: function(data) {
			unemployment_r2.clear();
			unemployment_r2_option.series[0].data = data
			unemployment_r2.setOption(unemployment_r2_option)
		},
		error: function() {
			alert('Error: cannot get data of unemployment r2')
		}
	})
}

get_unemployment_l1_data()
get_unemployment_l2_data()
get_unemployment_c1_data()
get_unemployment_r1_data()
get_unemployment_r2_data()