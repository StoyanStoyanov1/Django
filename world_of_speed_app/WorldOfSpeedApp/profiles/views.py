from django.shortcuts import render, redirect
from WorldOfSpeedApp.profiles.forms import CreateProfileForm

def profile_details(request):
    return render(request, 'profile/profile-details.html')

def profile_create(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-create.html', context)

def profile_edit(request):
    return render(request, 'profile/profile-edit.html')

def profile_delete(request):
    return render(request, 'profile/profile-delete.html')