function toggle_filters() {
	if ($('#filters').style("display") == "none") {
		$('#filters').style("display", "table-row");
	}

	else {
		$('#filters').hide();
	}
}