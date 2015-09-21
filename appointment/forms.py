from django import forms
from django.forms.extras.widgets import SelectDateWidget

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('เช้า', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

class AppForm(forms.Form):
	Doctor = forms.CharField(required=True,max_length=100)
	Doctor.widget.attrs['class'] = 'form-control'

	Date = forms.DateField(widget=SelectDateWidget())
	Date.widget.attrs['class'] = 'form-control'

	Time = forms.MultipleChoiceField(required=True,
		widget=forms.CheckboxSelectMultiple, 
		choices=FAVORITE_COLORS_CHOICES)
	

	Symptom = forms.CharField(widget=forms.Textarea)
	Symptom.widget.attrs['class'] = 'form-control'

	Cause = forms.CharField(widget=forms.Textarea)
	Cause.widget.attrs['class'] = 'form-control'