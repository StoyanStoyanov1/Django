from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from my_music_app.profiles.models import Profile


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIS_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    GENRE_POP_MUSIC = "Pop Music"
    GENRE_JAZZ_MUSIC = "Jazz Music"
    GENRE_ROCK_MUSIC = "Rock Music"
    GENRE_COUNTRY_MUSIC = "Country Music"
    GENRE_RNB_MUSIC = "R&B Music"
    GENRE_DANCE_MUSIC = "Dance Music"
    GENRE_HIP_HOP_MUSIC = "Hip Hop Music"
    GENRE_OTHER = "Other"

    GENRES = (
        (GENRE_POP_MUSIC, GENRE_POP_MUSIC),
        (GENRE_JAZZ_MUSIC, GENRE_JAZZ_MUSIC),
        (GENRE_ROCK_MUSIC, GENRE_ROCK_MUSIC),
        (GENRE_COUNTRY_MUSIC, GENRE_COUNTRY_MUSIC),
        (GENRE_RNB_MUSIC, GENRE_RNB_MUSIC),
        (GENRE_DANCE_MUSIC, GENRE_DANCE_MUSIC),
        (GENRE_HIP_HOP_MUSIC, GENRE_HIP_HOP_MUSIC),
        (GENRE_OTHER, GENRE_OTHER),
    )

    MIN_PRICE = 0.0

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIS_NAME_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GENRES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(MIN_PRICE)]
    )

    owner = models.ForeignKey(
        Profile, 
        on_delete=models.DO_NOTHING,
    )

