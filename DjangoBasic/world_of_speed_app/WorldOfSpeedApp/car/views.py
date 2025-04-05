from django.shortcuts import render, redirect
from WorldOfSpeedApp.car.forms import CreateCarForm

def catalogue(request):
    return render(request, 'car/catalogue.html')

def car_details(request):
    return render(request, 'car/car_details.html')

def car_create(request):

   
    form = CreateCarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)

def car_edit(request):
    return render(request, 'car/car-edit.html')

def car_delete(request):
    return render(request, 'car/car-delete.html')
