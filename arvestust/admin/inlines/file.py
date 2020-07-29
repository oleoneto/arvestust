from django.contrib.contenttypes import admin
from ...models import File


class FileInline(admin.GenericTabularInline):
    model = File
    extra = 0
