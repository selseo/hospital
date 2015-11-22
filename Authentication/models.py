from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

#Create Common User Profile
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    #0=patient 1=doctor 2=nurse 3=officer 4=pharmacist 5=admin
    role=models.IntegerField(default=0)
    #0=not available 1=available
    status=models.IntegerField(default=1)
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Patient(models.Model):
    userprofile=models.OneToOneField(UserProfile, default=None)
    sex=models.CharField(max_length=1)
    idcard=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=200)
    birthdate=models.DateField()

    def __unicode__(self):
        return self.userprofile.user.username


