from django import template


register = template.Library()


@register.inclusion_tag('tags/youtube_object.html')
def show_youtube_element(element):
    
    return {"id": element.id, "name": element.name, "url": element.url, "embed_url": element.embed_url}
