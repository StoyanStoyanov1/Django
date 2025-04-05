from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WorldOfSpeedApp.car.validators import validate_year
from WorldOfSpeedApp.profiles.models import Profile


class Car(models.Model):
    TYPE_CHOICES = (
        ("Rally", "Rally"),
        ("Open-wheel", "Open-wheel"),
        ("Kart", "Kart"),
        ("Drag", "Drag"),
        ("Other", "Other"),
    )

    MAX_TYPE_LENGTH = 10

    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=TYPE_CHOICES,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(MIN_MODEL_LENGTH),
        ]
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            validate_year,
        ]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        unique=True,
        error_messages={
            "unique": "This image URL is already in use! Provide a new one.",
        }
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1.0),
        ]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )