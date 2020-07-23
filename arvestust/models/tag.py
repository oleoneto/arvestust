from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .abstracts import ArvestustRecord


class Tag(ArvestustRecord):
    content = models.CharField(max_length=64, verbose_name=_('content'))

    class Meta:
        db_table = 'arvestust_tags'

    def __str__(self):
        return f'{self.content}'

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'slug': self.slug})
