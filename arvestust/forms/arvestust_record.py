from django import forms
from ..models.abstracts import ArvestustRecord


class ArvestustRecordFormMixin(forms.BaseModelForm):
    class Meta:
        exclude = (
            'content_type',
            'object_id',
            'content_object',
        )
