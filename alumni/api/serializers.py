from rest_framework import serializers
from alumni.models import Alumni
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        return representation


class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = ('id', 'name', 'email', 'phone', 'year_of_passing', 'date_of_birth', 'martial_status',
                  'profession', 'address', 'graduation', 'graduation1', 'created_at', 'last_updated', 'requestor')

    def to_representation(self, instance):
        representation = super(AlumniSerializer, self).to_representation(instance)
        representation['requestor'] = UserSerializer(instance.requestor).data
        return representation
