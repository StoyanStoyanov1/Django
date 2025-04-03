from django.shortcuts import render
from django import forms
from django.shortcuts import redirect

from my_music_app.profiles.models import Profile
from my_music_app.web.forms import CreateProfileForm

from my_music_app.albums.models import Album


def get_profile():
    return Profile.objects.first()

def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
        
    context = {
        "form": form,
    }

    return render(request, 'web/home-no-profile.html', context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        "albums", Album.objects.all(),

    }
    return render(request, "web/home-with-profile.html")