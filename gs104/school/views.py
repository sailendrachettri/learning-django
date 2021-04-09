from django.shortcuts import render
from .models import ExamCenter, MyExamCenter

def home(request):
    exam_center = ExamCenter.objects.all()
    my_exam_center = MyExamCenter.objects.all()
    context = {'centers':exam_center, 'mycenters':my_exam_center}
    return render(request, 'school/home.html', context)