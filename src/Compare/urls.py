from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns("",
    url(r"^admin", include(admin.site.urls)),
    url(r"^user/", include("compareuser.urls")),
    url(r"^youtube/", include("compareyoutube.urls")),
    url(r"", include("comparemain.urls")))