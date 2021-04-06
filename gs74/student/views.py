from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')