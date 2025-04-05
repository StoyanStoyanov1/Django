from django.urls import path, include

from WorldOfSpeedApp.car.views import catalogue, car_create, car_edit, car_delete, car_details

urlpatterns = [
    path('catalogue/', catalogue, name='catalogue car'),
    path('create/', car_create, name='create car'),
    path('<int:pk>/', include([
        path('details/', car_details, name='details car'),
        path('edit/', car_edit, name='edit car'),
        path('delete/', car_delete, name='delete car'),
    ]))
]