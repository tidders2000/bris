from django.db import models
from django.contrib.auth.models import User
from estab.models import Establishment

class Rota (models.Model):
 user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
 estab = models.ForeignKey(Establishment,null=True,on_delete=models.CASCADE)