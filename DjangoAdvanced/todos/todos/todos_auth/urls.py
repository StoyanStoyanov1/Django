from django.urls import path

from todos.todos_auth.views import CreateUserView, LoginAppView

urlpatterns = [
   path("register/", CreateUserView.as_view(), name="api_create_user"),
   path("login/", LoginAppView.as_view(), name="api_login_user"),
]