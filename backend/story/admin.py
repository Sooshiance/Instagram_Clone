from typing import TYPE_CHECKING

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Story

if TYPE_CHECKING:
    from .models import Story as StoryType


@admin.register(Story)
class StoryAdmin(ModelAdmin):
    list_display = ['user']
