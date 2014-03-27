from django.db import models


class CompareObjectTypeManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)

    def default_object_types(self):
        
        return self.filter(default=True)
    
    
class CompareCategoryManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    