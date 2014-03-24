import logging

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.conf import settings


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
    repository = models.ForeignKey("comparelist.CompareList", related_name="repository_owner")
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
    
    def __unicode__(self):
        return "User[name=%s]" % getattr(self, self.USERNAME_FIELD, "Empty")


signals_logger = logging.getLogger("signals")

signals_logger.info("Logging signals from %s", __name__)


def compare_user_create_repository(sender, instance, raw, **kwargs):
    
    if not raw and not instance.pk:
        from comparelist.models import CompareList
        repository = CompareList.objects.create(name="repository")
        instance.repository = repository
        
        signals_logger.debug("Created repository for %s", instance)
        
        
def compare_user_set_allowed_objct_types(sender, instance, raw, **kwargs):
    
    if not raw and instance.date_joined == instance.date_updated:
        from compareobject.models import CompareObjectType
        allowed_types = CompareObjectType.objects.default_object_types().all()
        instance.allowed_object_types = allowed_types
        
        signals_logger.debug("Added allowed types %s for %s", allowed_types, instance)
        
        
pre_save.connect(compare_user_create_repository, sender=CompareUser)
post_save.connect(compare_user_set_allowed_objct_types, sender=CompareUser)
