from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from overtime.models import Overtime
from estab.models import Establishment
from leave.models import Leave

@login_required
def index(request):
    current_user = request.user.pk
    otapprove=Overtime.objects.filter(appmanager=current_user,approved=False)
    alapprove=Leave.objects.filter(appmanager=current_user,approved=False)
    myhours=Establishment.objects.filter(user=current_user)
    myleave=Leave.objects.filter(user=current_user)
    myot=Overtime.objects.filter(user=current_user,approved=True)
    if request.method=="POST":
        otapp=request.POST.get('otapp')
        ot_pk=request.POST.get('ot_pk')
        t = Overtime.objects.get(id=ot_pk)
        t.approved = otapp  
        t.save()
        return render(request,'index.html', {'myot':myot,'otapprove':otapprove, 'alapprove':alapprove, 'myhours':myhours,'myleave':myleave})
    else:
     return render(request,'index.html', {'myot':myot,'otapprove':otapprove, 'alapprove':alapprove, 'myhours':myhours,'myleave':myleave})

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