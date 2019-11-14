
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm
# Create your views here.


@login_required
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")