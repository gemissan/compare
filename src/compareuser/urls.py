from django.conf.urls import patterns, url


urlpatterns = patterns("compareuser.views",
    url(r"login$", "login", name="login_view"),
    url(r"logout$", "logout", name="logout_view")
)
