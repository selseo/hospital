from django.contrib import admin
from .models import PatientVisitInfo, Prescription

# Register your models here.
admin.site.register(PatientVisitInfo)
admin.site.register(Prescription)