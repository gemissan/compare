from django.db import models


class CompareObjectTypeManager(models.Manager):
    
    def get_by_natural_key(self, name):
        
        return self.get(name=name)

    def default_object_types(self):
        
        return self.filter(default=True)