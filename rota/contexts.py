from django.contrib.auth.decorators import user_passes_test  
from django.shortcuts import HttpResponse
@user_passes_test(lambda u: u.groups.filter(name='companyGroup').exists())
def you_view():
    return HttpResponse("Since you're logged in, you can see this text!")