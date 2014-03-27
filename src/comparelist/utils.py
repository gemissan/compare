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
    
    return "_".join(value).lower().replace(" ", "_")
