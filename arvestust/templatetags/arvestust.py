import magic
from django import template
from django.core import serializers
from django.template.defaultfilters import safe
from ..models.validators.file import VALID_FILE_TYPES

register = template.Library()


@register.filter
def json_dump(values):
    # Return values as JSON data
    data = list(values)
    data = serializers.serialize('json', data)
    return safe(data)


@register.filter
def file_mime(file):
    # Get the mime type of a file (E.g. image/jpeg, text/plain)
    mime = magic.from_file(file, mime=True)
    return mime


@register.filter
def file_type(mime):
    # TODO: fix implementation of filter
    try:
        category, t = mime.split('/')

        if category == 'application':
            if t == 'vnd.apple.keynote':
                return 'powerpoint'
            if t in ['vnd.apple.pages', 'msword']:
                return 'word'
            if t in ['vnd.apple.numbers', 'csv']:
                return 'excel'
            if t in ['zip']:
                return 'folder'
            return t

        if category in ['image', 'audio', 'video', 'text']:
            if category == 'text':
                if t in ['plain', 'rtf', 'richtext']:
                    return 'alt'
                else:
                    return 'code'
            return category
    except ValueError:
        return 'code'


@register.filter
def file_size(file, unit):
    """
    Convert the size from bytes to other units like KB, MB or GB

    Adapted from:
    https://thispointer.com/python-get-file-size-in-kb-mb-or-gb-human-readable-format/
    """

    base = 1024

    if unit == 'KB':
        size = file.size/base
    elif unit == 'MB':
        size = file.size/(base**2)
    elif unit == 'GB':
        size = file.size/(base**3)
    else:
        size = file.size

    return f'{round(size, 2)} {unit}'


@register.filter
def total_file_sizes(files, unit):
    total = 0
    base = 1024

    for file in files:
        if unit == 'KB':
            size = file.file.size / base
        elif unit == 'MB':
            size = file.file.size / (base ** 2)
        elif unit == 'GB':
            size = file.file.size / (base ** 3)
        else:
            size = file.file.size
        total += size
    return f'{round(total, 2)} {unit}'


@register.filter
def file_name(file):
    return file.name.split('/')[-1]
