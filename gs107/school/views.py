from django.shortcuts import render
from .models import Student
def home(request):
    student_data = Student.students.get_stu_roll_range(101, 107) 
    # student_data = Student.objects.all()
    context = {'students':student_data}
    return render(request, 'school/home.html', context) 