from school import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.StudentCreateView.as_view(), name= 'create'), 
    path('thanks/', views.ThanksTemplateView.as_view(), name= 'thanks'), 
]
