from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.conf import settings

from djoser.serializers import UserCreateSerializer, UserSerializer

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    firstName = serializers.CharField(required=True)
    lastName = serializers.CharField(required=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'lastName', 'firstName', 'username', 'password')


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email')


class AccountSerializer(UserSerializer):
    role = serializers.ChoiceField(required=True, choices=settings.ROLES)

    class Meta:
        model = User
        fields = (
            'id', 'lastName', 'firstName', 'username', 'password', 'role')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            lastName=validated_data['lastName'],
            firstName=validated_data['firstName'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class DoctorSerializer(AccountSerializer):

    class Meta(AccountSerializer.Meta):
        fields = ('lastName', 'firstName', 'role')
