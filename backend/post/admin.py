from django.contrib import admin

from .models import (
    Post,
    Comment,
    Album,
)


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user']
    inlines = [AlbumInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user']
