from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, EditUserProfile, EditAdminProfile
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created Successfully!')
            user = fm.save()
            group = Group.objects.get(name='Editors')
            user.groups.add(group)
    else:
        fm = SignupForm()
    return render(request, 'enroll/signup.html', {'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in Successfully!') #auto pass this message
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html', {'name':request.user.username})
        
    else:
        return HttpResponseRedirect('/login/') 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')