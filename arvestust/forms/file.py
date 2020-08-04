from django import forms
from ..models.file import File
from .arvestust_record import ArvestustRecordFormMixin


class FileForm(ArvestustRecordFormMixin, forms.ModelForm):
    class Meta:
        model = File
        exclude = ArvestustRecordFormMixin.Meta.exclude + ('likes', 'uploaded_by')
