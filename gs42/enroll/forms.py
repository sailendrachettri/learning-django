from django import forms
from django.core import validators


def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Name should starts with s')

class StudentResgistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField(validators=[starts_with_s])
    email = forms.EmailField()

    



