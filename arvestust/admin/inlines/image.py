from django.contrib import admin
from ...models import Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0
