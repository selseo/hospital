from django.db import models
from doctor_timetable.models import Doctor
from ptregister.models import Patient

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

   
class Dee(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
   	    return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey('doctor_timetable.Doctor')
    patient=models.ForeignKey(Patient)
    symptom=models.CharField(max_length=100)
    cause=models.CharField(max_length=100)