from django.contrib.contenttypes import admin
from ...models import Save


class SaveInline(admin.GenericStackedInline):
    model = Save
    extra = 0
