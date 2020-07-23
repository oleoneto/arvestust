from django.db import models
from django.db.models import Q


class CommentManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().prefetch_related()

    def get_for_user(self, user):
        return self.get_queryset().filter(
            (
                # TODO: include comments liked by user
                # Q(likes_author__in=user) |
                ~Q(reports__in=[user])
            )
        )
