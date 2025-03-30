from django.urls import path
from petstagram.accounts.views import signup_user, signin_user, details_profile, delete_profile, edit_profile

urlpatterns = (
    path("signup/", signup_user, name="signup_user"),
    path("signin/", signin_user, name="signin_user"),
    path("profile/<int:pk>", details_profile, name="details profile"),
    path("profile/<int:pk>/edit", edit_profile, name="edit profile"),
    path("profile/<int:pk>/pk>/delete", delete_profile, name="delete profile"),
)
