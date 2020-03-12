from rest_framework import viewsets, status, filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from chat.models import Room, RoomUser, Chat
from chat.api.serializers import RoomSerializer, RoomUserSerializer, ChatSerializer
import json, pdb


class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializer


class RoomUserView(viewsets.ModelViewSet):
    queryset = RoomUser.objects.all().order_by('-id')
    serializer_class = RoomUserSerializer


class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all().order_by('-id')
    serializer_class = ChatSerializer


class RoomAPIView(APIView):
    def get_queryset(self):
        room_id = self.request.query_params.get('room_id')

    def get(self, request, room_id):
        # pdb.set_trace()
        # room_id = self.request.query_params.get('room_id')
        queryset = Chat.objects.filter(room=room_id)
        serialized_data = ChatSerializer(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


class LatestChatAPIView(APIView):
    def get_queryset(self):
        room_id = self.request.query_params.get('room_id')
        chat_id = self.request.query_params.get('chat_id')

    def get(self, request, room_id, chat_id):
        # pdb.set_trace()
        # room_id = self.request.query_params.get('room_id')
        queryset = Chat.objects.filter(room=room_id, id__gt=chat_id)
        serialized_data = ChatSerializer(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


class NewMessageAPIView(generics.GenericAPIView):
    serializer_class = ChatSerializer

    def post(self, request):
        # pdb.set_trace()
        data = {
            'message': request.data['message'],
            'room': request.data['room'],
            'user': request.data['user']
        }
        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
