from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

def home(request):
    # student_data = Student.objects.all() #student models interact with database
    # student_data = Student.objects.filter(marks=87)
    # student_data = Student.objects.exclude(marks=87)
    # student_data = Student.objects.order_by('marks') #Acending order
    # student_data = Student.objects.order_by('-marks') #Decending order
    # student_data = Student.objects.order_by('?') #Randomly order
    # student_data = Student.objects.order_by('id')[:5] 
    # student_data = Student.objects.order_by('id').reverse()[:5] 
    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name', 'city') 
    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('id', 'name')
    # student_data = Student.objects.values_list('id', 'name', named=True)
    # student_data = Student.objects.using('default') #Database name in our case 'default' is our database | it is useful when we've to work on multiple databases
    # student_data = Student.objects.dates('pass_date', 'month')

#--------------------------------Teacher's table - second table--------------------------
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1) 

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.intersection(qs1) 

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs1.difference(qs2) 

#----------------------------------------------AND, OR Operator-----------------------------
    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6, roll=106) #Same as above using comma
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))  #Same as above two lines - first import Q

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=102)
    student_data = Student.objects.filter(Q(id=6) | Q(roll=101))  #Same as above line - first import Q

    



    print('Return: ', student_data)
    print('===========================================>')
    print('SQL Query: ', student_data.query)
    return render(request, 'school/home.html', {'students': student_data})
