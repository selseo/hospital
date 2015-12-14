from django import forms
from Visit.models import PatientVisitInfo

class PatientVisitPharmacistForms(forms.ModelForm):
    class Meta:
        model = PatientVisitInfo
        fields = ('status','weight','height','pulse','systolic','diastolic','bodyTemp')