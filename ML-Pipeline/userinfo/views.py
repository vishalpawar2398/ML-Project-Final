from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import userform

def testing(r):
    form=userform()
    if r.method=='POST':
        form=userform(r.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/contact/us')

    return render(r,'base.html',{'form':form})


