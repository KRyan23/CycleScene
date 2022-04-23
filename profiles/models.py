from django.db import models

''' Required Imports '''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

class UserProfile(models.Model):
    ''' For managing user profile, delivery information and order history '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_mobile_phone = models.CharField(max_length=20, null=True, blank=True)
    default_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode= models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    ''' This creates and or updates the user profile '''
    if created:
        UserProfile.objects.create(user=instance)
        # If the profile exists just save the changes
    instance.userprofile.save()
