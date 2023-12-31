from django import forms
from .models import Userinputmodel
import pandas as pd
import os
models_dir=os.path.join(os.path.dirname(__file__),'models')
csv_file=os.path.join(models_dir,'Bengaluru_House_Dataaws.csv')

df=pd.read_csv(csv_file)
area_list,availiablity_list,location_list,society_list=(
    list(df['area_type'].unique()),
    list(df['availability'].unique()),
    list(df['location'].unique()),
    list(df['society'].unique()))



BLANK_CHOICE = [('', '')]
AREA_CHOICES =BLANK_CHOICE+ [(area_list[i], data) for i, data in enumerate(area_list)]
AVAIL_CHOICES = BLANK_CHOICE+[(availiablity_list[i], data) for i, data in enumerate(availiablity_list)]
LOCATION_CHOICES = BLANK_CHOICE+[(location_list[i], data) for i, data in enumerate(location_list)]
SOCIETY_CHOICES = BLANK_CHOICE+[(society_list[i], data) for i, data in enumerate(society_list)]

class Quotationform(forms.ModelForm):
    area_type=forms.ChoiceField(choices=AREA_CHOICES)
    availability=forms.ChoiceField(choices=AVAIL_CHOICES)
    location = forms.ChoiceField(choices=LOCATION_CHOICES)
    society=forms.ChoiceField(choices=SOCIETY_CHOICES)
    class Meta:
        model=Userinputmodel
        fields = ['area_type','availability','location','bhk','society','total_sqft','bath','balcony']
