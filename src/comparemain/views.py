import logging

from django.shortcuts import render_to_response
from django.views.generic import TemplateView


logger = logging.getLogger(__name__)


def login(request):
    
    return render_to_response("login.html")


def logout(request):
    
    return


def register(request):
    
    return render_to_response("register.html")


class AboutView(TemplateView):
    
    template_name = "about.html"


def index(request):
    
    return render_to_response("index.html")

def profile(request):
    
    return render_to_response("profile.html")

def show_user(request, user_slug):
    
    return
