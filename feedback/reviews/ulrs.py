from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.review),
    include("", include("reviews.urls"))
]