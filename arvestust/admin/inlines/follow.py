from django.contrib.contenttypes import admin
from ...models import Follow


class FollowInline(admin.GenericStackedInline):
    model = Follow
    extra = 0
