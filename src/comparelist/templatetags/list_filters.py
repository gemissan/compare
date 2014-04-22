from django import template


register = template.Library()


@register.filter
def list_url(lst):
    
    return lst.get_absolute_url()


@register.filter
def repository_url(user, repository_type):
    
    return list_url(user.get_repository(repository_type))
