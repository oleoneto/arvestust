from django.db import models
from django.db.models import Q


class ActivityManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().prefetch_related()

    def get_for_user(self, user):
        return self.get_queryset().filter(
            user=user
        )

    def get_matches(self, pk, user, obj_id):
        return self.get_queryset().exclude(id=pk).filter(
            Q(user=user) &
            Q(object_id=obj_id)
        ).distinct()
