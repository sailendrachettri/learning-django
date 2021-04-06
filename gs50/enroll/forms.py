from django import forms
from django.core import validators
from .models import User

class StudentResgistration(forms.ModelForm):
    name = forms.CharField(max_length=40, required=False)
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name':'Enter Name', 'password':'Enter Password', 'email': 'Enter Email'}
        error_messages = {
            'name': {'required': 'Name cannot be empty!'},
            'password': {'required': 'Paaword cannot be empty!'}
        }
        widgets = {
            'password':forms.PasswordInput
        }

        