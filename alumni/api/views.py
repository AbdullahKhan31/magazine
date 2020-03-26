from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from alumni.models import Alumni
from alumni.api.serializers import AlumniSerializer, UserSerializer
from user_management.models import User


class AlumniRegisterView(viewsets.ModelViewSet):
    queryset = Alumni.objects.all().order_by('-id')
    serializer_class = AlumniSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
