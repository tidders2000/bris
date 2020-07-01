from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'team')
    list_filter = ("team",)
    search_fields = ['team', 'user']


admin.site.register(Profile, ProfileAdmin)


# Register your models here.
