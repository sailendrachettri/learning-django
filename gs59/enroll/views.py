from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages


def regi(request):
    messages.info(request, 'Now You can login')
    messages.success(request, 'Succefually created')
    messages.warning(request, 'Warning message here man!')
    messages.error(request, 'Error message here man!')
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})
