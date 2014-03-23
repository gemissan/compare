from compareobject.models import CompareCategory, CompareObject


class YoutubeArtistCategory(CompareCategory):
    
    default_category_type = "youtube artist"


class YoutubeObject(CompareObject):
    
    @property
    def artists(self):
        
        return self.categories.filter(category_type=YoutubeArtistCategory.default_category_type)
