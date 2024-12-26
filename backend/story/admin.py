from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Story
from .models import Story as StoryType


@admin.register(Story)
class StoryAdmin(ModelAdmin[StoryType]):
    list_display = ['user']
