from django.db import models
from django.conf import settings

from compareobject.models import Comparision


class CompareFeature(models.Model):
    """
    """
    
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    
    class Meta:
        unique_together = ("name", "user",)
        
    def __unicode__(self):
        return self.name


class CompareList(models.Model):
    """
    """
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="owned_lists")
    name = models.CharField(max_length=255)
    object_type = models.ForeignKey("compareobject.CompareObjectType", null=True, default=None, related_name="compare_lists")
    categories = models.ManyToManyField("compareobject.CompareCategory", null=True, default=None, related_name="compare_lists")
    features = models.ManyToManyField("comparelist.CompareFeature", null=True, default=None, related_name="compare_list")
    list_objects = models.ManyToManyField("compareobject.CompareObject", null=True, default=None, related_name="compare_lists")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    is_private = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ("owner", "name",)
        
    @property
    def private(self):
        
        return self.is_private
    
    def get_better_objects(self, compare_object):
        """
        """
        
        comparisions = Comparision.objects.filter(
                compare_list=self,
                compare_object_worse=compare_object,
                compare_object_better__in=self.list_objects)
        
        return comparisions.compare_object_better
    
    def get_worse_comparisions(self, compare_object):
        """
        """
        
        comparisions = Comparision.objects.filter(
                compare_list=self,
                compare_object_better=compare_object,
                compare_object_worse__in=self.list_objects)
        
        return comparisions.compare_object_worse
    
    def get_all_comparisions(self, compare_object):
        """
        """
        
        better_comparisions = self.get_better_comparisions(compare_object)
        worse_comparisions = self.get_worse_comparisions(compare_object)
        
        return better_comparisions | worse_comparisions
    
    def is_repository(self):
        
        return self.owner is None and self.repository_owner is not None
    
    def __unicode__(self):
        return self.name


class CompareView(models.Model):
    """
    """
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owned_views")
    compare_list = models.ForeignKey("comparelist.CompareList", related_name="compare_views")
    included_categories = models.ManyToManyField("compareobject.CompareCategory", related_name="included_views")
    excluded_categories = models.ManyToManyField("compareobject.CompareCategory", related_name="excluded_views")
    features = models.ManyToManyField("comparelist.CompareFeature", related_name="compare_views")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    is_private = models.BooleanField(default=True)
    
    @property
    def private(self):
        
        return self.is_private and self.compare_list.private
    