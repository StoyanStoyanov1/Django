from django.urls import path

from todos_app_workshop.auth.views import CreateUserApiView

urlpatterns = [
    path("register/", CreateUserApiView.as_view(), name="api_create_user"),
]