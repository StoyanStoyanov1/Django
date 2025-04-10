from django.contrib.auth import get_user_model
from rest_framework import generics as api_views, serializers, permissions
from rest_framework.authtoken import views as api_token_views

UseModel = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseModel
        fields = ('username', 'password')

    def create(self, validated_data):
        return UseModel.objects.create_user(**validated_data)

    def to_representation(self, *args, **kwargs):
        representation = super().to_representation(*args, **kwargs)
        representation.pop('password', None)
        return representation

class CreateUserApiView(api_views.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.AllowAny,)

