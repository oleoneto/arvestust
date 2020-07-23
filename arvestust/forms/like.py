from django import forms
from ..models.like import Like


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = '__all__'
