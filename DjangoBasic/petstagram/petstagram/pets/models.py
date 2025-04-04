from django.db import models
from django.utils.text import slugify

class Pet(models.Model):
    MAX_NAME_LENGHT = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGHT,
    )

    pet_photo = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.pk))

        super().save(*args, **kwargs)