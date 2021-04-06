from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, EditUserProfile, EditAdminProfile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created Successfully!')
            fm.save()
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
                    return HttpResponseRedirect('/profile/')

        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfile(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfile(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'Your profile updated!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfile(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfile(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {'name':request.user.username, 'form':fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/') 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#With old password
def user_changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successufally!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def userdetail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfile(instance=pi)
        return render(request, 'enroll/userdetail.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
