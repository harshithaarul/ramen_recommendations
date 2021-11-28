function submit() {
    var url = "http://localhost:8000/getRecs";

    var result = []
    var name = document.getElementById("brand")
    result.push(name.value)
    var variety = document.getElementById("variety")
    result.push(variety.value)

    var prevLen = result.length;

    var style = document.getElementsByName("style")
    for (var i = 0; i < style.length; i++) {
        if (style[i].checked)
            result.push(style[i].value)
    }

    if (result.length == prevLen) {
        alert("Select a value for style!");
        return;
    }

    var country = document.getElementById("country")
    result.push(country.value)
    var stars = document.getElementById("stars")
    result.push(stars.value)

    document.getElementById("results").innerText = "Getting your recommendations!";

    var http = new XMLHttpRequest();
    http.open("POST", url);
    http.setRequestHeader("Content-Type", "application/json");
    http.onreadystatechange = function() {
        if (http.readyState == XMLHttpRequest.DONE) {
            var response = JSON.parse(http.responseText);
            document.getElementById("results").innerHTML = "<br><br><p>From your input, we recommend the following:</p><br>";
            for (var ramen in response) {
                document.getElementById("results").innerHTML += "<p>";
                document.getElementById("results").innerHTML += "- " + response[ramen][1];
                document.getElementById("results").innerHTML += " by " + response[ramen][0];
                document.getElementById("results").innerHTML += " comes in a " + response[ramen][2].toLowerCase();
                document.getElementById("results").innerHTML += " from " + response[ramen][3];
                document.getElementById("results").innerHTML += "</p><br>";
            }
            // document.getElementById("results").innerHTML += "</ul>";
        }
    }
    http.send(JSON.stringify(result));
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