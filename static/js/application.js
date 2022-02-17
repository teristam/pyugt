
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var text_received = [];

    //receive details from server
    socket.on('text', function(msg) {
        console.log("Received text" + msg.text);
        //…maintain a list of ten numbers
        if (text_received.length >= 5){
            text_received.shift()
        }            
        text_received.push(msg.text);
        text_string = '';
        for (var i = 0; i < text_received.length; i++){
            text_string = text_string + '<p>' + text_received[i] + '</p> <hr/>';
        }
        $('#log').html(text_string);
    });

});