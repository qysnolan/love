from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):

    list_display = ("title", "menu_id", "type", "description", "photo",
                    "isActive", "last_update")
    search_fields = ("title", "description", "type", "description", "recipe")

admin.site.register(Menu, MenuAdmin)
