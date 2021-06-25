from student01.home.models import Registration
from django import forms
from .models import *
class studentforms(forms.ModelForm):
    class Meta():
        model=Registration
        fields="__all__"

class profile(forms.ModelForm):
    class Meta():
        model=Registration
        fields=['fullname','img']



