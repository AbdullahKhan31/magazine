from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from daycare.models import DaycareReservation
from daycare.api.serializers import DaycareReservationSerializer, UserSerializer
from user_management.models import User


class DaycareReservationView(viewsets.ModelViewSet):
    queryset = DaycareReservation.objects.all().order_by('-id')
    serializer_class = DaycareReservationSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer