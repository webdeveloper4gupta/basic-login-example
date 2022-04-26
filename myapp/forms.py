from django import forms
from .models import aman1
class mahajan(forms.ModelForm):
    class Meta:
        model=aman1
        fields="__all__"