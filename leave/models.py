from django.db import models
from django.contrib.auth.models import User
# Create your models here.
location=[('bingham','bingham'),('cropwell','cropwell'),('cotgrave','cotgrave')]
teams=[('nurseing','nursing'),('hca','hca'),('admin','admin')]
class Leave(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    team=models.CharField(max_length=254, choices=teams)
    location=models.CharField(max_length=254, choices=location, default="bingham")
    date_start = models.DateField(auto_now=False)
    date_end = models.DateField(auto_now=False)
    approved = models.BooleanField(default=False)
    days= models.CharField(max_length=254)
    appmanager = models.CharField(max_length=254, null=True, default='approver')
    def __str__(self):
        return self.user