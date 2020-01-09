from django.db import models

class months(models.Model):
    month=models.CharField(max_length=254)
    month_num=models.IntegerField(default=0)
    start=models.CharField(max_length=254)
    finsh=models.CharField(max_length=254)

# Create your models here.
