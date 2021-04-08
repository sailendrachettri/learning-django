from django.shortcuts import render

class UnderCinstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Call from middleware before view')
        response = render(request, 'mysite/siteuc.html')
        print('Call from middleware after view')
        return response