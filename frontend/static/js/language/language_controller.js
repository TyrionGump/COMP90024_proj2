function get_language_l1_data() {
	$.ajax({
		url: "/language/l1",
		success: function(data) {
			language_l1.clear()
			language_l1_option.options[0].series[0].data = data.Sydney
			language_l1_option.options[0].series[1].data = data.Melbourne
			language_l1_option.options[0].series[2].data = data.Brisbane
			language_l1_option.options[0].series[3].data = data.Perth
			language_l1_option.options[1].series[0].data = data.Adelaide
			language_l1_option.options[1].series[1].data = data.GoldCoast
			language_l1_option.options[1].series[2].data = data.Canberra
			language_l1_option.options[1].series[3].data = data.Newcastle
			language_l1.setOption(language_l1_option)
		},
		error: function() {
			alert("Error: cannot get data of language l1")
		}
	})
}

function get_language_l2_data() {
	$.ajax({
		url: "/language/l2",
		success: function(data) {
			language_l2.clear();
			language_l2_option.legend.data = data.legend;
			language_l2_option.xAxis[0].data = data.xAxis;
			for (var i = 0; i < 2; i++) {
				language_l2_option.series[i].name = data.legend[i];
				language_l2_option.series[i].data = data.data[i];
			}
			language_l2.setOption(language_l2_option);
			
		},
		error: function() {
			alert("Error: cannot get data of language l2")
		}
	})
}

function get_language_c1_data() {
	$.ajax({
		url: "/language/c1",
		success: function(data) {
			language_c1_scatter_option.series[0].name = data.data_name
			language_c1_scatter_option.series[0].data = data.data
			language_c1_scatter.setOption(language_c1_scatter_option)
		},
		error: function() {
			alert("Error: cannot get data of language c1")
		}
	})
}

function get_language_r1_data(city) {
	$.ajax({
		url: "/language/r1",
		type: "post",
		data: city,
		success: function(data) {
			language_r1.clear();
			city_name = city.name
			language_r1_option.series[0].data = data[city_name]['data']
			language_r1_option.xAxis.data = data[city_name]['xAxis']
			language_r1.setOption(language_r1_option)
		},
		error: function() {
			alert('Error: cannot get data of language r1')
		}
	})
}

var sydney_wordcloud_data = document.getElementById('Sydney_wordcloud');
sydney_wordcloud_data.addEventListener("click", function() {
	get_language_r1_data({"name": "Sydney"})
})
var melbourne_wordcloud_data = document.getElementById('Melbourne_wordcloud');
melbourne_wordcloud_data.addEventListener("click", function() {
	get_language_r1_data({"name": "Melbourne"})
})
var brisbane_wordcloud_data = document.getElementById('Brisbane_wordcloud');
brisbane_wordcloud_data.addEventListener("click", function() {
	get_language_r1_data({"name": "Brisbane"})
})
var adelaide_wordcloud_data = document.getElementById('Adelaide_wordcloud');
adelaide_wordcloud_data.addEventListener("click", function() {
	get_language_r1_data({"name": "Adelaide"})
})



function get_language_r2_data() {
	$.ajax({
		url: "/language/r2",
		success: function(data) {
			language_r2.clear();
			language_r2_option.series[0].data = data
			language_r2.setOption(language_r2_option)
		},
		error: function() {
			alert('Error: cannot get data of language r2')
		}
	})
}


get_language_l1_data()
get_language_l2_data()
get_language_c1_data()
get_language_r1_data({"name": "Sydney"})
get_language_r2_data()