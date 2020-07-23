# arvestust:admin:inlines
from django.contrib import admin
from ...models import Follow


class FollowInline(admin.StackedInline):
    model = Follow
    extra = 0
