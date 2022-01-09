var last_data;
var temp = 0;
var hum = 0;
var btn = 0;
var socket = io();

socket.on('connect', function () {
    socket.emit('message', {data: 'I\'m connected!'});
});

socket.on("new_data", data => {
    temp = data.temp;
    hum = data.hum;
    btn = data.btn;
    console.log(data);
});

socket.on("last_data", data => {
    last_data = data;
});

