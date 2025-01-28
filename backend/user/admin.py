import django_stubs_ext
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import AbstractUser

from .models import OTP, Profile, User
from .models import Profile as ProfileType

django_stubs_ext.monkeypatch()


@admin.register(User)
class UserAdmin(BaseUserAdmin[AbstractUser]):
    list_display = ("username", "is_phone", "is_email", "is_superuser")
    filter_horizontal = ()
    list_filter = ("is_phone", "is_email", "is_superuser", "is_private")
    fieldsets = ()
    search_fields = ("username",)


class ProfileAdmin(admin.ModelAdmin[ProfileType]):
    list_display = ("username",)
    list_filter = ("is_private",)


# admin.site.register(User, UserAdmin)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(OTP)
