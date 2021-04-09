from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

class geekyshowsRedirectView(RedirectView):
    url = 'https://www.google.com'


