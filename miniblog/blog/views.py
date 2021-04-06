from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SighUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group



# **********************HOME*********************
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})


# **********************ABOUT*********************
def about(request):
    return render(request, 'blog/about.html')


# **********************CONTACT*********************
def contact(request):
    return render(request, 'blog/contact.html')


# **********************DASHBOARD*********************
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('/login/') 


# **********************SIGNUP*********************
def user_signup(request):
    if request.method == 'POST':
        form = SighUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! You have become an Author.')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            # return HttpResponseRedirect('/')
    else:
        form = SighUpForm()
    return render(request, 'blog/signup.html', {'form':form})


# **********************LOGOUT*********************
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# **********************LOGIN*********************
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


# **********************ADD NEW POST*********************
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc) 
                pst.save()
                messages.success(request, 'Post Added Successfully!')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

# **********************UPDATE POST*********************
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')


# **********************DELETE POST*********************
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
        return HttpResponseRedirect('/dashboard/')
    
    else:
        return HttpResponseRedirect('/login/')