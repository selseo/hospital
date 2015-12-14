from django.db import models

from appointment.models import Appointment
from Medicine.models import Medicine
from Disease.models import Disease

from django.core.exceptions import ValidationError

# Create your models here.

class PatientVisitInfo(models.Model):
	appointment=models.OneToOneField(Appointment, primary_key=True)
	weight=models.DecimalField(max_digits=4, decimal_places=1, null=True)
	height=models.DecimalField(max_digits=4, decimal_places=1, null=True)
	bodyTemp=models.DecimalField(max_digits=4, decimal_places=1, null=True)
	pulse=models.IntegerField(null=True)
	systolic=models.IntegerField(null=True)
	diastolic=models.IntegerField(null=True)
	status=models.IntegerField()
	lastUpdate=models.DateTimeField(auto_now=True)
	note=models.CharField(max_length=200, null=True)
	medicines=models.ManyToManyField(Medicine,through='Prescription')
	diseases=models.ManyToManyField(Disease)

class Prescription(models.Model):
	class Meta():
		auto_created=True
	patientVisitInfo=models.ForeignKey(PatientVisitInfo)
	medicines=models.ForeignKey(Medicine)
	amount=models.IntegerField(default = 1)
	usage=models.CharField(max_length=200,null=True)

# Validators.

def weightTooMuch(value):
	if(value >= 500):
		raise ValidationError('%s is not less than 500' % value)
