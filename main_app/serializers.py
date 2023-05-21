from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['id', 'title', 'description', 'created_at', 'amount', 'decision']


class AppealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appeal
        fields = ['id', 'title', 'description']

    def create(self, validated_data):
        appeal = Appeal.objects.create(**validated_data)
        return appeal


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password']


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password']

