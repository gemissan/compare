import logging

from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout

from comparemain.forms import LoginForm
from comparemain.decorators import redirect_to, redirect_to_index
from comparemessages import get_messages


logger = logging.getLogger(__name__)
authentication_logger = logging.getLogger("authentication")


class LoginView(View):
    form_class = LoginForm
    template = "login.html"
    
    def get(self, request, *args, **kwargs):
        
        form = self.form_class()
        return render(request, self.template, {"form": form})

    def post(self, request, *args, **kwargs):
        
        messages = []
        
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect("index-view")
            else:
                messages.append("incorrect login data")
                authentication_logger.warning("Invalid password for user '%s' from ip %s", form.cleaned_data["username"], request.META.get("REMOTE_ADDR"))
        
        return render(request, self.template, {"form": form, "compare_messages": get_messages(messages)})


@redirect_to_index
def logout_view(request):
    
    logout(request)


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
