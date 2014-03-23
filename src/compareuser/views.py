import logging

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import auth

from compareuser.forms import LoginForm, CreateUserForm


logger = logging.getLogger(__name__)

User = get_user_model()


def login(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["name"]
            user = auth.authenticate(name=username)
            if user:
                if user.is_active:
                    login_user(request, user)
                    
                    return redirect("index_view")
            else:
                logger.warning("Unsuccessfull login attempt for username %s", username)
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})


def logout(request):
    
    logout_user(request)
    
    return redirect("index_view")


def create(request):
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            login_user(request, form.instance)
            
            return redirect("index_view")
    else:
        form = CreateUserForm()
    
    return render(request, "create.html", {"form": form})


def show(request, user_id):
    
    shown_user = get_object_or_404(User, pk=user_id)
    user = getattr(request, "user", None)
    
    return render_to_response("show.html", {"user": user, "shown_user": shown_user})


def login_user(request, user):
    
    auth.login(request, user)
                    
    logger.debug("Logged in user %s", user)
    
    return True


def logout_user(request):
    
    user = getattr(request, "user", None)
    
    if user:
        logger.debug("User %s logged out", user)
        auth.logout(request)
    
    return bool(user)