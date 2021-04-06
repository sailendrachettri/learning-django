from django.shortcuts import render
from .forms import StudentResgistration

def showformdata(request):
    fm = StudentResgistration(initial={'name': 'Raj'})
    return render(request, 'enroll/userregistration.html', {'form': fm})