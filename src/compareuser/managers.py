from django.contrib.auth.models import UserManager

class CompareUserManager(UserManager):

    def get_by_natural_key(self, username):
        
        return self.get(username=username)