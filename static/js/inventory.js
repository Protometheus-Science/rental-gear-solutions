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

function sort_table(column, current) {
	// Style columns
	heads = [...document.getElementsByClassName("table-head")]
	for (var i = heads.length - 1; i >= 0; i--) {
		heads[i].classList.remove("sorted");
	}
	current.classList.add("sorted")

	// Sort rows
	let get_child = x => x.getElementsByClassName(column)[0].id.toUpperCase();
	sorted = [...document.getElementsByClassName("inventory-item")]
	sorted.sort((aid, bid) => {
		let a = get_child(aid)
		let b = get_child(bid)
		if (a == b) {
			return 0
		}
		return (a < b)? 1 : -1;
	})

	let rows = document.getElementsByClassName("inventory-item")
	for (var i = rows.length - 1; i >= 0; i--) {
		rows[i].outerHTML = sorted[i].outerHTML
	}
}

function fuzzy_search(column) {
	console.log("searching " + column)
}