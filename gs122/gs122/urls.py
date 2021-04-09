from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='studentdetail'),

]
