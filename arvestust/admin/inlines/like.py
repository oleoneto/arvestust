from django.contrib.contenttypes import admin
from ...models import Like


class LikeInline(admin.GenericTabularInline):
    model = Like
    extra = 0
