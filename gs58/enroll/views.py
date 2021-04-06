from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request, messages.SUCCESS, 'You account has been created!') #OR below one bothe are same
            # messages.success(request, 'You account has been created!')
            messages.info(request, 'Now you can login!')
            print(messages.get_level(request))
            messages.debug(request, 'Debug!')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'New Debug Debug!')
            print(messages.get_level(request))
            
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})
