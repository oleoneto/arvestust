from django import forms
from ..models.tag import Tag
from .arvestust_record import ArvestustRecordFormMixin


class TagForm(ArvestustRecordFormMixin, forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ArvestustRecordFormMixin.Meta.exclude + ('user',)
