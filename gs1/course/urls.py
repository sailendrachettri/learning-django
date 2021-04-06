from course import views
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', views.learn_django, name='learndj'),
    path('var/', views.var, name='var'),
    path('add/', views.add, name='add'),
    path('strf/', views.strf, name='strf'),
    path('altstrf/', views.strf, name='strf'),
]