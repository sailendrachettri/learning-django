from registration import views
from django.urls import path

urlpatterns = [
    path('profile/', views.ProfileTemplateView.as_view(), name='profile'),
]
