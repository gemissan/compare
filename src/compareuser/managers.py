from django.contrib.auth.models import UserManager

class CompareUserManager(UserManager):

    def get_by_natural_key(self, slug):
        
        return self.get(slug=slug)