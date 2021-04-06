from django.urls import path
from . import views

urlpatterns = [
    path('', views.showformdata),
    path('success/', views.thankyou, name='success')
]
