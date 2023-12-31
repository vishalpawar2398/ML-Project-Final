from django.shortcuts import render


import os.path
import pickle

import pandas as pd
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .form import Quotationform

def home(r):
    form=Quotationform()
    return render(r,'base.html',{'form':form})

def result(r):
    form=Quotationform()
    if r.method=='POST':
        form=Quotationform(r.POST)
        if form.is_valid():
            location=form.cleaned_data['location']
            bhk = form.cleaned_data['bhk']
            bath = form.cleaned_data['bath']
            total_sqft = form.cleaned_data['total_sqft']

            models_dir=os.path.join(os.path.dirname(__file__),'models')
            pickle_file=os.path.join(models_dir,'linear_regression.pkl')
            with open(pickle_file,'rb') as model_file:
                model=pickle.load(model_file)

            input_data=pd.DataFrame([[location,bhk,bath,total_sqft]],columns=['location','bhk','bath','total_sqft'])
            predicted_price=round(model.predict(input_data)[0])

            house=form.save(commit=False)
            house.price=predicted_price
            house.save()



            return render(r,'testing.html',{'predicted_price': predicted_price})

    return HttpResponse('PredictionError')

