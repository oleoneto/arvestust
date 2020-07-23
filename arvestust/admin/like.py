from django.contrib import admin
from ..models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'created_at',
        'updated_at',
        'content_type',
        'object_id',
        'user',
    ]

    # Ensure current user is assigned as author of post instance.
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        obj.save()
