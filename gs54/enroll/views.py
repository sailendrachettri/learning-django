from django.shortcuts import render
    
def show_details(request, year):
    student = {'yr':year}
    return render(request, 'enroll/show.html', student) 