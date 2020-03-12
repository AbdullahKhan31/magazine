from django.urls import path, include
from .api import views as api_views
from rest_framework import routers
from django.conf.urls import url
from chat import views

app_name = 'Chat'
router = routers.DefaultRouter()
router.register('room', api_views.RoomView)
router.register('room-user', api_views.RoomUserView)
router.register('chat', api_views.ChatView)

urlpatterns = [
    path('', include(router.urls)),
    path('get-chat/<int:room_id>', api_views.RoomAPIView.as_view(), name='get-chat'),
    path('latest-chat/<int:room_id>/<int:chat_id>', api_views.LatestChatAPIView.as_view(), name='latest-chat'),
    path(r'get-chat/<int:room_id>', api_views.RoomAPIView.as_view(), name='get-chat'),
    path('ChatRooms', views.index, name='index'),
    path(r'LeaveChatRoom/<int:room_id>', views.leave_chat_room, name='LeaveChatRoom'),
    path(r'OpenChatRoom/<int:room_id>', views.open_chat_room, name='OpenChatRoom'),
    path(r'AddRoom', views.add_room, name='AddRoom'),
    path('send-message', api_views.NewMessageAPIView.as_view())
]
