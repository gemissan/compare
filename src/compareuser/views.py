import logging

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login

from compareuser.forms import LoginForm
from compareobject.views import index


logger = logging.getLogger(__name__) 


def login_user_view(request):
    """
    """
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["name"]
            user = authenticate(name=username)
            if user:
                if user.is_active:
                    login(request, user)
                    
                    logger.debug("Logged in user %s" % user)
                    
                    return index(request)
            else:
                logger.warning("Unfortunately user %s couldn't log in" % (username,))
    else:
        form = LoginForm()
    
    return render_to_response("user_login.html", {"form": form}, RequestContext(request))
