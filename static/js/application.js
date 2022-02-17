
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('text', function(msg) {
        console.log("Received text" + msg.text);
        //maintain a list of ten numbers
        // if (numbers_received.length >= 10){
        //     numbers_received.shift()
        // }            
        // numbers_received.push(msg.number);
        // numbers_string = '';
        // for (var i = 0; i < numbers_received.length; i++){
        //     numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        // }
        $('#log').html(msg.text);
    });

});