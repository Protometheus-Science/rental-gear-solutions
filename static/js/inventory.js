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
		let matches = filters.filter(x => ids.includes(x)).length

		if (matches == filters.length) {
			items[i].style.display = "table-row";
		}
	}
}

function sort_table(column) {
	rows = [...document.getElementsByClassName("inventory-item")]
	sorted = rows.sort(a, b => {
		return (a > b)? 1 : -1;
	})
	for (var i = rows.length - 1; i >= 0; i--) {
		rows[i] = sorted[i]
	}
}

function fuzzy_search(column) {
	console.log("searching " + column)
}