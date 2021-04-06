from django import forms

class StudentResgistration(forms.Form):
    # name = forms.CharField(widget=forms.PasswordInput)
    # name = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(widget=forms.Textarea(attrs={'class':'somecss1'}))
    # name = forms.CharField(widget=forms.CheckboxInput())
    # name = forms.CharField(widget=forms.FileInput())

