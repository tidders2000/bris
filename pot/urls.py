from django.conf.urls import url, include
from .views import pot

urlpatterns = [
    url(r'^pot/',pot, name='pot'),
    ]
