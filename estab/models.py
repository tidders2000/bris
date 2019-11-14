

from django.db import models
days =[('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday'),('friday','friday')] 
teams=[('nurseing','nursing'),('hca','hca'),('admin','admin')]
location=[('bingham','bingham'),('cropwell','cropwell'),('cotgrave','cotgrave')]
class Establishment (models.Model):
    

    team=models.CharField(max_length=254, choices=teams)
    location=models.CharField(max_length=254, choices=location, default="bingham")
    shift_start = models.TimeField(auto_now=False)
    shift_end = models.TimeField(auto_now=False)
    day = models.CharField(max_length=254, choices=days)
    hours = models.DecimalField(max_digits=2, decimal_places=0,)
    info = models.TextField()
    
    
    def __str__(self):
        return self.team 
