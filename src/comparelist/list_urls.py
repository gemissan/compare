from django.conf.urls import patterns, url


urlpatterns = patterns("comparelist.list_views",
    url(r"repository", "repository", name="show-repository-view"),
    url(r"all", "all_lists", name="show-all-lists-view"),
    url(r"(?P<list_id>\d+)$", "show_list", name="show-list-view"),
    url(r"create$", "create_list", name="create-list-view"),
    url(r"", "index", name="index-list-view")
)
