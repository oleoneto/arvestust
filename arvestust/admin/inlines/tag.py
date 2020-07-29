from django.contrib.contenttypes import admin
from ...models import Tag


class TagInline(admin.GenericStackedInline):
    model = Tag
    extra = 0
