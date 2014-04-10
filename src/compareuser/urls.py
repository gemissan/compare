from django.conf.urls import patterns, url


urlpatterns = patterns("compareuser.views",
    url(r"(?P<user_slug>\w+)$", "show", name="show-user-view")
)
