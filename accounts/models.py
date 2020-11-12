from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

teams = [('nurseing', 'nursing'), ('hca', 'hca'), ('admin', 'admin'), ('admin_CB', 'admin_CB'),
         ('admin_COT', 'admin_COT'), ('Dispensary', 'Dispensary'), ('admin_BIN', 'admin_BIN')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=254, choices=teams)
    leave = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
    pot = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
