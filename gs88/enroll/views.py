from django.shortcuts import render
from django.core.cache import cache



# def home(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'The Manjhi', 20)
#         mv = cache.get('movie')
#     return render(request, 'enroll/course.html', {'fm':mv})

# def home(request):
#     mv = cache.get_or_set('fees', 1000, 20, version=2)
#     return render(request, 'enroll/course.html', {'fm':mv})

# def home(request):
#     data = {'name': 'Sailendra', 'roll': 101}
#     cache.set_many(data, 30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request, 'enroll/course.html', {'stu':sv})

def home(request):
    cache.delete('roll')
    return render(request, 'enroll/course.html')

