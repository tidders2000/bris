from django.conf.urls import url, include
from .views import reports, overtime_rep, estab_rep,pdf

urlpatterns = [
    url(r'^reports/',reports, name='reports'),
     url(r'^overtime_rep/',overtime_rep, name='overtime_rep'),
      url(r'^estab_rep/',estab_rep, name='estab_rep'),
       url(r'^pdf/',pdf, name='pdf'),
   
]
