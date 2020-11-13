from django.conf.urls import url, include
from .views import add_emp

urlpatterns = [
    url(r'^add_emp/', add_emp, name='add_emp'),
]
