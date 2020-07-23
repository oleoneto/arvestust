from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .abstracts import ArvestustRecord


class Follow(ArvestustRecord):
    user = models.ForeignKey(
        get_user_model(),
        related_name='follows',
        on_delete=models.PROTECT,
        verbose_name=_('author')
    )

    class Meta:
        db_table = 'arvestust_follows'
        indexes = [models.Index(fields=['user', 'created_at'])]

    def get_absolute_url(self):
        return reverse('follow-detail', kwargs={'slug': self.slug})
