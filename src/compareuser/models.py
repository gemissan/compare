from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.conf import settings

from comparelist.models import CompareList


class CompareUser(AbstractBaseUser):
    """
    """
    
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    repository = models.ForeignKey("comparelist.CompareList", related_name="repository_owner")
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL)
    favourite_lists = models.ManyToManyField("comparelist.CompareList", related_name="favourited_users")
    favourite_views = models.ManyToManyField("comparelist.CompareView", related_name="favourited_users")
    allowed_object_types = models.ManyToManyField("compareobject.CompareObjectType")
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    objects = UserManager()
    
    def get_full_name(self):
        
        if self.first_name or self.last_name:
            return "%s %s" % (self.first_name, self.last_name,)
        else:
            return self.get_short_name()
    
    def get_short_name(self):
        
        return self.username
    
    def has_perm(self, perm, obj=None):
    
        return True

    def has_module_perms(self, app_label):
        
        return True
    
    def __unicode__(self):
        return "User[name=%s]" % getattr(self, self.USERNAME_FIELD, "Empty")
    

def compare_user_create_repository(sender, instance, raw, **kwargs):
    
    if not raw and instance.repository is not None:
        repository = CompareList.objects.create(name="repository")
        instance.repository = repository
        
        
pre_save.connect(compare_user_create_repository, sender=CompareUser)
