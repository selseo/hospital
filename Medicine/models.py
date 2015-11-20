from django.db import models

# Create your models here.

class Medicine(models.Model)
	name = models.CharField(max_length=300,primary_key=True)
	availability = models.BooleanField(default=True)

