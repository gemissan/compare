from django.db import models


class CompareFeatureManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    
    
class CompareListManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)


class CompareViewManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    