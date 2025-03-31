from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, BaseValidator
from django.core.exceptions import ValidationError
from petstagram.pets.models import Pet

def random_validator(value):
    # if invalid, 'raise ValidationError'
    # Else, if valid, do nothing
    pass

SIZE_5_MB = 5 * 1024 * 1024

class MaxFileSizeValidator(BaseValidator):
    
    def clean(self, x):
        return x.size
    
    def compare(self, file_size, max_size):
        return max_size < file_size


def validate_image_size_less_than_5mb(value):
    if value.size > SIZE_5_MB:
        raise ValidationError('File size shoyld be less than 5MB')
    

class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='get_photos/',
        validators=(
            MaxFileSizeValidator(limit_value=SIZE_5_MB),
        )               
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    location = models.CharField(
        max_length = MAX_LOCATION_LENGTH,
        null=True,
        blank=True
    )

    pets = models.ManyToManyField(Pet)

    create_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )
