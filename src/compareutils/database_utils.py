import logging


logger = logging.getLogger(__name__)


def create_object(model, *args, **kwargs):
    """
    """
    
    logger.debug("create_object args (%s) kwargs (%s)" % (args, kwargs,))
    
    obj, created = model.objects.get_or_create(**kwargs)
    
    logger.debug("create_object %s %s" % ("created" if created else "fetched", obj,))
    
    return obj
    

def create_objects(model, *args, **kwargs):
    """
    """
    
    return [create_object(model, **args_list) for args_list in args]
