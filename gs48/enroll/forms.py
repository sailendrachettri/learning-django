from django import forms
from django.core import validators
from .models import User

class StudentResgistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password']

