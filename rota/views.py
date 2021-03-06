from django.shortcuts import render, HttpResponseRedirect, redirect
import datetime
import calendar
from datetime import timedelta
from estab.models import Establishment, Shifts
from pot.models import Pot
from leave.models import Leave
from django.contrib.auth.models import User
from overtime.models import Overtime
import dateutil.parser
from django.db.models import Q
from accounts.models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test

value = []
team = []


def is_member(user):
    return user.groups.filter(name='admin').exists()


@login_required
@user_passes_test(is_member, login_url='/rota/rota_view')
def rota(request):
    """ gets days and teams for page and sets two empty var """
    days = Establishment.objects.values('day').distinct()
    teams = Establishment.objects.values('team').distinct()
    selection = ''
    staffs = ''
    if request.method == "GET":
        """ gets the day and team searches model and returns shifts that are unallocated"""
        day = request.GET.get('day')
        team = request.GET.get('team')
        selection = Establishment.objects.filter(
            day=day, allocated=False).filter(team=team)
        staffs = User.objects.values('username')
        return render(request, 'rota.html', {'days': days, 'teams': teams, 'selection': selection, 'staffs': staffs})
    elif request.method == "POST":
        """ takes shift id and username gets user pk and adds to db"""
        username = request.POST.get('username')
        shift = request.POST.get('shiftid')
        user_allocated = request.POST.get('user')
        """UserID=User.objects.get(username=username).pk"""

        """ updates field in establishment to show shift is allocated"""
        t = Establishment.objects.get(id=shift)
        t.allocated = True
        t.user = user_allocated
        t.save()
        return render(request, 'rota.html', {'days': days, 'teams': teams, 'selection': selection})
    else:
        return render(request, 'rota.html', {'days': days, 'teams': teams, 'selection': selection})


""" renders rota view"""


@login_required
def rota_view(request):
    current_user = request.user.pk
    teaml = request.user.profile.team
    selection = []
    data = Shifts.objects.order_by('day')

    for dat in data:
        if dat.user.profile.team == teaml:
            selection.append(dat)
    return render(request, 'rota_view.html', {'selection': selection})
