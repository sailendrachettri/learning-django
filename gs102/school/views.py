from django.shortcuts import render
from .models import Student, Teacher, Contractor

def home(request):
    student_data = Student.objects.all()
    teacher_data = Teacher.objects.all()
    contractors_data = Contractor.objects.all()
    return render(request, 'school/home.html', {'students': student_data, 'contractors':contractors_data, 'teachers':teacher_data})