from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session.set_expiry(10) #Expire in 10 seconds
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session['name']
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_age())
    # print(request.session.get_expiry_date())
    # print(request.session.get_expire_at_browser_close())
    return render(request, 'student/getsession.html', {'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')