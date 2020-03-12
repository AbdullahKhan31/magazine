from rest_framework import serializers
from chat.models import Room, RoomUser, Chat
from user_management.api.serializers import UserSerializer


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'description', 'status', 'created_at', 'last_updated')

    def to_representation(self, instance):
        representation = super(RoomSerializer, self).to_representation(instance)
        return representation


class RoomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomUser
        fields = ('id', 'room', 'user', 'status', 'created_at', 'last_updated')

    def to_representation(self, instance):
        representation = super(RoomUserSerializer, self).to_representation(instance)
        representation['room'] = RoomSerializer(instance.room).data
        representation['user'] = UserSerializer(instance.user).data
        return representation


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'message', 'room', 'user', 'created_at', 'last_updated')

    def to_representation(self, instance):
        representation = super(ChatSerializer, self).to_representation(instance)
        representation['room'] = RoomSerializer(instance.room).data
        representation['user'] = UserSerializer(instance.user).data
        return representation

