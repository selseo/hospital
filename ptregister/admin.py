from django.contrib import admin
from .models import Patient,UserProfile

# Register your models here.
admin.site.register(Patient)
admin.site.register(UserProfile)
