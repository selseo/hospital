from django.db import models
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

class Doctor(models.Model):
    drusername=models.CharField(max_length=20)
    drpassword=models.CharField(max_length=100)
    drname=models.CharField(max_length=50)
    drsurname=models.CharField(max_length=50)
    drsex=models.CharField(max_length=1)
    drbirthdate=models.CharField(max_length=12)
    dridcard=models.CharField(max_length=13)
    draddress=models.CharField(max_length=200)
    dremail=models.CharField(max_length=50)
    drnum=models.CharField(max_length=10)
    drphone=models.CharField(max_length=12)
    class Meta:
        unique_together = (('drusername'),('dridcard'),('dremail'),)
        def __str__(self): 
            return str(self.id)+" "+str(self.drname)+" "+str(self.drsurname)

class TimetableManager(models.Manager):
    def editTimetable(self, available, d, doctor):
        # Firstly, check whether this time period ever existed in database or not
        av = self.filter(doctor_id=doctor, date=d)
        if av.count() == 0:
            tmp = '';
            if available['period']==0:
                tmp = self.create(doctor_id=doctor,date=d,morning = True if available['status'] == 1 else False, afternoon=False,patientnum=0)    
            else:
                tmp = self.create(doctor_id=doctor,date=d,morning=False, afternoon = True if available['status'] == 1 else False)    
            tmp.save()
        else:
            if available['period']==0:
                av.update(morning = True if available['status'] == 1 else False)
            else :
                av.update(afternoon = True if available['status'] == 1 else False)
        # # If yes, just update it
        # if av.count() > 0:
            

        # # If no, create new one
        # else:
            


class timeTable(models.Model):
    doctor_id=models.ForeignKey('Doctor')
    date = models.DateField()
    morning = models.BooleanField()
    afternoon = models.BooleanField()
    patientnum = models.IntegerField(default=0) # should this line be included?

    objects = TimetableManager()

    def __str__(self):
      return ''


class Appointment(models.Model):
    patient_id=models.ForeignKey(Patient)
    timetable_id=models.ForeignKey(timeTable)
    symptom=models.CharField(max_length=100)
    cause=models.CharField(max_length=100)
