from django.conf.urls import url, include
from .views import tracker, nsdetail

urlpatterns = [
    url(r'^tracker/', tracker, name='tracker'),
    url(r'(?P<id>\d+)$', nsdetail, name='nsdetail'),
]
