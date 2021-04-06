from django.urls import path
from . import views

urlpatterns = [
    path("learn/", views.fees_django)
]
