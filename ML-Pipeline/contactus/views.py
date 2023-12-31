from django.conf import settings
from django.shortcuts import render
from .form import contactform
from django.http import HttpResponseRedirect
from .mail import Mail_send
import os
def con(r):
    form=contactform()
    if r.method=='POST':
        form=contactform(r.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/')
    return render(r,'contactus/contactus.html',{'form':form})


def test(r):
    test = contactform()
    if r.method == 'POST':
        test = contactform(r.POST)
        if test.is_valid():
            test.save()
            print(test.cleaned_data['Email'])
            email=test.cleaned_data['Email']
            image_paths = [
                os.path.join(settings.STATIC_DIR, 'images/Balcony.jpg'),
                os.path.join(settings.STATIC_DIR, 'images/Hall.jpg'),
                os.path.join(settings.STATIC_DIR, 'images/Kitchen.jpg'),
                os.path.join(settings.STATIC_DIR, 'images/Bedroom.jpg')
            ]
            Mail_send(email,image_paths)
            return HttpResponseRedirect('/contact/page/')

    return render(r,'contactus/test.html',{'test':test})

