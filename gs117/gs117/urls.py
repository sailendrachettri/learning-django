from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='home'),
    path('home/', views.RedirectView.as_view(url='/'), name='home'),
    # path('index/', views.RedirectView.as_view(url='/'), name='index'),
    # path('gs/', views.RedirectView.as_view(url='https://www.geekyshows.com'), name='Geeky snow'),
    # path('google/', views.geekyshowsRedirectView.as_view(), name='Google'),

    path('index/', views.RedirectView.as_view(pattern_name='home'), name='index'),
]
