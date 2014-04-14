from django.conf.urls import patterns, url


urlpatterns = patterns("comparemain.views",
    url(r"login$", "login", name="login-user-view"),
    url(r"logout$", "logout", name="logout-user-view"),
    url(r"register$", "register", name="register-new-user-view"),
    url(r"profile$", "profile", name="user-profile-view"),
    url(r"user/(?P<user_slug>\w+)$", "show_user", name="show-user-view"),
    url(r"about$", "about", name="about-view"),
    url(r"", "index", name="index-view"),
)
