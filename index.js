function submit() {
    var result = []
    var name = document.getElementById("name")
    result.push(name.value)
    var favRamen = document.getElementById("favRamen")
    result.push(favRamen.value)
    var spicy = document.getElementsByName("spicy")
    for (var i = 0; i < spicy.length; i++) {
        if (spicy[i].checked)
            result.push(spicy[i].value)
    }
    var style = document.getElementsByName("style")
    for (var i = 0; i < style.length; i++) {
        if (style[i].checked)
            result.push(style[i].value)
    }
    var protein = document.getElementsByName("protein")
    for (var i = 0; i < protein.length; i++) {
        if (protein[i].checked)
            result.push(protein[i].value)
    }
    var country = document.getElementById("country")
    result.push(country.value)
    console.log(result)
}

function cancel() {
    var name = document.getElementById("name")
    name.value = ""
    var favRamen = document.getElementById("favRamen")
    favRamen.value = ""
    var spicy = document.getElementsByName("spicy")
    for (var i = 0; i < spicy.length; i++) {
        if (spicy[i].checked)
            spicy[i].checked = false
    }
    var style = document.getElementsByName("style")
    for (var i = 0; i < style.length; i++) {
        if (style[i].checked)
            style[i].checked = false
    }
    var protein = document.getElementsByName("protein")
    for (var i = 0; i < protein.length; i++) {
        if (protein[i].checked)
            protein[i].checked = false
    }
    var country = document.getElementById("country")
    country.value = ""
}