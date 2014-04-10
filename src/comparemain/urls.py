from django.conf.urls import patterns, url


urlpatterns = patterns("comparemain.views",
    url(r"login$", "login", name="login-user-view"),
    url(r"logout$", "logout", name="logout-user-view"),
    url(r"new", "new", name="new-user-view"),
    url(r"about$", "about", name="about-view"),
    url(r"", "index", name="index-view"),
)