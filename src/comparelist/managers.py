from django.db import models


class CompareFeatureManager(models.Manager):
    
    def get_by_natural_key(self, user_id, name):
        
        if user_id:
            return self.get(user__id=user_id, name=name)
        else:
            return self.get(user=None, name=name)
    