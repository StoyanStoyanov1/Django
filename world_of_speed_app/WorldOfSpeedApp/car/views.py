from django.shortcuts import render

def catalogue(request):
    return render(request, 'car/catalogue.html')

def car_details(request):
    return render(request, 'car/car_details.html')

def car_create(request):
    return render(request, 'car/car-create.html')

def car_edit(request):
    return render(request, 'car/car-edit.html')

def car_delete(request):
    return render(request, 'car/car-delete.html')
