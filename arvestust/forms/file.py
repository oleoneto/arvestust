from django import forms
from ..models.file import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        exclude = ('likes',)
