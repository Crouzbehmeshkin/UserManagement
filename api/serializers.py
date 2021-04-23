from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Client, Admin


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Client
        fields = ('user', 'name', 'occupation')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        client, created = Client.objects.update_or_create(user=user,
                                                          name=validated_data['name'],
                                                          occupation=validated_data['occupation'])
        return client


# Register User Serializer
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


# Register Client Serializer
class RegisterClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('user', 'name', 'occupation')

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client
