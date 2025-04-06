from django.urls import path

from todos.todos_auth.views import CreateUserView

urlpatterns = [
   path("create/", CreateUserView.as_view(), name="api_create_user"),
]