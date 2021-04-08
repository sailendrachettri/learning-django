from django.shortcuts import render
from .models import Student
from datetime import date, time

def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(name__exact='Sailendra') #Case sensitive
    # student_data = Student.objects.filter(name__iexact='sailendra') #Case insensitive

    # student_data = Student.objects.filter(name__contains='u')

    # student_data = Student.objects.filter(id__in=[1, 5, 7])

    # student_data = Student.objects.filter(marks__in=[100, 90])

    # student_data = Student.objects.filter(marks__gt= 90)
    # student_data = Student.objects.filter(marks__gte= 90)

    # student_data = Student.objects.filter(marks__lt= 97)
    # student_data = Student.objects.filter(marks__lte= 90)

    # student_data = Student.objects.filter(name__startswith = 'S')
    # student_data = Student.objects.filter(name__endswith = 'a')

    # student_data = Student.objects.filter(passdate__range = ('2021-1-10', '2021-4-9')) #YYYY-MM-DD

    # student_data = Student.objects.filter(admdatetime__date = date(2021, 4, 8))
    # student_data = Student.objects.filter(admdatetime__date__gt = date(2021, 2, 8))
    # student_data = Student.objects.filter(admdatetime__date__gte = date(2021, 2, 8))
    # student_data = Student.objects.filter(admdatetime__date__lt = date(2021, 4, 8))
    # student_data = Student.objects.filter(admdatetime__date__lte = date(2021, 4, 8))

    # student_data = Student.objects.filter(passdate__year = 2021)
    # student_data = Student.objects.filter(passdate__year__gt = 2020)
    # student_data = Student.objects.filter(passdate__year__lt = 2022)
    # student_data = Student.objects.filter(passdate__month = 4)
    # student_data = Student.objects.filter(passdate__month__gt= 4)
    # student_data = Student.objects.filter(passdate__month__lt= 4)
    # student_data = Student.objects.filter(passdate__month__gte= 4)
    # student_data = Student.objects.filter(passdate__day= 8)
    # student_data = Student.objects.filter(passdate__day__gt= 8)
    # student_data = Student.objects.filter(passdate__day__gte= 8)
    # student_data = Student.objects.filter(passdate__week= 2)
    # student_data = Student.objects.filter(passdate__week__gt= 12)
    # student_data = Student.objects.filter(passdate__week__gt= 12)
    # student_data = Student.objects.filter(passdate__week_day= 2)

    # student_data = Student.objects.filter(admdatetime__time__gt= time(13, 00))
    # student_data = Student.objects.filter(admdatetime__hour__gt=10)
    # student_data = Student.objects.filter(admdatetime__minute__gt=20)
    # student_data = Student.objects.filter(admdatetime__second__gt=40)
    # student_data = Student.objects.filter(roll__isnull=False)
    # student_data = Student.objects.filter(roll__isnull=True)

 
    print('Return: ', student_data)
    print('<-----------------<--------------------->-------------------->')
    print('SQL Query: ', student_data.query)
    return render(request, 'school/home.html', {'students': student_data})