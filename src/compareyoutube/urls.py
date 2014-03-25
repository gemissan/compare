from django.conf.urls import patterns, url


urlpatterns = patterns("compareyoutube.views",
    url(r"", "index", name="youtube_index"),
    url(r"(?P<username>\w+)/list/(?P<list_name>\w+)", "list", name="youtube_list"))