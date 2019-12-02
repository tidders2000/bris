from django.conf.urls import url, include
from .views import reports, overtime_rep, estab_rep

urlpatterns = [
    url(r'^reports/',reports, name='reports'),
     url(r'^overtime_rep/',overtime_rep, name='overtime_rep'),
      url(r'^estab_rep/',estab_rep, name='estab_rep'),
    
   
]
