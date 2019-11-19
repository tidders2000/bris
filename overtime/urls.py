from django.conf.urls import url, include
from .views import overtime

urlpatterns = [
    url(r'^overtime/',overtime, name='overtime'),
    ]
