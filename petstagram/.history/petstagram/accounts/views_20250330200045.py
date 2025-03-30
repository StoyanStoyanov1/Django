from django.shortcuts import render
from django.http import HttpResponse

def signup_user(request):
    context = {}
    return render(request, "accounts/register-page.html", context)

def signin_user(request):
    context = {}

    return render(request, "accounts/signin-user.html", context)

def signout_user(request):
    return None

def details_profile(request):
    context = {}

    return render(request, "accounts/details_profile.html", context)

def edit_profile(request):
    context = {}

    return  render(request, "accounts/edit_profile.html", context)

def delete_profile(request):
    context = {}

    return render(request, "accounts/delete_profile.html", context)
