// Todo::
// This file is included in chat_layout.html, so it will give errors in other Chat_layoyt.html pages as body
// elements might not exist there. But since jQuery is loaded in  Chat_layoyt.html, cannot load this in room.html
// before jQuery init.

var last_message_id = null;

$(document).ready(function () {
    last_message_id = $("input[name='chat_id']").last().val();
    $('#chat_box').scrollTop($('#chat_box')[0].scrollHeight);
    // Every 1 second, new messages are fetch.
    window.setInterval(function () {
        getGetNewMessages()
    }, 1000);
});


// Sets CSRF Token
$(function () {
    $.ajaxSetup({
        headers: {"X-CSRFToken": getCookie("csrftoken")}
    });
});

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

// Send Button on Click Listener
$('#sendBtn').click( function(){
    message = $('#chat_message').val();
    if (message) {
        last_message = "<div class='mine'><span class='sender'>" + user_name + "</span><br/>" + message;
        last_message += "<br /><span style='font-size:0.6em;' id='msg_status'><i class=\"fas fa-circle-notch fa-spin\"></i></span></div><br/><br/>"
        $('.chat_box').append(last_message);
        let data = {"message": message, "room": room_id, "user": user_id}
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/chat/send-message',
            contentType: 'application/json',
            data: JSON.stringify(data),
        }).done(function (response) {
            $('#msg_status').text('Sent')
            last_message_id = response.id;
        }).fail(function (msg) {
            $('#msg_status').text('Failed')
        }).always(function (msg) {
            $('#chat_message').val('');
            $('#chat_box').scrollTop($('#chat_box')[0].scrollHeight);
        });
    }
});



// Fetch new messages from server 'last_message_id' ownards.
function getGetNewMessages() {
    // Change to production URL before deoplyment.
		
    url = 'http://localhost:8000/chat/latest-chat/' + room_id + '/' + last_message_id;
    $.get(url, function (data, status) {
        $.each(data, function (i, item) {
            last_message_id = item.id;
            msg_time = item.created_at.split('T')[0]
            messageData = "<div class='other'><span class='sender'>" + item.user.username + "("+msg_time+")</span><br/>" + item.message;
            messageData += "<br /></div><br/><br/>"
            $('#chat_box').append(messageData);
            $('#chat_box').scrollTop($('#chat_box')[0].scrollHeight);
        });
    });
}
