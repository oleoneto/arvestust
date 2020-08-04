import os
import inflection
import magic
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .record import ArvestustRecord
from ..managers.arvestust_file import ArvestustFileManager
from ..validators.file import validate_file_size, validate_file_type, validate_storage_quota


def file_upload_path(instance, filename):
    name, extension = os.path.splitext(filename)
    file = f'{str(instance.uuid)}{extension}'
    folder = inflection.pluralize(str(instance.content_type))
    return f'{folder}/{instance.content_object.uuid}/{file}'


def check_in_memory_mime(in_memory_file):
    mime = magic.from_buffer(in_memory_file.read(), mime=True)
    return mime


class ArvestustFile(ArvestustRecord):
    name = models.CharField(max_length=50, blank=True)
    file = models.FileField(
        upload_to=file_upload_path,
        verbose_name=_('file'),
        storage=getattr(settings, 'PUBLIC_FILE_STORAGE'),
        validators=[validate_file_size, validate_file_type]
    )
    mime = models.CharField(max_length=100, blank=True, editable=False)
    is_private = models.BooleanField(default=False)

    # TODO: Handle ArvestustRecord deletion
    # Determine the content_type associated with the upload file then opt for the best course of action.
    # The goal is to be compliant with GDPR and other regulations while also ensuring the availability of
    # any materials that are for public consumption on the platform.
    uploaded_by = models.ForeignKey(
        get_user_model(),
        related_name='%(class)s',
        on_delete=models.DO_NOTHING,
        editable=False,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'arvestust_records'
        abstract = True

    objects = ArvestustFileManager()

    def clean(self, *args, **kwargs):
        self.mime = check_in_memory_mime(self.file)
        super(ArvestustFile, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Generate a Medium-like URL slugs:
        self.slug = slugify(f'{self.name}-{str(self.uuid)[-12:]}')

        if self.is_private:
            # self.file.storage = settings.PRIVATE_FILE_STORAGE
            self.file.storage = getattr(settings, 'PRIVATE_FILE_STORAGE')

        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.file.name)
        super().delete()

    def __str__(self):
        return self.name if self.name else f'{self.slug}'

    def get_absolute_url(self):
        return reverse('%(class)-detail', kwargs={'slug': self.slug})
