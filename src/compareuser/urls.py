from django.conf.urls import patterns, url


urlpatterns = patterns("compareuser.views",
    url(r"login$", "login", name="login_user_view"),
    url(r"logout$", "logout", name="logout_user_view"),
    url(r"create$", "create", name="create_user_view"),
    url(r"(?P<user_id>\d+)$", "show", name="show_user_view")
)
