function toggle_filters() {
	if ($('#filters').style("display") == "none") {
		$('#filters').style("display", "table-row");
	}

	else {
		$('#filters').hide();
	}
}

function update_filters() {
	filters = [...document.getElementsByClassName("filter-parameter")].map(x => x.value)
	items = [...document.getElementsByClassName("inventory-item")]
	for (var i = items.length - 1; i >= 0; i--) {
		items[i].style.display = "none";
		if (filters.includes(items[i])) {
			items[i].style.display = "table-row";
		}
	}
}