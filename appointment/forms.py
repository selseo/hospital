from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Department
from .models import Doctor

department = Department.objects.all()
doctor = Doctor.objects.all()
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('1', 'Morning'),
    ('2', 'Afternoon'),
)

class AppForm(forms.Form):
	department = forms.ModelChoiceField(queryset=department, to_field_name="name", required=True, empty_label="--- Select Department ---",
		widget=forms.Select(attrs={'id': 'department', 'class': 'form-control'}))
	doctor = forms.ChoiceField(required=True,
		widget=forms.Select(attrs={'id': 'doctor', 'class': 'form-control'}))
	appointment = forms.ChoiceField(required=True,
		widget=forms.Select(attrs={'id': 'appointment', 'class': 'form-control'}))
	symptom = forms.CharField(widget=forms.Textarea(
		attrs={'id': 'symptom', 'class': 'form-control', 'rows': 4, 'placeholder' : 'Describe your symptoms here ....'}))
	cause = forms.CharField(widget=forms.Textarea(
		attrs={'id': 'cause', 'class': 'form-control', 'rows': 4, 'placeholder' : 'Describe your causes here ....'}))

class AppByStaff(forms.Form):
	patientid = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': 'Patient ID', 'id': 'patientid', 'class': 'form-control'}))
	patientidcard = forms.CharField(label='Patient ID Card', max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Citizen ID', 'id': 'patientidcard', 'class': 'form-control'}))
	patientname = forms.CharField(label='Your name', max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Patient Name', 'id': 'patientname', 'class': 'form-control', 'disabled' : 'disabled'}))
	department = forms.ModelChoiceField(queryset=department, to_field_name="name", required=True, empty_label="--- Select Department ---",
		widget=forms.Select(attrs={'id': 'department', 'class': 'form-control'}))
	doctor = forms.ChoiceField(required=True,
		widget=forms.Select(attrs={'id': 'doctor', 'class': 'form-control'}))
	appointment = forms.ChoiceField(required=True,
		widget=forms.Select(attrs={'id': 'appointment', 'class': 'form-control'}))
	symptom = forms.CharField(widget=forms.Textarea(
		attrs={'id': 'symptom', 'class': 'form-control', 'rows': 4, 'placeholder' : 'Describe your symptoms here ....'}))
	cause = forms.CharField(widget=forms.Textarea(
		attrs={'id': 'cause', 'class': 'form-control', 'rows': 4, 'placeholder' : 'Describe your causes here ....'}))
	
