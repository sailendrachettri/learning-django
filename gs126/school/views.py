from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView  
from django.views.generic.base import TemplateView

class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    success_url = 'thankyou/'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'

