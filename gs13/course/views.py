from django.shortcuts import render
from datetime import datetime

def learn_django(request):
    
    data = {
        'stu1': {'name':'Rahul', 'roll': 101},
        'stu2': {'name':'Sonam', 'roll': 102},
        'stu3': {'name':'Raj', 'roll': 103},
        'stu4': {'name':'Anu', 'roll': 104},
        }
    
    return render(request, 'course/courseone.html', {'data': data})