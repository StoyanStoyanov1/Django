from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics as api_views, serializers

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):

        class Meta:
            model = UserModel
            fields = ('username' , 'password')

        def create(self, validated_data):
            return UserModel.objects.create_user(**validated_data)

        def to_representation(self, *args, **kwargs):
            representation =  super().to_representation(*args, **kwargs)

            representation.pop('password', None)

            return representation

class CreateUserView(api_views.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = UserModel.objects.all()

class LoginAppView:
    pass

class LogoutAppView:
    pass