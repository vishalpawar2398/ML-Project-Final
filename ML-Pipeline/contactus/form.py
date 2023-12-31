from django import forms
from .models import contacmodel

class contactform(forms.ModelForm):
    class Meta:
        model=contacmodel
        fields=("__all__")