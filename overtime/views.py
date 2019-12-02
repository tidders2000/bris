from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import overtime_form
from .models import Overtime
from datetime import datetime


def overtime(request):
    
    form=overtime_form()
    approver=User.objects.filter(groups__name='managers')
    if request.method == "POST":
        ot = overtime_form(request.POST)
        current_user = request.user.pk
        approver=request.POST.get('appID')
        appmanagerun=request.POST.get('appmanager')    
           
        if ot.is_valid():
            o=ot.save(commit=True)
            o.user=User(current_user)
            o.appmanager=approver
            o.appmanagerun=appmanagerun
            o.save()
            return render(request, 'ot_request.html',{'form':form, 'approver':approver}) 
 
        
             
    return render(request,'ot_request.html',{'form':form,'approver':approver})


