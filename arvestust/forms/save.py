from django import forms
from ..models.save import Save


class SaveForm(forms.ModelForm):
    class Meta:
        model = Save
        fields = "__all__"
