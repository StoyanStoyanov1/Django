from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.ListBooks.as_view()),
    path('books/<int:id>/', views.DetailBook.as_view()),
]