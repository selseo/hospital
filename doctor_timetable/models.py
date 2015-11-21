from django.db import models

# Create your models here.
class Doctor(models.Model):
    drusername=models.CharField(max_length=20,primary_key=True)
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
class timeTable(models.Model):
	dr=models.ForeignKey('Doctor');
	date = models.DateField();
	time1 = models.BooleanField();
	time2 = models.BooleanField();
	patientnum = models.IntegerField(default=0);
	def __str__(self):
		return str(dr.id)+" "+str(dr.drname)+" "+str(date)