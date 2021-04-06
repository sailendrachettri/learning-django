from django.shortcuts import render


def learn_django(request):
    return render(request, 'fees/feesone.html')

def learn_python(request):
    return render(request, 'fees/feestwo.html')
    
