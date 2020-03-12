from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from auditorium.models import AuditoriumReservation
from auditorium.api.serializers import AuditoriumReservationSerializer, UserSerializer
from user_management.models import User


class AuditoriumReservationView(viewsets.ModelViewSet):
    queryset = AuditoriumReservation.objects.all().order_by('-id')
    serializer_class = AuditoriumReservationSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

