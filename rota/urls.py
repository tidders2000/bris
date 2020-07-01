from django.conf.urls import url, include
from .views import rota, rota_view
# increase

urlpatterns = [
    url(r'^rota/', rota, name='rota'),
    url(r'^rota_view/', rota_view, name='rota_view'),
    # url(r'^increase/',increase, name='increase')


]
