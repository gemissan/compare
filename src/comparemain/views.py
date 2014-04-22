import logging

from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout

from comparemain.forms import LoginForm
from comparemain.decorators import redirect_to, redirect_to_index
# from django.contrib import messages


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
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # messages.info(request, "Successful login")
                    authentication_logger.debug("User '%s' was logged in from ip %s", username, request.META.get("REMOTE_ADDR"))
                    return redirect("index-view")
                else:
                    # messages.error(request, "Successful login")
                    authentication_logger.error("User '%s' is not active", username)
            else:
                # messages.error(request, "Incorrect login data")
                authentication_logger.error("Invalid password for user '%s' from ip %s", username, request.META.get("REMOTE_ADDR"))
        
        return render(request, self.template, {"form": form})


@redirect_to_index
def logout_view(request):
    
    if request.user.is_authenticated():
        username = request.user.username
        logout(request)
        
        # messages.info(request, "logged out")
        authentication_logger.info("User '%s' logged out", username)


def register_view(request):
    
    return render_to_response("register.html")


class AboutView(TemplateView):
    
    template_name = "about.html"


def index_view(request):
    
    return render_to_response("index.html")


def profile_view(request):
    
    return render_to_response("profile.html")


@redirect_to("user-profile-view")
def show_user_view(request, user_slug):
    
    pass
