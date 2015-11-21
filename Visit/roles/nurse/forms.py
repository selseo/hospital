from django import forms
from Visit.models import PatientVisitInfo

class PatientVisitForms(forms.ModelForm):
    class Meta:
        model = PatientVisitInfo
        fields = '__all__'