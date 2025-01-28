from django.contrib import admin

from .models import Explorer


class ExplorerAdmin(admin.ModelAdmin):
    list_display = ["post", "all_data"]


admin.site.register(Explorer, ExplorerAdmin)
