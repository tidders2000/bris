from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import shifts_form, shifts_form2
from .models import Shifts
from django.forms import formset_factory
from django.contrib import messages


x = 0


def monday(request):
    form = shifts_form()
    users = User.objects.all()
    if request.method == 'POST':
        sf = shifts_form(request.POST)
        if sf.is_valid():
            user = sf['user'].value()
            final = sf.save(commit=True)
            final.day = 'Monday'
            final.save()
            request.session['name'] = user

            response = redirect('/estab/tuesday')
            return response

    return render(request, 'Monday.html', {'users': users, 'form': form})


def tuesday(request):
    form = shifts_form2()
    stored_user = User.objects.get(id=request.session['name'])
    if request.method == 'POST':
        sf = shifts_form2(request.POST)
        if sf.is_valid():

            final = sf.save(commit=True)
            final.day = 'Tuesday'
            final.user = stored_user
            final.save()
            response = redirect('/estab/wednesday')
            return response

    return render(request, 'Tuesday.html', {'form': form})


def wednesday(request):
    form = shifts_form2()
    stored_user = User.objects.get(id=request.session['name'])
    if request.method == 'POST':
        sf = shifts_form2(request.POST)
        if sf.is_valid():

            final = sf.save(commit=True)
            final.day = 'Wednesday'
            final.user = stored_user
            final.save()
            response = redirect('/estab/thursday')
            return response

    return render(request, 'Wednesday.html', {'form': form})


def thursday(request):
    form = shifts_form2()
    stored_user = User.objects.get(id=request.session['name'])
    if request.method == 'POST':
        sf = shifts_form2(request.POST)
        if sf.is_valid():

            final = sf.save(commit=True)
            final.day = 'Thursday'
            final.user = stored_user
            final.save()
            response = redirect('/estab/friday')
            return response

    return render(request, 'Thursday.html', {'form': form})


def friday(request):
    form = shifts_form2()
    stored_user = User.objects.get(id=request.session['name'])
    if request.method == 'POST':
        sf = shifts_form2(request.POST)
        if sf.is_valid():

            final = sf.save(commit=True)
            final.day = 'Friday'
            final.user = stored_user
            final.save()
            response = redirect('/')
            return response

    return render(request, 'Friday.html', {'form': form})
