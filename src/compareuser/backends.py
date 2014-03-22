import logging

from django.contrib.auth import get_user_model


logger = logging.getLogger(__name__)
User = get_user_model()

class DummyAuthenticationBackend(object):
    """
    """
    
    def authenticate(self, name=None):
        """
        """
        
        logger.debug("Authenticate %s" % (name,))
        
        kwargs = {User.USERNAME_FIELD: name}
        
        authenticated_object = None
        try:
            authenticated_object = User.objects.get(**kwargs)
        except User.DoesNotExist:
            logger.warning("User with creditentials %s doesn't exist" % (kwargs,))
        except Exception as e:
            logger.error(unicode(e))
        else:
            logger.debug("%s authenticated as %s" % (name, authenticated_object,))
        
        return authenticated_object
    
    def get_user(self, username):
        """
        """
        
        logger.debug("get_user %s" % (username,))
        
        try:
            return User.objects.get(pk=username)
        except User.DoesNotExist:
            return None
