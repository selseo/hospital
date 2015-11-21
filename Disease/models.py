from django.db import models

# Create your models here.
class Disease(models.Model):
	ICD10=models.CharField(max_length=10,primary_key=True)
	SNOMED=models.CharField(max_length=20,null=True)
	DRG=models.CharField(max_length=20,null=True)
	name=models.CharField(max_length=20,null=True)
	availability=models.BooleanField(default=True)