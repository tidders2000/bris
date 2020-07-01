from django.shortcuts import render, HttpResponse
from django.views.generic import View
from overtime.models import Overtime
from estab.models import Establishment
from absence.models import Absence
import calendar
from django.db.models import Sum
from datetime import datetime
from datetime import date
import calendar
from django.contrib.auth.models import User
from accounts.models import Profile

from .models import months
from .utils import render_to_pdf


def reports(request):
    return render(request, 'reports.html')


""" renders team absence for managers checking history report"""


def teamabs_rep(request):
    teaml = request.user.profile.team
    staffs = Profile.objects.filter(team=teaml)

    if request.method == 'POST':
        id = request.POST.get('username')
        staffab = Absence.objects.filter(user=id)
        return render(request, 'teamabs_rep.html', {'staffs': staffs, 'staffab': staffab})
    else:
        return render(request, 'teamabs_rep.html', {'staffs': staffs})


""" renders absence report"""


def absence_rep(request):
    title = 'Absence Report'
    new = 0
    today = date.today()

    if request.method == "POST":
        start = request.POST.get('start')

        absence = Absence.objects.filter(absence_start__gte=start)
        absenceAll = Absence.objects.filter(absence_end__isnull=True)
        for abse in absenceAll:
            user = abse.user

            today = date.today()
            now = (today - abse.absence_start).days

            new = round(now)

            dw = Establishment.objects.filter(user=user).count()
            shifts_m = round(new/7*dw)
            t = Absence.objects.get(id=abse.id)
            t.days = shifts_m
            t.save()
        return render(request, 'absence_rep.html', {'new': new, 'today': today, 'absence': absence, 'title': title, 'absenceAll': absenceAll})

    return render(request, 'absence_rep.html', {'title': title})


""" renders overtime report"""


def overtime_rep(request):
    title = 'Overtime Report'
    if request.method == "POST":
        start = request.POST.get('start')
        finish = request.POST.get('finish')
        overtime = Overtime.objects.filter(Date__gte=start, Date__lte=finish)
        return render(request, 'overtime_rep.html', {'overtime': overtime, 'title': title})

    return render(request, 'overtime_rep.html', {'title': title})


""" renders establishment report"""


def estab_rep(request):
    title = 'Establishment Report'
    monthly = months.objects.all()
    result = []
    estab = []
    unu = []
    x = 0

    if request.method == 'POST':
        """ get month number and year and works out start end date via calendar"""
        num = request.POST.get('month')
        year = datetime.now().year
        month = int(num)
        dt = calendar.monthrange(year, month)
        star = str(year), "-", str(month), "-01"
        end = str(year), "-", str(month), "-", str(dt[1])
        start = ''.join(star)
        finish = ''.join(end)
        """arrays for working out number of day type in each month"""
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        dayVals = [1, 2, 3, 4, 5]

        """start = months.objects.filter(month_num=num).values_list('start', flat=True)
        finish = months.objects.filter(month_num=num).values_list('finsh', flat=True)"""

        month_name = months.objects.filter(month_num=num)
        """sums number of days in each month by type"""
        for day in dayVals:
            matrix = calendar.monthcalendar(year, month)
            num_days = sum(1 for x in matrix if x[day] != 0)
            result.append(num_days)
        """calculates total number of hours and also empty shifts"""
        for day in days:
            est = Establishment.objects.filter(day=day).aggregate(
                Sum('hours')).get('hours__sum', 0.00)
            unused = establishment = Establishment.objects.filter(day=day).filter(
                username='unallocated').aggregate(Sum('hours')).get('hours__sum', 0.00)
            if not est:
                est = 0
            if not unused:
                unused = 0
            new = est*int(result[x])
            u = unused*int(result[x])
            estab.append(new)
            unu.append(u)
            x = x+1
        a = sum(estab)
        b = sum(unu)
        c = a+b
        """gets overtime worked for period"""

        overtime = Overtime.objects.filter(Date__gte=start, Date__lte=finish).aggregate(
            Sum('hours')).get('hours__sum', 0.00)
        if overtime is None:
            overtime = 0

        total = a-b+overtime
        return render(request, 'estab_rep.html', {'result': result, 'estab': estab, 'unu': unu, 'overtime': overtime, 'total': total, 'c': c, 'month_name': month_name})

    return render(request, 'estab_rep.html', {'monthly': monthly})


"""Aloows report to be printed to pdf"""


def pdf(request):
    overtime = Overtime.objects.filter(
        Date__gte='2019-11-01', Date__lte='2019-11-30')
    data = {
        'today': datetime.date.today(),
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
        'overtime': overtime
    }
    pdf = render_to_pdf('pdf/invoice.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
