from django.conf.urls import url, include
from .views import monday, tuesday, wednesday, thursday, friday

urlpatterns = [
    url(r'^monday/', monday, name='monday'),
    url(r'^tuesday/', tuesday, name='tuesday'),
    url(r'^wednesday/', wednesday, name='wednesday'),
    url(r'^thursday/', thursday, name='thursday'),
    url(r'^friday/', friday, name='friday'),



]
