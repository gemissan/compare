from django.shortcuts import render_to_response


def index(request):
    
    user = getattr(request, "user", None)
    
    return render_to_response("index.html", {"user": user})


def about(request):
    
    user = getattr(request, "user", None)
    
    return render_to_response("about.html", {"user": user})
