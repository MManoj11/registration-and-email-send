from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.mail import send_mail
from app.forms import *
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()

            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()

            send_mail('Registration',
                      "Successfully Registration is Done",
                      'mannammanoj11@gmail.com',
                      [NSUO.email],
                      fail_silently=False

                      )
            return HttpResponse('Registration is done successfully................')
        else:
            return HttpResponse('Not valid')











    return render(request,'registration.html',d)