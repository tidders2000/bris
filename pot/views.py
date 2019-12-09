from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from .forms import pot_form
from .models import Pot
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required()
def pot(request):
    """form for staff to add overtime"""    
    form=pot_form()
    approver=User.objects.filter(groups__name='managers')
    if request.method == "POST":
        pt = pot_form(request.POST)
        current_user = request.user.pk
        approver=request.POST.get('appID')
        appmanagerun=request.POST.get('appmanager')  
        """team l gets the team from profile"""
        teaml= request.user.profile.team 
        pot_hours=request.user.profile.pot
        starttime=request.POST.get('pot_start')
        """code removes 0 and : from time and converts to int to use as margin"""
        slice=starttime.replace("0", "")
        slice2=slice.replace(":","")
        if slice2=='1':
            slice2=10
        width= int(slice2)-8
        hours=request.POST.get('hours')
        hour_int=int(hours)
        if  request.POST.get('worked')=='pluspot':
            new_hours= pot_hours+hour_int
        
        else:
            neg='-'+hours
            new_hours= pot_hours+int(neg)
            
        
        
        Profile.objects.filter(user=current_user).update(pot=new_hours)
        
        
        
        if pt.is_valid():
            o=pt.save(commit=True)
            o.user=User(current_user)
            o.team=teaml
            o.width=width
            o.appmanager=approver
            o.appmanagerun=appmanagerun
            o.save()
            return render(request, 'pot.html',{'form':form, 'approver':approver}) 
 
        
             
    return render(request,'pot.html',{'form':form,'approver':approver})


