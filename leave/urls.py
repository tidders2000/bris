from django.conf.urls import url, include
from .views import leave

urlpatterns = [
    url(r'^leave/',leave, name='leave'),
    ]
