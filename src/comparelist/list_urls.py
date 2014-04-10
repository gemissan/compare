from django.conf.urls import patterns, url


urlpatterns = patterns("comparelist.list_views",
    url(r"(?P<list_id>\d+)$", "show", name="show-list-view"),
    url(r"create$", "create", name="create-list-view"),
    url(r"", "index", name="index-list-view")
)
