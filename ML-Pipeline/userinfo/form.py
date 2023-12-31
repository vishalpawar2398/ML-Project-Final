from django import forms
from .models import usermodel

class userform(forms.ModelForm):

    class Meta:
        model=usermodel
        fields=("__all__")
        widgets = {
            'balcony':forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),
            'playground': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')])
        }

