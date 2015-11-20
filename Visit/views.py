from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from ptregister.models import Patient
from appointment.models import Appointment

import random

# Create your views here.

def index(request):
    return HttpResponse("All Indexes.")

def seed(request):
	pt = Patient(ptusername=random.randrange(1,100),
    ptpassword=make_password(password=random.randrange(0,100000).'',hasher='sha1'),
    ptname='name'+random.randrange(1,100),
    ptsurname='sur'+random.randrange(1,100),
    ptsex=random.choice(['M','F']),
    ptbirthdate=random.randrange(1,100000),
    ptidcard=random.randrange(1,100),
    ptaddress=random.randrange(1,100),
    ptemail=random.randrange(1,100),
    ptnum=random.randrange(1,100),
    ptphone=random.randrange(1,100),)
	pt.save()
	return render(request, 'roles.seed')
