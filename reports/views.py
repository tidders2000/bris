from django.shortcuts import render
from overtime.models import Overtime
from estab.models import Establishment
import calendar
from django.db.models import Sum

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
     
    year = 2019
    month = 11
    day_to_count = calendar.MONDAY
    matrix = calendar.monthcalendar(year,month)
    num_days = sum(1 for x in matrix if x[day_to_count] != 0)
    hour=Establishment.objects.filter(day='Monday').aggregate(Sum('hours')).get('hours__sum',0.0)
    hours_ua=Establishment.objects.filter(day='Monday').filter(username='unallocated').aggregate(Sum('hours')).get('hours__sum',0.0)
    ot_hours=Overtime.objects.filter(Date__gte='2019-11-01', Date__lte='2019-11-30').aggregate(Sum('hours')).get('hours__sum',0.0)
    hours=hour
    hours_ua=hour-hours_ua
    mondays=num_days*hours
    
    
    return render(request,'estab_rep.html',{'title':title,'num_days':num_days,'hours':hours,'mondays':mondays,'hours_ua':hours_ua,'ot_hours':ot_hours})