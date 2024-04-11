# middleware.py
from django.shortcuts import redirect
from django.urls import reverse


class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path.startswith(reverse('admin:index')):
            return redirect('admin:login')

        return self.get_response(request)
