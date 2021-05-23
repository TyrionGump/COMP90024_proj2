function get_source_l1_data() {
	$.ajax({
		url: "/source/l1",
		success: function(data) {
			source_l1.clear();
			source_l1_option.legend.data = data.legend;
			source_l1_option.xAxis.data = data.xAxis;
			for (var i = 0; i < data.legend.length; i++) {
				source_l1_option.series[i].name = data.legend[i];
				source_l1_option.series[i].data = data.data[i];
			}
			source_l1.setOption(source_l1_option);
		},
		error: function() {
			alert("Error: cannot get data of source l1")
		}
	})
}

function get_source_l2_data() {
	$.ajax({
		url: "/source/l2",
		success: function(data) {
			source_l2.clear();
			source_l2_option.legend.data = data.legend;
			source_l2_option.xAxis[0].data = data.xAxis;
			for (var i = 0; i < data.legend.length; i++) {
				source_l2_option.series[i].name = data.legend[i];
				source_l2_option.series[i].data = data.data[i];
			}
			source_l2.setOption(source_l2_option);
			
		},
		error: function() {
			alert("Error: cannot get data of source l2")
		}
	})
}

function get_source_c12_scatter_data() {
	$.ajax({
		url: "/source/c12",
		success: function(data) {
			source_c1_scatter_option.series[0].name = 'Average polarity for Android'
			source_c1_scatter_option.series[0].data = data.android
			source_c1_scatter.setOption(source_c1_scatter_option)
			source_c2_scatter_option.series[0].name = 'Average polarity for IOS'
			source_c2_scatter_option.series[0].data = data.android
			source_c2_scatter.setOption(source_c2_scatter_option)
		},
		error: function() {
			alert("Error: cannot get data of source c12")
		}
	})
}




function get_source_r1_data() {
	$.ajax({
		url: "/source/r1",
		success: function(data) {
			source_r1.clear();
			source_r1_option.legend.data = data.legend;
			source_r1_option.yAxis.data = data.yAxis
			for (var i = 0; i < data.legend.length; i++) {
				source_r1_option.series[i].name = data.legend[i];
				source_r1_option.series[i].data = data.data[i];
			}
			source_r1.setOption(source_r1_option)
			
		},
		error: function() {
			alert('Error: cannot get data of source r1')
		}
	})
}

function get_source_r2_data(device) {
	$.ajax({
		url: "/source/r2",
		type: "post",
		data: device,
		success: function(data) {
			source_r2.clear();
			device_name = device.name
			source_r2_option.series[0].data = data[device_name]
			source_r2.setOption(source_r2_option)
		},
		error: function() {
			alert('Error: cannot get data of source r2')
		}
	})
}

var android_wordcloud_data = document.getElementById('Android_wordcloud');
android_wordcloud_data.addEventListener("click", function() {
	get_source_r2_data({"name": "android"})
})

var ios_wordcloud_data = document.getElementById('IOS_wordcloud');
ios_wordcloud_data.addEventListener("click", function() {
	get_source_r2_data({"name": "ios"})
})


get_source_l1_data();
get_source_l2_data();
get_source_c12_scatter_data();
get_source_r1_data();
get_source_r2_data({"name": "android"});
