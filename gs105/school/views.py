from django.shortcuts import render
from .models import Student
def home(request):
    student_data = Student.students.all()
    context = {'students':student_data}
    return render(request, 'school/home.html', context)