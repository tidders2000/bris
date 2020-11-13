from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
location = [('bingham', 'bingham'), ('cropwell',
                                     'cropwell'), ('cotgrave', 'cotgrave')]
teams = [('nurseing', 'nursing'), ('hca', 'hca'), ('admin', 'admin')]


class EmpDetails(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    team = models.CharField(max_length=254, choices=teams)
    location = models.CharField(
        max_length=254, choices=location, default="bingham")
    job_title = models.CharField(max_length=254, default='jobtitle')
    starting_salary = models.IntegerField(default=1000)
    hours = models.DecimalField(max_digits=3, decimal_places=1,)
    dbs_number = models.CharField(max_length=254, default=000000000)
    start_date = models.DateField(auto_now=True)
    new_start = models.BooleanField(default=False)
