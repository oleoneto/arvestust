from django import forms
from ..models.comment import Comment
from .arvestust_record import ArvestustRecordFormMixin


class CommentForm(ArvestustRecordFormMixin, forms.ModelForm):
    class Meta(ArvestustRecordFormMixin.Meta):
        model = Comment
        exclude = ArvestustRecordFormMixin.Meta.exclude + ('reports', 'likes', 'user')
