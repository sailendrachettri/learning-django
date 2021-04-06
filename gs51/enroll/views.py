from django.shortcuts import render
from .forms import StudentResgistration
from django.http import HttpResponseRedirect
from .models import User
    
def showformdata(request):
    if request.method == 'POST':
        pi = User.objects.get(pk=1)
        fm = StudentResgistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()


    else:
        fm = StudentResgistration()

    return render(request, 'enroll/userregistration.html', {'form': fm})