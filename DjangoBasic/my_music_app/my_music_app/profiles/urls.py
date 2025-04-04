from django.urls import path

from my_music_app.profiles.views import DetailProfileView, DeleteProfileView

urlpatterns = (
    path("details/", DetailProfileView.as_view(), name="details_profile"),
    path("delete/", DeleteProfileView.as_view(), name="delete_profile"),
)
