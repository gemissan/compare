from functools import wraps

from compareuser.views import login_redirect

def require_login(view):
    """
    """
    
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if hasattr(request, "user") and request.user.is_authenticated():
            return view(request, *args, **kwargs)
        else:
            return login_redirect()
    
    return wrapper

