from django.shortcuts import render
from .forms import emp_form
from .models import EmpDetails
from django.contrib import messages

# Create your views here.


def add_emp(request):

    form = emp_form()
    if request.method == 'POST':

        af = emp_form(request.POST)
        if af.is_valid():
            af.save(commit=True)
            messages.error(request, "Changes saved")

    return render(request, 'addemp.html', {'form': form})
