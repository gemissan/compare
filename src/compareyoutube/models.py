from django.db.models.signals import pre_save

from compareobject.models import CompareCategory, CompareObject
from compareobject.signals import compare_category_set_category_type


class YoutubeArtistCategory(CompareCategory):
    
    default_category_type = "youtube artist"


class YoutubeObject(CompareObject):
    
    @property
    def artists(self):
        
        return self.categories.filter(category_type=YoutubeArtistCategory.default_category_type)
    
    
pre_save.connect(compare_category_set_category_type, sender=YoutubeArtistCategory)
