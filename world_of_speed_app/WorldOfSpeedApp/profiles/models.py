from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from WorldOfSpeedApp.profiles.validators import validate_username


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 3

    MAX_PASSWORD_LENGTH = 20
    MIN_PASSWORD_LENGTH = 5

    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25

    MIN_AGE = 21

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(
                MIN_USERNAME_LENGTH,
                message="Username must be at least %(limit_value)d chars long!"
            ),
            validate_username,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_AGE),
        ],
        help_text= f"Age requirement: {MIN_AGE} years and above."
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_PASSWORD_LENGTH,
        validators=[
            MinLengthValidator(MIN_PASSWORD_LENGTH),
        ]
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_FIRST_NAME_LENGTH,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LAST_NAME_LENGTH,
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
    )