from django.utils import unittest

from compareyoutube.models import YoutubeArtistCategory


class YoutubeArtistCategoryTestCase(unittest.TestCase):
    
    def test_new_object_has_proper_category_type(self):
        
        youtube_artist = YoutubeArtistCategory.objects.create(name="test")
        
        self.assertEqual(youtube_artist.category_type, YoutubeArtistCategory.default_category_type)
