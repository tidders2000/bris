from django.conf.urls import url, include
from .views import absence,absence_edit

urlpatterns = [
    url(r'^absence/',absence, name='absence'),
    url(r'^edit/(?P<id>\d+)/',absence_edit, name='absence_edit')
    ]

