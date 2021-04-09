from django.shortcuts import render
from .models import Student, ExamCenter

def home(request):
    student_data = Student.objects.all()
    examcenter_data = ExamCenter.objects.all()
    return render(request, 'school/home.html', {'students':student_data, 'centers':examcenter_data})