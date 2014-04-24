from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.filter
def repository_url(repository_type):
    
    return reverse(repository_type.index_view)
