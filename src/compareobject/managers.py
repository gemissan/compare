from django.db import models


class CompareObjectTypeManager(models.Manager):

    def default_object_types(self):
        
        return self.filter(default=True)