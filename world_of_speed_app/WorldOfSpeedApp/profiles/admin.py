from django.contrib import admin

from WorldOfSpeedApp.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age', 'email')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
