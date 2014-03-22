from django.conf.urls import patterns, url


urlpatterns = patterns("",
    url(r"^$", "compareobject.views.index", name="index_view"),
    )