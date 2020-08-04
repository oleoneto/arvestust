from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .abstracts import ArvestustRecord


class Tag(ArvestustRecord):
    content = models.CharField(max_length=64, verbose_name=_('content'))

    class Meta:
        db_table = 'arvestust_tags'
        unique_together = ('object_id', 'content_type', 'content',)

    def clean(self):
        super(Tag, self).clean()
        if Tag.objects.filter(
                content=self.content,
                object_id=self.object_id,
        ).count() > 0:
            raise ValidationError(_('This is a duplicate entry'))

    def __str__(self):
        return f'{self.content}'

    def get_absolute_url(self):
        return reverse('arvestust:tag-detail', kwargs={'slug': self.slug})
