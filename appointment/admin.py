from django.contrib import admin
from .models import Department
from .models import timeTable
from .models import Appointment
from Authentication.models import UserProfile, Patient, Doctor
from Disease.models import Disease
from Medicine.models import Medicine
# Register your models here.
admin.site.register(Department)

admin.site.register(timeTable)

admin.site.register(Appointment)

admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Doctor)

admin.site.register(Disease)
admin.site.register(Medicine)