from django import forms
from django.contrib.auth.models import User
from Authentication.models import UserProfile,Patient


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstname','lastname','sex','idcard','phone')
