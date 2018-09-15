function helloWorld() {
    return "Hello World"
}

function addCoordinate(latitude, longitude) {
    console.error(latitude);
    console.error(longitude);
    var data = [{"Latitude": latitude,
                "Longitude": longitude}];
    $.post({
        url: "api/locations",
        data: JSON.stringify(data),
        dataType: "json",
        contentType:"application/json"
    });
}