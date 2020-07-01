"""bris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from rota import urls as urls_rota
from overtime import urls as urls_overtime
from leave import urls as urls_leave
from reports import urls as urls_reports
from pot import urls as urls_pot
from absence import urls as urls_absence
from accounts import urls as urls_accounts
from estab import urls as urls_estab


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^rota/', include(urls_rota)),
    url(r'^overtime/', include(urls_overtime)),
    url(r'^leave/', include(urls_leave)),
    url(r'^reports/', include(urls_reports)),
    url(r'^pot/', include(urls_pot)),
    url(r'^absence/', include(urls_absence)),
    url(r'^estab/', include(urls_estab)),

]
