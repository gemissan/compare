import logging

from django.shortcuts import render, redirect
from django.contrib import auth

from compareuser.forms import LoginForm


logger = logging.getLogger(__name__) 


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
