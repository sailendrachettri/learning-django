from django.shortcuts import render
from .models import Student
from django.db.models import Q
def home(request):
   
    # student_data = Student.objects.filter(Q(id=1) & Q(roll=101))
    # student_data = Student.objects.filter(Q(id=1) | Q(roll=102))
    student_data = Student.objects.filter(~Q(id=6))

    
    print('Return: ', student_data)
    print('<-----------------<--------------------->-------------------->')
    print('SQL Query: ', student_data.query)
    return render(request, 'school/home.html', {'students':student_data})