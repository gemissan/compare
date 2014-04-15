from django.db import models


class CompareFeatureManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    
    
class CompareListManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    
    def get_query_set(self):
        
        return models.Manager.prefetch_related("object_type").get_query_set(self)


class CompareViewManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    