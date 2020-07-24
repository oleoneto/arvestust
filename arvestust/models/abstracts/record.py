import uuid
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class ArvestustRecord(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        related_name='%(class)s',
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Default fields. Used for record-keeping.
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(_('slug'), max_length=250, unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True, editable=False)

    class Meta:
        db_table = 'arvestust_records'
        indexes = [models.Index(fields=['created_at'])]
        ordering = ['-created_at']
        abstract = True

    def save(self, *args, **kwargs):
        # Generate a Medium-like URL slugs:
        self.slug = slugify(f'{str(self.uuid)}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.slug}'

    def get_absolute_url(self):
        return reverse('%(class)-detail', kwargs={'slug': self.slug})
