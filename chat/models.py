from django.db import models
from datetime import datetime
from user_management.models import User

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=200, default="", null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_updated = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class RoomUser(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='roomuser_room')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='roomuser_user')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_updated = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.room.name + '__' + self.user.name


class Chat(models.Model):
    message = models.CharField(max_length=200, default="", null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='chat_room')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='chat_user')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_updated = models.DateTimeField(default=datetime.now, blank=True)

    # def __str__(self):
    #     return self.room.name + '__' + self.user.name
