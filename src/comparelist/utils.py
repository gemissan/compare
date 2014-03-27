from compareutils import slugify

def feature_slug_populate_from(instance):
    
    if instance.user:
        return (instance.user.slug, instance.name,)
    else:
        return (instance.name,)
   
    
def feature_slugify(value):

    return slugify(value)


def list_slug_populate_from(instance):
    
    if instance.is_global_repository():
        return (instance.name,)
    else:
        if instance.is_repository():
            user_slug = instance.repository_owner
        else:
            user_slug = instance.owner.slug
    
    return (user_slug, instance.name)


def list_slugify(value):
    
    return slugify(value)


def view_slug_populate_from(instance):
    
    if instance.user:
        return (instance.owner.slug, instance.name,)
    else:
        return (instance.name,)
   
    
def view_slugify(value):

    return slugify(value)
