from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver

teams = [('nurseing', 'nursing'), ('hca', 'hca'), ('admin', 'admin'), ('admin_CB', 'admin_CB'),
         ('admin_COT', 'admin_COT'), ('Dispensary', 'Dispensary'), ('admin_BIN', 'admin_BIN')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=254, choices=teams)
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    mobile = models.CharField(max_length=40, blank=True)
    next_of_kin_name = models.CharField(max_length=254, default="My Name")
    next_of_kin_phone = models.CharField(max_length=40, blank=True)
    date_of_birth = models.DateField(auto_now=True)
    ni_Number = models.CharField(max_length=40, blank=True)
    profile_image = models.ImageField(
        upload_to='media/profiles')
    Passport_Number = models.CharField(max_length=40, blank=True)
    Driving_lic = models.CharField(max_length=40, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
