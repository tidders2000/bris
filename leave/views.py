from django.shortcuts import render
from .forms import leave_form
from django.contrib import messages
from.models import Leave
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

""" return form for users to request leave"""
@login_required
def leave(request):
    form=leave_form()
    approver=User.objects.filter(groups__name='managers')
    if request.method == "POST":
            le = leave_form(request.POST)
            current_user = request.user.pk
            approver=request.POST.get('appID')
            test= leave_form(request.POST)
            teaml= request.user.profile.team
            print(test)
            if le.is_valid():
               l=le.save(commit=False)
               l.user=User(current_user)
               l.team=teaml
               l.appmanager=approver
               l.save()
               messages.error(request, "request submitted")
               return render(request, 'leave.html',{'form':form, 'approver':approver}) 
 
    return render(request, 'leave.html',{'form':form, 'approver':approver}) 