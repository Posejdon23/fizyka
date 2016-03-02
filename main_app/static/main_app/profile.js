function show_fields(visibility) {
    opposite = "visible"
    if(visibility == "visible"){
        opposite = "hidden"
    }
    document.getElementById("id_first_name").style.visibility = opposite;
    document.getElementById("id_last_name").style.visibility = opposite;
    document.getElementById("submit").style.visibility = visibility;
}