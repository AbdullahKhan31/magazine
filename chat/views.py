import pdb
from django.shortcuts import render, redirect
from chat import models
from django.contrib.auth.decorators import login_required
from chat.forms import AddRoomForm


def index(request):
    current_user = request.user
    all_rooms = models.Room.objects.all()
    page_data = {
        'rooms': all_rooms
    }
    return render(request, 'Chatroom/index.html', page_data)


def open_chat_room(request, room_id):
    current_user = request.user
    room = models.Room.objects.get(pk=room_id)
    chats = models.Chat.objects.filter(room=room)
    room_user = models.RoomUser(room=room, user=current_user)
    room_user.save()

    page_data = {
        'room': room,
        'chats': chats
    }
    return render(request, 'Chatroom/room.html', page_data)


def leave_chat_room(request, room_id):
    current_user = request.user
    room = models.Room(pk=room_id)
    models.RoomUser.objects.get(room=room, user=current_user).delete()
    return redirect('Chat:index')


@login_required
def add_room(request):
    context = {'page_title': 'Add Room'}

    if request.method == 'GET':
        form = AddRoomForm()
        context['form'] = form

        return render(request, 'Chatroom/add-room.html', context)

    elif request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('Chat:index')
        # else return to same page with errors
        return render(request, 'Chatroom/add-room.html', context)
