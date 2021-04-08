from django.shortcuts import render
from .models import Student

def home(request):
    # student_data = Student.objects.get(pk=1)
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()

    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('name').last()

    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.all()
    # print(student_data.exists())

    # student_data = Student.objects.all()
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())

    # student_data = Student.objects.create(name= 'Sameer', roll=111, city='Rachi', marks=89, pass_date='2020-2-10')
    # print('Return: ', student_data)

    # student_data, created = Student.objects.get_or_create(name= 'Ameer', roll=112, city='Rachi', marks=80, pass_date='2020-1-10')
    # print('Return: ', created)

    # student_data = Student.objects.filter(roll=108).update(name='Kabirs')
    # student_data = Student.objects.filter(marks=90).update(city='Suntaley')

    # student_data, created = Student.objects.update_or_create(id=13, name='Ameer', defaults={'name': 'Kholi'})
    # print('Return: ', created)

    # objs = [
    #     Student(name = 'Raj', roll=119, city='Dhanbhad', marks=73, pass_date='2020-1-9'),
    #     Student(name = 'Kaij', roll=120, city='Dhanbhad', marks=82, pass_date='2020-2-19'),
    #     Student(name = 'Quazi', roll=121, city='Rachi', marks=17, pass_date='2020-4-19'),
    #     Student(name = 'Raj', roll=116, city='Dhanbhad', marks=73, pass_date='2020-1-9'),
    #     Student(name = 'Kaij', roll=117, city='Dhanbhad', marks=82, pass_date='2020-2-19'),
    #     Student(name = 'Quazi', roll=118, city='Rachi', marks=17, pass_date='2020-4-19'),
    # ]
    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'Subinkhor'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1,2])
    # student_data = Student.objects.in_bulk()

    # student_data = Student.objects.get(pk=13).delete()
    # student_data = Student.objects.filter(marks=80).delete()
    # student_data = Student.objects.all().delete()

    # student_data = Student.objects.all()
    # print(student_data.count())

    student_data = Student.objects.all().explain()

    print(student_data)
    return render(request, 'school/home.html', {'student': student_data})
