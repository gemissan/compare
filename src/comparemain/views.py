import logging

from django.shortcuts import render_to_response
from django.views.generic import View, TemplateView


logger = logging.getLogger(__name__)


def LoginView(View):
    
    def get(self, request, *args, **kwargs):
        
        return render_to_response("login.html")

    def post(self, request, *args, **kwargs):
        
        return render_to_response("login.html")


def logout(request):
    
    return LoginView.as_view()(request)


def register(request):
    
    return render_to_response("register.html")


class AboutView(TemplateView):
    
    template_name = "about.html"


def index(request):
    
    return render_to_response("index.html")

def profile(request):
    
    return render_to_response("profile.html")

def show_user(request, user_slug):
    
    return profile(request)
