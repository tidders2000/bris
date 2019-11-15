from django.conf.urls import url, include
from .views import rota

urlpatterns = [
    url(r'^rota/',rota, name='rota'),
   
     
   
]
