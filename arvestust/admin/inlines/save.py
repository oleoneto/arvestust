from django.contrib import admin
from ...models import Save


class SaveInline(admin.StackedInline):
    model = Save
    extra = 0
