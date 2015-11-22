from django.db import models

# Create your models here.
class Disease(models.Model):
	ICD10=models.CharField(max_length=10,primary_key=True)
	SNOMED=models.CharField(max_length=20,null=True)
	DRG=models.CharField(max_length=20,null=True)
	name=models.CharField(max_length=200,null=True)
	availability=models.BooleanField(default=True)
	def __str__(self):
		string1 = ""
		if self.ICD10:
			string1 = string1 + "ICD10 : " + self.ICD10
		if self.name:
			string1 = string1 + " Name : " + self.name
		if self.SNOMED:
			string1 = string1 + " SNOMED : " + self.SNOMED
		if self.DRG:
			string1 = string1 + " DRG : " + self.DRG
		return string1