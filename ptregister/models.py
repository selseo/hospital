from django.db import models

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
