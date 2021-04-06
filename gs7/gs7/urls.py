"""gs7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from course import views as cv
from fees import views as fv


coureseperator = [
    path('learndj/', cv.learn_django),
    path('learnpy/', cv.learn_python),
]

feesseperator = [
    path('learndj/', fv.learn_django),
    path('learnpy/', fv.learn_python),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cor/', include(coureseperator)),
    path('fe/', include(feesseperator)),

    #Remove below lines and run server
       """
    path('cor/', include([
        path('learndj/', cv.learn_django),
        path('learnpy/', cv.learn_python),
    ])),
    path('fe/', include([
        path('learndj/', fv.learn_django),
        path('learnpy/', fv.learn_python),
    ])),
    """
]
