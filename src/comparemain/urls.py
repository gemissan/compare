from django.conf.urls import patterns, url


urlpatterns = patterns("comparemain.views",
    url(r"^$", "index", name="index_view"),
    url(r"^about/?", "about", name="about_view"))