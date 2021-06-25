from django import forms
from home.models import Registration

class studentforms(forms.ModelForm):
    class Meta():
        model=Registration
        fields="__all__"