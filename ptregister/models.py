from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Patient(models.Model):
    ptusername=models.CharField(max_length=20)
    ptpassword=models.CharField(max_length=20)
    ptname=models.CharField(max_length=50)
    ptsurname=models.CharField(max_length=50)
    ptsex=models.CharField(max_length=1)
    ptbirthdate=models.CharField(max_length=12)
    ptidcard=models.CharField(max_length=16)
    ptaddress=models.CharField(max_length=200)
    ptemail=models.CharField(max_length=50)
    ptnum=models.CharField(max_length=10)
    ptphone=models.CharField(max_length=12)

#Create Common User Profile
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    #user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    sex=models.CharField(max_length=1)
    idcard=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    #0=patient 1=doctor 2=nurse 3=officer 4=pharmacist 5=admin
    role=models.IntegerField()

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
