from django.db import models
from django.contrib.auth.models import User
# Create your models here.
location=[('bingham','bingham'),('cropwell','cropwell'),('cotgrave','cotgrave')]
teams=[('nurseing','nursing'),('hca','hca'),('admin','admin')]
status=[('Unactioned','Unactioned'),('Declined','Declined'),('Approved','Approved')]

class Leave(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    team=models.CharField(max_length=254, choices=teams)
    location=models.CharField(max_length=254, choices=location, default="bingham")
    date_start = models.DateField(auto_now=False)
    date_end = models.DateField(auto_now=False)
    approved = models.BooleanField(default=False)
    hours = models.FloatField()
    days= models.CharField(max_length=254)
    status=models.CharField(max_length=254, choices=status, default="Unactioned")
    appmanager = models.CharField(max_length=254, null=True, default='approver')
   