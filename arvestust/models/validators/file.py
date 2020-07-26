# arvestust:models:validators
import magic
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

__MAX_UPLOAD_SIZE__ = 10 << 20  # 10 Megabytes

__DEFAULT_ORGANIZATION_QUOTA__ = 10 << 30  # 10 Gigabytes

__DEFAULT_USER_QUOTA__ = 100 << 20  # 100 Megabytes

VALID_AUDIO_TYPES = [
    'audio/3gpp',
    'audio/3gpp2',
    'audio/aac',
    'audio/midi',
    'audio/mpeg',
    'audio/ogg',
    'audio/opus',
    'audio/wav',
    'audio/webm',
    'audio/x-midi',
]

VALID_IMAGE_TYPES = [
    'image/bmp',
    'image/gif',
    'image/ief',
    'image/jp2',
    'image/jpeg',
    'image/png',
    'image/svg+xml',
    'image/vnd.microsoft.icon',
    'image/vnd.wap.wbmp',
    'image/tiff',
    'image/x-icon',
]

VALID_VIDEO_TYPES = [
    'video/3gpp',
    'video/3gpp2',
    'video/mp4',
    'video/mpeg',
    'video/ogg',
    'video/webm',
    'video/x-msvideo',
]

VALID_TEXT_TYPES = [
    'text/calendar',
    'text/css',
    'text/csv',
    'text/html',
    'text/javascript',
    'text/plain',
    'text/richtext',
    'text/rtf'
]

VALID_APPLICATION_TYPES = [
    'application/epub+zip',
    'application/json',
    'application/msword',
    'application/pdf',
    'application/php',
    'application/vnd.apple.keynote',
    'application/vnd.apple.pages',
    'application/vnd.apple.numbers',
    'application/vnd.ms-excel',
    'application/vnd.ms-powerpoint',
    'application/vnd.oasis.opendocument.presentation',
    'application/vnd.oasis.opendocument.spreadsheet',
    'application/vnd.oasis.opendocument.text',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/x-tar',
    'application/xhtml+xml',
    'application/xml',
    'application/xml-dtd',
    'application/xslt+xml',
    'application/zip'
]

VALID_FILE_TYPES = {
    'audio': VALID_AUDIO_TYPES,
    'image': VALID_IMAGE_TYPES,
    'video': VALID_VIDEO_TYPES,
    'text': VALID_TEXT_TYPES,
    'application': VALID_APPLICATION_TYPES
}


def validate_file_type(file):
    v = sorted(v for value in VALID_FILE_TYPES.values() for v in value)
    mime = magic.from_buffer(file.read(), mime=True)
    if mime in v:
        return mime
    raise ValidationError(_('This file type is not supported'))


def validate_file_size(file):
    if file.size > __MAX_UPLOAD_SIZE__:
        raise ValidationError(_(f'Maximum file size is {__MAX_UPLOAD_SIZE__}'))
    return file


def validate_storage_quota(file):
    # TODO: before uploading, determine if user or organization has if within upload limits
    pass
