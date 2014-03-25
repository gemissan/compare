import logging

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.conf import settings


logger = logging.getLogger(__name__)


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
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)
    favourite_lists = models.ManyToManyField("comparelist.CompareList", null=True, related_name="favourited_users")
    favourite_views = models.ManyToManyField("comparelist.CompareView", null=True, related_name="favourited_users")
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
    
    def repository(self, object_type):
        
        try:
            return self.repositories.get(object_type=object_type)
        except Exception:
            # TODO: Change the exception type
            return None
    
    def __unicode__(self):
        return "User[pk=%s, name=%s]" % (self.pk, getattr(self, self.USERNAME_FIELD, None),)


signals_logger = logging.getLogger("signals")

signals_logger.info("Logging signals from %s", __name__)
        
        
def compare_user_set_allowed_objct_types(sender, instance, raw, **kwargs):
    """
    Receiver for post_save CompareUser signal.
    Adds default allowed_compare_objects to user.
    Works only when user has no allowed_compare_objects.
    """
    
    if not raw and not instance.allowed_object_types.all():
        from compareobject.models import CompareObjectType
        from comparelist.models import CompareList
        allowed_types = CompareObjectType.objects.default_object_types().all()
        instance.allowed_object_types = allowed_types
        
        signals_logger.debug("Added allowed types %s for %s", allowed_types, instance)
        
        for allowed_type in allowed_types:
            if not instance.repository(allowed_type):
                repository_list = CompareList.objects.create(
                    repository_owner = instance,
                    name = "%s_repository" % (allowed_type.name),
                    object_type = allowed_type
                )
                
                instance.repositories.add(repository_list)
                
                signals_logger.debug("Added repository list %s for %s", repository_list, instance)
        
        
post_save.connect(compare_user_set_allowed_objct_types, sender=CompareUser)
