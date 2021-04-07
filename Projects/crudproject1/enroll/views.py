from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save() # First option for saveing data it save all the field data
            fm = StudentRegistration()

            # Below is second option - it is useful if we don't want to save specific field - dont mention that field for eg. password field
            # name = fm.cleaned_data['name']
            # email = fm.cleaned_data['email']
            # reg = User(name=name, email=email)
            # reg.save()
    else:
        fm = StudentRegistration(request.POST)
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
        
    return render(request, 'enroll/updatestudent.html', {'form':fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/') 