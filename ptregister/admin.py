from django.contrib import admin
from .models import Patients,UserProfile

# Register your models here.
admin.site.register(Patients)
admin.site.register(UserProfile)
