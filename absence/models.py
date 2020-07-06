from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reason(models.Model):
    reason = models.CharField(max_length=254)

    def __str__(self):
        return self.reason


class Absence(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=254, null=True, default='approver')
    absence_start = models.DateField(
        auto_now=False, null=True)
    absence_end = models.DateField(auto_now=False, null=True, blank=True)
    gp_consult = models.BooleanField(default=False)
    further_support = models.TextField(null=True, blank=True)
    days = models.CharField(max_length=254, default=0)
    reason = models.ForeignKey(Reason, on_delete=models.SET_NULL, null=True)
