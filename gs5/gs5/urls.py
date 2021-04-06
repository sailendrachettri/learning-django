# from fees import views as fv
# from course import views as cv
# or

from fees.views import learn_python
from course.views import learn_django

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learnpy/', learn_python),
    path('learndj/', learn_django),
]
