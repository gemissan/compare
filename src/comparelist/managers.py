from django.db import models


class CompareFeatureManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    
    
class CompareListManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    
    def get_queryset(self):
        
        return super(CompareListManager, self).get_queryset().prefetch_related("object_type")


class CompareViewManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)
    