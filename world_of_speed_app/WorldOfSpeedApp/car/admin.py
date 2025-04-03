from django.contrib import admin

from WorldOfSpeedApp.car.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'type', 'year', 'price', 'owner')
    search_fields = ('model', 'type', 'year', 'price', 'owner')
    list_filter = ('model', 'type', 'year', 'price', 'owner')
