from django.db import models

class months(models.Model):
    month=models.CharField(max_length=254)
    month_num=models.IntegerField()

# Create your models here.
