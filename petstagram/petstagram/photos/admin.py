from django.contrib import admin
from petstagram.photos.models import PetPhoto

@admin.register(PetPhoto)
class PetPhotoADmin(admin.ModelAdmin):
    list_display = ('pk', 'location', 'create_at', 'modified_at')