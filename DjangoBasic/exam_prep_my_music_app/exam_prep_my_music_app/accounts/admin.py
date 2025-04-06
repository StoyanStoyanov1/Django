from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from exam_prep_my_music_app.accounts.forms import UserChangeForm, UserCreationForm

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form =UserCreationForm
    form = UserChangeForm

    list_display = ('pk','email', "is_staff")
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {"fields": {"email", "password"}}),
        ("Personal info", {"fields": ()}),
        ("Permissions", {"fields": ("is_active", "is_staff", "groups")}),
        ("importnat dates", {"fields": ("last_login")})
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2")
            }
        )
    )