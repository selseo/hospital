from django.contrib import admin
from appointment.models import Department
from appointment.models import timeTable
from appointment.models import Appointment
from Authentication.models import UserProfile, Patient, Doctor
from Visit.models import PatientVisitInfo, Prescription
from Disease.models import Disease
from Medicine.models import Medicine
# Register your models here.
admin.site.register(Department)

admin.site.register(timeTable)

admin.site.register(Appointment)

admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Doctor)

admin.site.register(PatientVisitInfo)
admin.site.register(Prescription)

admin.site.register(Disease)
admin.site.register(Medicine)

