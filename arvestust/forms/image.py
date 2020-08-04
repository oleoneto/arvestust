from django import forms
from ..models.image import Image
from .arvestust_record import ArvestustRecordFormMixin


class ImageForm(ArvestustRecordFormMixin, forms.ModelForm):
    class Meta:
        model = Image
        exclude = ArvestustRecordFormMixin.Meta.exclude + ('uploaded_by',)
