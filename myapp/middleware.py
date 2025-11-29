from django.urls import reverse
from django.shortcuts import redirect

class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            paths_to_redirect = [reverse('spartans:sign_up'), reverse('spartans:sign_in')]
            
            if request.path in paths_to_redirect:
                return redirect(reverse('spartans:index'))

        response = self.get_response(request)
        return response







    