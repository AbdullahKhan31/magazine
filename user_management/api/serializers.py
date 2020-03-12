from rest_framework import serializers
from user_management.models import User, Role, UserRole
import rest_auth.serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'title', 'description', 'created_at','last_updated', 'status')


class UserRoleSerializer(serializers.ModelSerializer):
    # role = serializers.StringRelatedField()
    # userdetail = serializers.StringRelatedField()
    class Meta:
        model = UserRole
        fields = ('id', 'user', 'role', 'approver', 'created_at', 'last_updated', 'status')

    def to_representation(self, instance):
        representation = super(UserRoleSerializer, self).to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['role'] = RoleSerializer(instance.role).data
        representation['approver'] = UserSerializer(instance.approver).data
        return representation


# LOGIN SERIALIZER
class LoginSerializer(rest_auth.serializers.LoginSerializer):
    def get_fields(self):
        fields = super(LoginSerializer, self).get_fields()
        fields['email'] = fields['username']
        del fields['username']
        return fields

    def validate(self, attrs):
        attrs['username'] = attrs['email']
        del attrs['email']
        return super(LoginSerializer, self).validate(attrs)