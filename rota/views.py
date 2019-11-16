from django.shortcuts import render
from .models import Rota
from.forms import rota_form
from estab.models import Establishment
from django.contrib.auth.models import User

def rota(request):
    """ gets days and teams for page and sets two empty var """
    days=Establishment.objects.values('day').distinct()
    teams=Establishment.objects.values('team').distinct()
    selection=''
    staffs=''
    if request.method=="GET":
        """ gets the day and team searches model and returns shifts that are unallocated"""
        day=request.GET.get('day')
        team=request.GET.get('team')
        selection=Establishment.objects.filter(day=day,username='unallocated').filter(team=team)
        staffs=User.objects.values('username')
        return render(request,'rota.html',{'days':days,'teams':teams, 'selection':selection,'staffs':staffs})
    elif request.method=="POST": 
        """ takes shift id and username gets user pk and adds to db"""
        username=request.POST.get('username')
        shift=request.POST.get('shiftid')
        UserID=User.objects.get(username=username).pk
        
        p = Rota(user=User(UserID), estab=Establishment(shift))
        p.save()
        """ updates field in establishment to show shift is allocated"""
        t = Establishment.objects.get(id=shift)
        t.username = username
        t.save()
        return render(request,'rota.html',{'days':days,'teams':teams, 'selection':selection})
    else:
     return render(request,'rota.html',{'days':days,'teams':teams, 'selection':selection})

def rota_view(request):
    """ gets days and teams for page and sets two empty var """
    days=Establishment.objects.values('day').distinct()
    teams=Establishment.objects.values('team').distinct()
    value=[]
    if request.method=="GET":
        day=request.GET.get('day')
        team=request.GET.get('team')
        rotas = Rota.objects.all()
        for rota in rotas:
            value.append(rota.estab.day)
        return render(request,'rota_view.html',{'rotas':rotas,'day':day,'team':team,'value':value})
    else:
        return render(request,'rota_view.html',{'rotas':rotas,'days':days,'teams':teams,'value':value})