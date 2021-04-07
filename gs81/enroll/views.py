from django.shortcuts import render
# from django.views.decorators.cache import cache_page


# Only for home cache
# @cache_page(20)
def home(request):
    return render(request, 'enroll/course.html')

def contact(request):
    return render(request, 'enroll/contact.html')

def about(request):
    return render(request, 'enroll/about.html')