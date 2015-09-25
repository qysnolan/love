from django.contrib import admin

from .models import Photo


class PhotoAdmin(admin.ModelAdmin):

    list_display = ("title", "photo_id", "description", "path", "last_update")
    search_fields = ("title", "description", )

admin.site.register(Photo, PhotoAdmin)