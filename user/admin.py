from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class Admin(UserAdmin):
    filter_horizontal = ()
    list_filter = ('is_active',)
    fieldsets = ()
    ordering = ['email']
    list_display = ('phone', 'is_active')


admin.site.register(User, Admin)
