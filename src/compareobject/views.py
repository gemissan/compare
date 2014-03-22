from django.shortcuts import render_to_response

from compareobject.models import CompareObject


def index(request):
    """
    """
    
    user = None
    
    if hasattr(request, "user"):
        user = request.user
    
    return render_to_response("index.html", {"user": user})
