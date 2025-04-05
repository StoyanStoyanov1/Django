from django.contrib.auth import get_user_model, models as auth_models
from django.db import models

# UserModel = get_user_model()

class AccountUser(auth_models.AbstractUser):
    age = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )

# class AccountsUserProxy(UserModel):
#
#     class Meta:
#         proxy = True
#         ordering = ("username",)