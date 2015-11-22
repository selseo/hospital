from django import forms
from Visit.models import PatientVisitInfo

class PatientVisitNurseForms(forms.ModelForm):
    class Meta:
        model = PatientVisitInfo
        fields = ('weight','height','pulse','systolic','diastolic')