from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import overtime_form
from .models import Overtime
from datetime import datetime


def overtime(request):
    staffs=User.objects.all()
    datas=''
    form=overtime_form()
    approver=User.objects.filter(groups__name='managers')
    if request.method=="POST":
            ot = overtime_form(request.POST)
            approver=request.POST.get('appID')
            current_user = request.user.pk
            if ot.is_valid():
                 o=ot.save(commit=False)
                 o.user=User(current_user)
                 o.appmanager=approver
                 o.save()
                 return render(request,'ot_request.html',{'staffs':staffs, 'form':form, 'datas':datas})
    else:
      return render(request,'ot_request.html',{'staffs':staffs, 'form':form, 'approver':approver})


