from django.shortcuts import render_to_response


def index(request):
    
    user = getattr(request, "user", None)
    
    if user and user.is_authenticated():
        return render_to_response("loggedin_index.html", {"user": user})
    else:
        return render_to_response("index.html")


def about(request):
    
    user = getattr(request, "user", None)
    
    return render_to_response("about.html", {"user": user})
