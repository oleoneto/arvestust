from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .managers import LikeManager
from .abstracts import ArvestustRecord


class Like(ArvestustRecord):
    user = models.ForeignKey(
        get_user_model(),
        related_name='likes',
        on_delete=models.CASCADE,
        verbose_name=_('author')
    )

    class Meta:
        db_table = 'arvestust_likes'

    objects = LikeManager()

    def get_absolute_url(self):
        return reverse('like-detail', kwargs={'slug': self.slug})
