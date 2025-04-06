from django.db import models
from django.contrib.auth import models as auth_models, get_user_model

from exam_prep_my_music_app.accounts.managers import AppUserManager

class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()
    def __str__(self):
        return self.email