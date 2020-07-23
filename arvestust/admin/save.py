from django.contrib import admin
from ..models import Save


@admin.register(Save)
class SaveAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'user',
        'created_at',
        'updated_at',
    ]
