from django.db.models.signals import pre_save

from django.db import models
from compareobject.models import CompareCategory, CompareObject, compare_category_set_category_type


class YoutubeArtistCategory(CompareCategory):
    
    default_category_type = "youtube artist"


class YoutubeObject(CompareObject):
    
    url = models.CharField(max_length=400)
    embed_url = models.CharField(max_length=400)
    
    @property
    def artists(self):
        
        return self.categories.filter(category_type=YoutubeArtistCategory.default_category_type)

    
pre_save.connect(compare_category_set_category_type, sender=YoutubeArtistCategory)
