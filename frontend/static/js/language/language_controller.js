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

function get_language_r2_data() {
	$.ajax({
		url: "/language/r2",
		success: function(data) {
			language_r2.clear();
			language_r2_option.series[0].data = data
			language_r2.setOption(language_r2_option)
		},
		error: function() {
			alert('Error: cannot get data of period r2')
		}
	})
}

var sydney_wordcloud_data = document.getElementById('sydney_wordcloud')
sydney_wordcloud_data.addEventListener("click", function() {
	get_language_r2_data({"name": "Sydney"})
})

var melbourne_wordcloud_data = document.getElementById("melbourne_wordcloud")
melbourne_wordcloud_data.addEventListener("click", function() {
	get_language_r2_data({"name": "Melbourne"})
})

var brisbane_wordcloud_data = document.getElementById("brisbane_wordcloud")
brisbane_wordcloud_data.addEventListener("click", function() {
	get_language_r2_data({"name": "Brisbane"})
})

var perth_wordcloud_data = document.getElementById("perth_wordcloud")
perth_wordcloud_data.addEventListener("click", function() {
	get_language_r2_data({"name": "Perth"})
})

var adelaide_wordcloud_data = document.getElementById("adelaide_wordcloud")
adelaide_wordcloud_data.addEventListener("click", function() {
	get_language_r2_data({"name": "Adelaide"})
})

var goldCoast_wordcloud_data = document.getElementById("goldCoast_wordcloud")
goldCoast_wordcloud_data.addEventListener("click", function() {
	get_language_r2_data({"name": "GoldCoast"})
})

var canberra_wordcloud_data = document.getElementById("canberra_wordcloud")
canberra_wordcloud_data.addEventListener("click", function() {
	get_language_r2_data({"name": "Canberra"})
})

var newCastle_wordcloud_data = document.getElementById("newcastle_wordcloud")
newCastle_wordcloud_data.addEventListener("click", function() {
	get_language_r2_data({"name": "Newcastle"})
})



get_language_l1_data()
get_language_l2_data()
get_language_c1_data()
get_language_r2_data()