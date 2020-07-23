from django import forms
from ..models.follow import Follow


class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = '__all__'
