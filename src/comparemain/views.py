import logging

from django.shortcuts import render, render_to_response
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login

from comparemain.forms import LoginForm


logger = logging.getLogger(__name__)
authentication_logger = logging.getLogger("authentication")


class LoginView(View):
    form_class = LoginForm
    template = "login.html"
    
    def get(self, request, *args, **kwargs):
        
        form = self.form_class()
        return render(request, self.template, {"form": form})

    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return index(request)
            else:
                authentication_logger.warning("Invalid password for user '%s' from ip %s", form.cleaned_data["username"], request.META.get("REMOTE_ADDR"))
        
        return render(request, self.template, {"form": form})


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
