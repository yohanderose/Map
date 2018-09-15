function helloWorld() {
    return "Hello World"
}

function addCoordinate(latitude, longitude) {
    console.error(latitude);
    console.error(longitude);
    $.post({
        url: "api/locations",
        data: [{
                "Latitude": latitude,
                "Longitude": longitude
            }],
        dataType: "json"
    });
}