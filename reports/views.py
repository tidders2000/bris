from django.shortcuts import render
from overtime.models import Overtime
from estab.models import Establishment
import calendar
from django.db.models import Sum
import datetime
from .models import months

def reports(request):
    return render(request,'reports.html')

def overtime_rep(request):
    title='Overtime Report'
    if request.method=="POST":
        start=request.POST.get('start')
        finish=request.POST.get('finish')
        overtime=Overtime.objects.filter(Date__gte=start, Date__lte=finish)
        return render(request,'overtime_rep.html',{'overtime':overtime, 'title':title})
    
    return render(request,'overtime_rep.html',{'title':title})

def estab_rep(request):
    title='Establishment Report'
    monthly=months.objects.all()
    result=[]
    estab=[]
    unu=[]
    x=0
    
    
    if request.method=='POST':
        num = request.POST.get('month')
        year = 2019
        month= int(num)
        days=['Monday','Tuesday','Wednesday','Thursday','Friday']
        dayVals=[1,2,3,4,5]
        
        start = months.objects.filter(month_num=num).values_list('start', flat=True)
        finish = months.objects.filter(month_num=num).values_list('finsh', flat=True)
        for day in dayVals:
           matrix = calendar.monthcalendar(year,month)
           num_days = sum(1 for x in matrix if x[day] != 0)
           result.append(num_days)
           
        for day in days:
            est=Establishment.objects.filter(day=day).aggregate(Sum('hours')).get('hours__sum',0.00)
            unused=establishment=Establishment.objects.filter(day=day).filter(username='unallocated').aggregate(Sum('hours')).get('hours__sum',0.00)
            if not est:
                est=0
            if not unused:
                unused=0
            new=est*int(result[x])
            u=unused*int(result[x])
            estab.append(new)
            unu.append(u)
            x=x+1
        a=sum(estab)
        b=sum(unu)
        c=a+b
        overtime=Overtime.objects.filter(Date__gte=start, Date__lte=finish).aggregate(Sum('hours')).get('hours__sum',0.00)
        total=a-b+overtime
        return render(request,'estab_rep.html',{'result':result,'estab':estab,'unu':unu,'overtime':overtime,'total':total,'c':c})
    
    return render(request,'estab_rep.html',{'monthly':monthly})