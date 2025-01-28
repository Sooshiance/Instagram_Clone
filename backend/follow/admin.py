from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Follower


@admin.register(Follower)
class FollowerAdmin(ModelAdmin[Follower]):
    list_display = ["following", "follower"]
