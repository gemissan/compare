import logging


logger = logging.getLogger("signals")

logger.info("Logging signals on %s", __name__)


def compare_category_set_category_type(sender, instance, raw, **kwargs):
    
    if not raw:
        logger.debug("Set category type to '%s' for %s", instance.default_category_type, instance)
        instance.category_type = sender.default_category_type
