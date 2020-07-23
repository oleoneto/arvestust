# arvestust:admin:inlines
from django.contrib import admin
from ...models import Tag


class TagInline(admin.StackedInline):
    model = Tag
    extra = 0
