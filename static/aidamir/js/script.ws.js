var last_data;
var temp = 0;
var light = 0;
var range = 0;
var hum = 0;

var socket = io();

socket.on('connect', function () {
    socket.emit('message', {data: 'I\'m connected!'});
});

socket.on("new_data", data => {
    data = JSON.parse(data);

    socket.emit('message', {data: 'Received data: ' + data});
    if ("temp" in data) {
        console.log("New temp data: " + data.temp);
        temp = data.temp;
    }
    if ("light" in data) {
        console.log("New light data: " + data.light);
        light = data.light;
    }
    if ("range" in data) {
        console.log("New range data: " + data.range);
        range = data.range;
    }
    if ("hum" in data) {
        console.log("New humidity data: " + data.hum);
        hum = data.hum;
    }

});

