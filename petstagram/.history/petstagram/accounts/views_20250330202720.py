from django.shortcuts import render
from django.http import HttpResponse

def signup_user(request):
    context = {}
    return render(request, "accounts/register-page.html", context)

def signin_user(request):
    context = {}
    return render(request, "accounts/login-page.html", context)

def signout_user(request):
    return None

def details_profile(request):
    context = {}
    return render(request, "accounts/profile-details-page.html", context)

def edit_profile(request):
    context = {}
    return render(request, "accounts/profile-edit-page.html", context)

def delete_profile(request):
    context = {}
    return render(request, "accounts/profile-delete-page.html", context)
