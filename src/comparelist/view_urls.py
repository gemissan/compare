from django.conf.urls import patterns, url


urlpatterns = patterns("comparelist.views",
    url(r"(?P<view_id>\d+)$", "show", name="show-listview-view"),
    url(r"create$", "create", name="create-listview-view"),
    url(r"", "index", name="index-listview-view")
)
