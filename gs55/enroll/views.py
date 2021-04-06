from django.shortcuts import render
from .forms import StudentRegistration

def show_form_data(request):
    fm = StudentRegistration()
    return render(request, 'enroll/userreg.html', {'form':fm})
