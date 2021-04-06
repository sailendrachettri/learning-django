from django.urls import path
from . import views

urlpatterns = [
    path('', views.course),
    path('home/', views.home),

]
