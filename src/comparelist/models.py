from django.db import models
from django.conf import settings
from autoslug import AutoSlugField

from django.core.urlresolvers import reverse

from compareobject.models import Comparision
from comparelist.managers import CompareFeatureManager, CompareListManager, CompareViewManager
from comparelist.utils import feature_slug_populate_from, feature_slugify, list_slug_populate_from, list_slugify, view_slug_populate_from, view_slugify


class CompareFeature(models.Model):
    """
    """
    
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    slug = AutoSlugField(populate_from=feature_slug_populate_from, slugify=feature_slugify)
    
    objects = CompareFeatureManager()
    
    class Meta:
        unique_together = ("user", "name",)
        
    def natural_key(self):
        
        return (self.slug,)
        
    def __unicode__(self):
        return self.name


class CompareList(models.Model):
    """
    """
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, related_name="owned_lists")
    repository_owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, related_name="repositories")
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=list_slug_populate_from, slugify=list_slugify)
    object_type = models.ForeignKey("compareobject.CompareObjectType", blank=True, related_name="compare_lists")
    categories = models.ManyToManyField("compareobject.CompareCategory", blank=True, related_name="compare_lists")
    features = models.ManyToManyField("comparelist.CompareFeature", blank=True, related_name="compare_list")
    list_objects = models.ManyToManyField("compareobject.CompareObject", blank=True, related_name="compare_lists")
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    private = models.BooleanField(default=True)
    
    objects = CompareListManager()
    
    class Meta:
        unique_together = [
            ["owner", "repository_owner", "name"],
        ]
        index_together = [
            ["owner", "object_type"],
            ["owner", "private"],
            ["repository_owner", "object_type"],
        ]
        
    def natural_key(self):
        
        return (self.slug,)
    
    def get_absolute_url(self):
        
        return reverse("show-list-view", args=[self.id])
        
    def get_owner(self):
        
        return self.owner or self.repository_owner
        
    def is_private(self):
        
        return self.is_private
    
    def get_features(self):
        """
        returns features available for this list.
        Has object_type default features and custom features.
        """
        
        return self.object_type.features & self.features
    
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
    
    def is_global_repository(self):
        
        return not self.owner and not self.repository_owner
    
    def is_repository(self):
        
        return self.repository_owner is not None
    
    def get_list_objects(self):
        
        if self.is_repository():
            return self.list_objects.all()
        else:
            return self.list_objects.all()
    
    def __unicode__(self):
        return self.name


class CompareView(models.Model):
    """
    """
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owned_views")
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=view_slug_populate_from, slugify=view_slugify)
    compare_list = models.ForeignKey("comparelist.CompareList", related_name="compare_views")
    included_categories = models.ManyToManyField("compareobject.CompareCategory", related_name="included_views")
    excluded_categories = models.ManyToManyField("compareobject.CompareCategory", related_name="excluded_views")
    features = models.ManyToManyField("comparelist.CompareFeature", related_name="compare_views")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    private = models.BooleanField(default=True)
    
    objects = CompareViewManager()
    
    class Meta:
        unique_together = ("owner", "name",)
        
    def natural_key(self):
        
        return (self.slug,)
    
    def get_absolute_url(self):
        
        return reverse("show-listview-view", args=[self.id])
    
    def is_private(self):
        
        return self.is_private or self.compare_list.private
        