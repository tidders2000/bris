from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from overtime.models import Overtime
from estab.models import Establishment
from leave.models import Leave
from django.db.models import Sum
from absence.models import Absence
from pot.models import Pot
from overtime.forms import status_form
from leave.forms import status_form_leave
from pot.forms import status_form_pot

""" displays dashboard page """
@login_required
def index(request):
    """ works out loggin user and team ids"""
    current_user = request.user.pk
    teaml= request.user.profile.team
    """approval requests"""
    otapprove=Overtime.objects.filter(appmanager=current_user).filter(status='Unactioned')
    alapprove=Leave.objects.filter(appmanager=current_user).filter(status='Unactioned')
    """user personal information """
    myhours=Establishment.objects.filter(user=current_user)
    hours_total=Establishment.objects.filter(user=current_user).aggregate(Sum('hours')).get('hours__sum',0.00)
    
    myleave=Leave.objects.filter(user=current_user)
    myot=Overtime.objects.filter(user=current_user).order_by('Date')
    absence=Absence.objects.filter(absence_end__isnull=True)
    """overtime total for cicle"""
    myottotal=Overtime.objects.filter(user=current_user).exclude(status='Declined').aggregate(Sum('hours')).get('hours__sum',0.00)
    team_leave=Leave.objects.filter(team=teaml).exclude(status='Declined').order_by('date_start')
    pot=request.user.profile.pot
    potapprove=Pot.objects.filter(appmanager=current_user).filter(status='Unactioned')
    """ manages the approval form for leave"""
    
    status=status_form()
    lestat=status_form_leave()
    potform=status_form_pot()
    """manages approval process for leave types"""
    if request.method=="POST":
         if 'otbutt' in request.POST:
        
            ot = status_form(request.POST)
            nv = ot['status'].value()
            ot_pk=request.POST.get('ot_pk')
            t = Overtime.objects.get(id=ot_pk)
            t.status = nv  
            t.save()
         elif 'albutt' in request.POST:
            ot = status_form_leave(request.POST)
            nv = ot['status'].value()
            ot_pk=request.POST.get('al_pk')
            t = Leave.objects.get(id=ot_pk)
            t.status = nv  
            t.save()
            
         elif 'potbutt' in request.POST:
            ot = status_form_pot(request.POST)
            nv = ot['status'].value()
            ot_pk=request.POST.get('po_pk')
            t = Pot.objects.get(id=ot_pk)
            t.status = nv  
            t.save()
         return render(request,'index.html', {'potapprove':potapprove,'potform':potform,'lestat':lestat,'status':status,'myot':myot,'otapprove':otapprove, 'alapprove':alapprove, 'myhours':myhours,'myleave':myleave,'myottotal':myottotal,' team_leave':team_leave})
    else:
     return render(request,'index.html', {'potapprove':potapprove,'potform':potform,'lestat':lestat,'status':status,'absence':absence,'myot':myot,'otapprove':otapprove, 'alapprove':alapprove, 'myhours':myhours,'myleave':myleave,'myottotal':myottotal,'team_leave':team_leave, 'hours_total':hours_total,'pot':pot})

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method=="POST":
        login_form=UserLoginForm(request.POST)
        if login_form.is_valid():
            user=auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
                                    
                                    
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None,'your u or p is wrong')
    else:
        login_form=UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """the users profile page"""
    user = User.objects.get(email=request.user.email)
    return render (request,'profile.html', {'profile':user})