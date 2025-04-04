from django.db import models
from petstagram.photos.models import PetPhoto

class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(max_length=MAX_TEXT_LENGTH)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    pet_photo = models.ForeignKey(
            PetPhoto,
            on_delete=models.DO_NOTHING
    )


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING

    )