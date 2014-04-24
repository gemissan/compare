from django.conf.urls import patterns, url

from compareyoutube.views import ShowRepositoryView, ShowListView


urlpatterns = patterns("compareyoutube.views",
    url(r"list/(?P<list_id>\d+)$", ShowListView.as_view(), name="show-youtube-list-view"),
    url(r"list/create$", "create_list", name="create-youtube-list-view"),
    url(r"view/(?P<view_id>\d+)$", "show_view", name="show-youtube-listview-view"),
    url(r"view/create$", "create_view", name="create-youtube-listview-view"),
    url(r"", ShowRepositoryView.as_view(), name="show-youtube-index-view")
)
