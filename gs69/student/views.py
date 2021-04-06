from django.shortcuts import render
from datetime import datetime, timedelta

def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_signed_cookie('name', 'Sonam', salt= 'nm',  expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    name = request.get_signed_cookie('name', default='Guest', salt='nm')
    return render(request, 'student/getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response