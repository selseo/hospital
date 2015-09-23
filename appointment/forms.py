from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Department

department = Department.objects.all()
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('1', 'เช้า'),
    ('2', 'บ่าย'),
)

class AppForm(forms.Form):
	Department = forms.ModelChoiceField(queryset=department,to_field_name="name")

	Doctor = forms.CharField(required=True,max_length=100)
	Date = forms.DateField(widget=SelectDateWidget())
	Time = forms.MultipleChoiceField(required=True,
		widget=forms.CheckboxSelectMultiple, 
		choices=FAVORITE_COLORS_CHOICES)
	Symptom = forms.CharField(widget=forms.Textarea)
	Cause = forms.CharField(widget=forms.Textarea)

	Doctor.widget.attrs['class'] = 'form-control'
	Date.widget.attrs['class'] = 'form-control'
	Symptom.widget.attrs['class'] = 'form-control'
	Cause.widget.attrs['class'] = 'form-control'