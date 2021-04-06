from django.shortcuts import render


def learn_django(request):
    # return render(request, 'course/courseone.html', context = coursename)
    # return render(request, 'course/courseone.html', coursename)
    return render(request, 'course/courseone.html', {'cname': 'Django'})

def learn_python(request):
    one = '1sfvav'
    two = '2avabva'
    three = '3vaabveer'
    context = {'one': one, 'three':two, 'two':three}
    return render(request, 'course/coursetwo.html', context)
    
