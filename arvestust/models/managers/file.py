from django.db import models
from django.db.models import Q


class FileManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().prefetch_related()

    def get_for_user(self, user):
        return self.get_queryset().filter(user=user)
