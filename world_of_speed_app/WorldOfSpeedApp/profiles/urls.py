from django.urls import path
from WorldOfSpeedApp.profiles.views import profile_create, profile_delete, profile_edit, profile_details

urlpatterns = [
    path('create/', profile_create, name='create'),
    path('details', profile_details, name='details'),
    path('edit/', profile_edit, name='edit'),
    path('delete/', profile_delete, name='delete'),
]