from django.db import models
from django.db.models import Q
from django.conf import settings


class CompareObjectType(models.Model):
    """
    """
    
    name = models.CharField(max_length=30, unique=True)
    features = models.ManyToManyField("comparelist.CompareFeature")
    
    def __unicode__(self):
        return self.name
    
    
class CompareCategory(models.Model):
    """
    """
    
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("name", "creator",)
    
    def get_user_categories(self, user):
        """
        """
        
        return self.objects.filter(Q(user=user) | Q(user=None))
    
    def __unicode__(self):
        return self.name


class CompareObject(models.Model):
    """
    """
    
    object_type = models.ForeignKey("compareobject.CompareObjectType", related_name="compare_objects")
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    categories = models.ManyToManyField("compareobject.CompareCategory", related_name="compare_objects")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.name
    
    
class Comparision(models.Model):
    """
    """
    
    comparer = models.ForeignKey(settings.AUTH_USER_MODEL)
    compare_list = models.ForeignKey("comparelist.CompareList")
    compare_feature = models.ForeignKey("comparelist.CompareFeature", null=True, default=None)
    compare_object_better = models.ForeignKey("compareobject.CompareObject", related_name="comparisions_better")
    compare_object_worse = models.ForeignKey("compareobject.CompareObject", related_name="comparisions_worse")
    is_equal = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    class Meta:
        unique_together = ("comparer", "compare_list", "compare_feature", "compare_object_better", "compare_object_worse")
    