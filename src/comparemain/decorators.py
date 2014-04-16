from functools import wraps

from django.shortcuts import redirect


def redirect_to(to):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            return redirect(to)
        return inner
    return wrapper


def redirect_to_index(func):
    return redirect_to("index-view")(func)