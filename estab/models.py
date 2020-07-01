from django.db import models
from django.contrib.auth.models import User
days = [('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday',
                                                       'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')]
teams = [('nurseing', 'nursing'), ('hca', 'hca'), ('admin', 'admin')]
location = [('bingham', 'bingham'), ('cropwell',
                                     'cropwell'), ('cotgrave', 'cotgrave')]


class Establishment (models.Model):

    shiftname = models.CharField(max_length=254, default='shift')
    team = models.CharField(max_length=254, choices=teams)
    location = models.CharField(
        max_length=254, choices=location, default="bingham")
    shift_start = models.TimeField(auto_now=False)
    shift_end = models.TimeField(auto_now=False)
    day = models.CharField(max_length=254, choices=days)
    hours = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    allocated = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    width = models.CharField(max_length=254, default='20')

    def __str__(self):
        return self.shiftname


class Shifts (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    shift_start = models.TimeField(auto_now=False, null=True)
    shift_end = models.TimeField(auto_now=False, null=True)
    day = models.CharField(max_length=254, choices=days, null=True)
    hours = models.DecimalField(max_digits=3, decimal_places=1, default=0)


def __str__(self):
    return self.user
