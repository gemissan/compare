import logging

from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField

from compareuser.managers import CompareUserManager


logger = logging.getLogger(__name__)


class CompareUser(AbstractBaseUser):
    """
    """
    
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="username")
    first_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    last_name = models.CharField(max_length=100, null=True, blank=True, default=None)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    favourite_lists = models.ManyToManyField("comparelist.CompareList", blank=True, related_name="favourited_users")
    favourite_views = models.ManyToManyField("comparelist.CompareView", blank=True, related_name="favourited_users")
    allowed_object_types = models.ManyToManyField("compareobject.CompareObjectType", blank=True)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    objects = CompareUserManager()
    
    @property
    def main_repository(self):
        
        from comparelist.models import CompareList
        try:
            return self.repositories.get(object_type=None)
        except CompareList.DoesNotExist:
            logger.critical("User %s does not have main repository", self)
            raise
    
    def natural_key(self):
        
        return (self.slug,)
    
    def get_absolute_url(self):
        
        return reverse("show-user-view", args=[self.slug])
    
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
    
    def get_repository(self, object_type):
        """
        Get user repository list with type <object_type>.
        Returns None if repository with that type does not exist.
        Returns False if repository exists but is not accessible.
        """
        
        if object_type in self.allowed_object_types.all():
            from comparelist.models import CompareList
            try:
                return self.repositories.get(object_type=object_type)
            except CompareList.DoesNotExist:
                return None
        else:
            return False
    
    def __unicode__(self):
        return "User[pk=%s, name=%s]" % (self.pk, getattr(self, self.USERNAME_FIELD, None),)


signals_logger = logging.getLogger("signals")

signals_logger.info("Logging signals from %s", __name__)


def compare_user_create_user_repository(sender, instance, action, reverse, pk_set, **kwargs):
    """
    """
    
    if not reverse and action == "post_add":
        from compareobject.models import CompareObjectType
        from comparelist.models import CompareList
        for pk in pk_set:
            object_type = CompareObjectType.objects.get(pk=pk)
            # TODO: This works for now but get_repository has to be changed
            if instance.get_repository(object_type) is None:
                try:
                    repository_list = CompareList.objects.get(repository_owner=instance, object_type=object_type)
                except CompareList.DoesNotExist:
                    repository_list = CompareList.objects.create(name="%s_repository" % (object_type.name), object_type=object_type)
                    repository_list.save()
                    
                instance.repositories.add(repository_list)
                
                signals_logger.debug("Added '%s' repository for %s", object_type, instance)


def compare_user_create_user_main_repository(sender, instance, raw, **kwargs):
    """
    Receiver for post_save CompareUser signal.
    Adds user main repository to database.
    """
    
    if not raw:
        from comparelist.models import CompareList
        CompareList.objects.create(repository_owner=instance, name="repository_%s" % (instance.slug,), object_type=None)


def compare_user_set_allowed_objct_types(sender, instance, raw, **kwargs):
    """
    Receiver for post_save CompareUser signal.
    Adds default allowed_compare_objects to user.
    Works only when user has no allowed_compare_objects.
    """
    
    if not raw and not instance.allowed_object_types.all():
        from compareobject.models import CompareObjectType
        allowed_types = CompareObjectType.objects.default_object_types().all()
        instance.allowed_object_types = allowed_types
        
        signals_logger.debug("Added allowed types %s for %s", allowed_types, instance)
        
        
m2m_changed.connect(compare_user_create_user_repository, sender=CompareUser.allowed_object_types.through)
post_save.connect(compare_user_create_user_main_repository, sender=CompareUser)
post_save.connect(compare_user_set_allowed_objct_types, sender=CompareUser)
