from django.contrib import admin
from .models import Establishment, Shifts


class Estab(admin.ModelAdmin):
    list_display = ('user', 'day', 'team', 'location')
    list_filter = ("user", 'day')
    list_order = ('day')
    search_fields = ['user', 'day']


admin.site.register(Establishment, Estab)

admin.site.register(Shifts)
