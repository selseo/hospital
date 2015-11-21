from django import forms
from appointment.models import Appointment
from Medicine.models import Medicine
from Disease.models import Disease
from Visit.models import PatientVisitInfo

# class Nurse(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('', 'email', 'password')