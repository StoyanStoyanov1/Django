from django.urls import path
from WorldOfSpeedApp.profiles.views import profile_create, profile_delete, profile_edit, profile_details

urlpatterns = [
    path('create/', profile_create, name='create profile'),
    path('details', profile_details, name='details profile'),
    path('edit/', profile_edit, name='edit profile'),
    path('delete/', profile_delete, name='delete profile'),
]