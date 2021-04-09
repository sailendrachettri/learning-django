from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

#-----------------------------FUNCTION BASED VIEW--------------------------------
def myview(request):
    return HttpResponse('<h1>FUNCTION BASED VIEW </h1>')


#---------------------------------CLASS BASED VIEW---------------------------------
class MyView(View):
    name = 'Sonam'
    def get(self, request):
        # return HttpResponse('<h1>CLASS BASED VIEW - GET</h1>')
        return HttpResponse(self.name) 

# class MyViewChild(MyView):
#     def get(self, request):
#         return HttpResponse(self.name)
