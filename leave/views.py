from django.shortcuts import render
from .forms import leave_form
from.models import Leave
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def leave(request):
    form=leave_form()
    approver=User.objects.filter(groups__name='managers')
    if request.method == "POST":
            le = leave_form(request.POST)
            current_user = request.user.pk
            approver=request.POST.get('appID')
            test= leave_form(request.POST)
            print(test)
            if le.is_valid():
               l=le.save(commit=False)
               l.user=User(current_user)
               l.appmanager=approver
               l.save()
               return render(request, 'leave.html',{'form':form, 'approver':approver}) 
 
    return render(request, 'leave.html',{'form':form, 'approver':approver}) 