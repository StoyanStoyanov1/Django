from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam_prep_my_music_app.accounts.forms import UserCreationForm

UserModel = get_user_model()

class AppUserRegisterView(views.CreateView):
    model = UserModel
    form_class = UserCreationForm
    template_name = 'accounts/register-page'
