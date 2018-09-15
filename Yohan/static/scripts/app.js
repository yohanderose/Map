function helloWorld() {
    return "Hello World"
}

function addCoordinate(latitude, longitude, label) {
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

function getCoordinates() {
    var coordinates = $.get({
        url: "api/locations"
    });

    // Put logic in here to render points on google maps canvas
    // Use something like

    var myLatLng = {lat: -25.363, lng: 131.044};

     var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      title: 'Hello World!'
    });
}