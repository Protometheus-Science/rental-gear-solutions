function toggle_filters() {
	if ($('#filters').style("display") == "none") {
		$('#filters').style("display", "table-row");
	}

	else {
		$('#filters').hide();
	}
}

function update_filters() {
	// Pull all filters into array and get the values of checked ones
	filters = [...document.getElementsByClassName("filter-parameter")].filter(x => x.checked).map(x => x.value)

	// Pull all items
	items = [...document.getElementsByClassName("inventory-item")]
	
	for (var i = items.length - 1; i >= 0; i--) {
		// default to hidden
		items[i].style.display = "none";
		
		// Pull item ids
		
		let ids = [...items[i].childNodes].map(x => x.id);
		// Find matches between ids and search paramets
		let match = ids.map(x => filters.includes(x)).includes(true)

		if (match) {
			items[i].style.display = "table-row";
		}
	}
}