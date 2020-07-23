import uuid
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .managers import SaveManager
from .abstracts import ArvestustRecord


class Save(ArvestustRecord):
    user = models.ForeignKey(
        get_user_model(),
        related_name='saves',
        on_delete=models.CASCADE,
        verbose_name=_('author')
    )
    notes = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('notes'))
    permalink = models.URLField(blank=True, null=True, verbose_name=_('permalink'))

    class Meta:
        db_table = 'arvestust_saves'

    objects = SaveManager()

    def get_absolute_url(self):
        return reverse('save-detail', kwargs={'slug': self.slug})
