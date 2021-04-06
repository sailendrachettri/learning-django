from django.urls import path
from fees import views

urlpatterns = [
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
]