from django import forms
from Visit.models import PatientVisitInfo

class PatientVisitNurseForms(forms.ModelForm):
    class Meta:
        model = PatientVisitInfo
        fields = ('status','weight','height','pulse','systolic','diastolic')

class PatientVisitDoctorForms(forms.ModelForm):
    class Meta:
        model = PatientVisitInfo
        # fields = ('status','weight','height','pulse','systolic','diastolic')

class PatientVisitPhamacistForms(forms.ModelForm):
    class Meta:
        model = PatientVisitInfo
        # fields = ('status','weight','height','pulse','systolic','diastolic')