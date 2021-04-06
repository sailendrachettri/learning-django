from django.shortcuts import render
from .forms import StudentResgistration

def showformdata(request):
    fm = StudentResgistration()
    fm.order_fields(field_order=['email', 'name', 'first_name'])
    return render(request, 'enroll/userregistration.html', {'form': fm})