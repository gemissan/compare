from django.conf.urls import patterns, url

from comparemain.views import LoginView, AboutView


urlpatterns = patterns("comparemain.views",
    url(r"login$", LoginView.as_view(), name="login-user-view"),
    url(r"logout$", "logout_view", name="logout-user-view"),
    url(r"register$", "register_view", name="register-new-user-view"),
    url(r"profile$", "profile_view", name="user-profile-view"),
    url(r"user/(?P<user_slug>\w+)$", "show_user_view", name="show-user-view"),
    url(r"about$", AboutView.as_view(), name="about-view"),
    url(r"", "index_view", name="index-view"),
)
