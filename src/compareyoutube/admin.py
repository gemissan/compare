from django.contrib import admin

from compareyoutube.models import YoutubeObject


class YoutubeObjectAdmin(admin.ModelAdmin):
    
    pass


admin.site.register(YoutubeObject, YoutubeObjectAdmin)
