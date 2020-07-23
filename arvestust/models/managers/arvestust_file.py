from django.db import models
from django.db.models import Q


class ArvestustFileManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().prefetch_related()

    def get_for_user(self, user):
        return self.get_queryset().filter(
            Q(is_private=False) |
            Q(uploaded_by=user)
        ).distinct()
