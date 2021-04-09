from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

def homefun(request):
    return render(request, 'school/home.html')

class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html') 

#--------------------------------------------------------------------------------------------
def aboutfun(request):
    context = {'msg': 'Welcome to GS Function View'}
    return render(request, 'school/about.html', context)

class AbotClassView(View):
    def get(self, request):
        context = {'msg': 'Welcome to GS Class Based View'}
        return render(request, 'school/about.html', context)

#--------------------------------------------------------------------------------------------

def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You form Submitted!')
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form':form})

class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form':form}) 

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You form Submitted!')


#------------------------------------------------------------------------------------------
def newsfun(request, template_name):
    context = {'info': 'CBI enquiry why GK earns less money'}
    return render(request, template_name, context)

class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info': 'CBI enquiry why GK earns less money'}
        return render(request, self.template_name, context)

    