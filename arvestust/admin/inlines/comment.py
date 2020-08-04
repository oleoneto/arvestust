from django.contrib.contenttypes import admin
from ...models import Comment


class CommentInline(admin.GenericTabularInline):
    model = Comment
    extra = 0
    autocomplete_fields = ['user']
