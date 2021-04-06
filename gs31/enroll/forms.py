from django import forms

class StudentResgistration(forms.Form):
    name = forms.CharField(initial='Sonal', help_text="Only 30 character allowed")
    # email = forms.EmailField()
    # first_name = forms.CharField()