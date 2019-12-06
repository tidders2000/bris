from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import overtime_form
from .models import Overtime
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required()
def overtime(request):
    """form for staff to add overtime"""    
    form=overtime_form()
    approver=User.objects.filter(groups__name='managers')
    if request.method == "POST":
        ot = overtime_form(request.POST)
        current_user = request.user.pk
        approver=request.POST.get('appID')
        appmanagerun=request.POST.get('appmanager')  
        """team l gets the team from profile"""
        teaml= request.user.profile.team 
        starttime=request.POST.get('shift_start')
        """code removes 0 and : from time and converts to int to use as margin"""
        slice=starttime.replace("0", "")
        slice2=slice.replace(":","")
        if slice2=='1':
            slice2=10
        width= int(slice2)-8
        
        if ot.is_valid():
            o=ot.save(commit=True)
            o.user=User(current_user)
            o.team=teaml
            o.width=width
            o.appmanager=approver
            o.appmanagerun=appmanagerun
            o.save()
            return render(request, 'ot_request.html',{'form':form, 'approver':approver}) 
 
        
             
    return render(request,'ot_request.html',{'form':form,'approver':approver})


