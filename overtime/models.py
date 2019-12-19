from django.db import models
from django.contrib.auth.models import User
# Create your models here.
location=[('bingham','bingham'),('cropwell','cropwell'),('cotgrave','cotgrave')]
teams=[('nurseing','nursing'),('hca','hca'),('admin','admin')]
status=[('Unactioned','Unactioned'),('Declined','Declined'),('Approved','Approved')]
class Overtime(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    team=models.CharField(max_length=254, choices=teams)
    location=models.CharField(max_length=254, choices=location, default="bingham")
    Date = models.DateField(auto_now=False,help_text='DD/MM/YY')
    shift_start = models.TimeField(auto_now=False)
    shift_end = models.TimeField(auto_now=False)
    hours = models.DecimalField(max_digits=3, decimal_places=1,) 
    approved = models.BooleanField(default=False)
    status=models.CharField(max_length=254, choices=status, default="Unactioned")
    appmanager = models.CharField(max_length=254, null=True)
    appmanagerun = models.CharField(max_length=254, null=True)
    width = models.CharField(max_length=254, default='20')