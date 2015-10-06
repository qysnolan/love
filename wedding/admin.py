from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):

    list_display = ("person_name", "comment_id", "comment", "isActive",
                    "last_update",)
    search_fields = ("persont_name", "comment",)

admin.site.register(Comment, CommentAdmin)
