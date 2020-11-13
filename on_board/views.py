from django.shortcuts import render, get_object_or_404
from employee_details.models import EmpDetails
from employee_details.forms import emp_form
# Create your views here.


def tracker(request):

    newstarts = EmpDetails.objects.all().filter(new_start=True)

    return render(request, 'tracker.html', {'newstarts': newstarts})


def nsdetail(request, id):
    instance = get_object_or_404(EmpDetails, id=id)
    employee = emp_form(instance=instance)

    return render(request, 'nsdetail.html', {'employee': employee})
