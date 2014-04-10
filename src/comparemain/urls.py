from django.conf.urls import patterns, url


urlpatterns = patterns("comparemain.views",
    url(r"login$", "login", name="login-view"),
    url(r"logout$", "logout", name="logout-view"),
    url(r"create$", "create", name="create-user-view"),
    url(r"^about$", "about", name="about-view"),
    url(r"^$", "index", name="index-view"),
)