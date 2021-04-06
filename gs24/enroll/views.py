from django.shortcuts import render
from enroll.models import Student

def Studentinfo(request):
    stud = Student.objects.all()
    print(stud ,"Debug my code")
    return render(request, 'enroll/studetials.html', {'stu': stud})
