from django import template


register = template.Library()


@register.filter
def repository_url(user, repository_type):
    
    return user.get_repository(repository_type).get_absolute_url()
