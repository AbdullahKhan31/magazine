from rest_framework import serializers
from auditorium.models import AuditoriumReservation
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        return representation


class AuditoriumReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriumReservation
        fields = ('id', 'reason', 'start_time', 'end_time', 'created_at', 'last_updated', 'requestor')

    def to_representation(self, instance):
        representation = super(AuditoriumReservationSerializer, self).to_representation(instance)
        representation['requestor'] = UserSerializer(instance.requestor).data
        return representation
