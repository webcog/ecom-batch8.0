from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    address_one = models.TextField(blank=True, null=True)
    address_two = models.TextField(blank=True, null=True)
    postal_code = models.IntegerField( blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True) 
    profile_image = models.ImageField(upload_to="profile/", default="profile_default.png", blank=True, null=True)
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')])
    

    def __str__(self):
        return self.user.username
