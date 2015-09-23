from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

   