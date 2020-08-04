import os
import uuid
import inflection
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .abstracts import ArvestustRecord, ArvestustFile
from .validators.file import validate_file_size, validate_storage_quota


def file_upload_path(instance, filename):
    name, extension = os.path.splitext(filename)
    file = f'{str(instance.uuid)}{extension}'
    folder = inflection.pluralize(str(instance.content_type))
    return f'{folder}/{instance.content_object.uuid}/{file}'


class Image(ArvestustFile):
    file = models.ImageField(
        upload_to=file_upload_path,
        verbose_name=_('file'),
        storage=getattr(settings, 'PUBLIC_FILE_STORAGE'),
        validators=[validate_file_size]
    )

    class Meta:
        db_table = 'arvestust_images'
        indexes = [models.Index(fields=['created_at'])]
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})
