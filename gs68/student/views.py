from django.shortcuts import render
from datetime import datetime, timedelta

def setcookie(request):
    response = render(request, 'student/setcookie.html') #this is response object #response is our custome variable you can use anu variable 
    # response.set_cookie('name', 'sonam', max_age=60) #age in seconds
    response.set_cookie('lname', 'Jha', expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    # name = request.COOKIES['name'] # it gives error if name is not set in cilent's machine. Below method is safe
    name = request.COOKIES.get('name', 'Default Value For Sonam by default none')
    return render(request, 'student/getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response