from django.conf.urls import patterns, url

urlpatterns = patterns("compareuser.views",
    url(r"login/?$", "login_user_view", name="login_user_view"))