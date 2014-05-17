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
        
        kwargs = {User.USERNAME_FIELD: name}
        
        authenticated_object = None
        try:
            authenticated_object = User.objects.get(**kwargs)
        except User.DoesNotExist:
            logger.warning("User with creditentials %s doesn't exist" % (kwargs,))
        except Exception as e:
            logger.error(str(e))
        else:
            logger.debug("%s authenticated as %s" % (name, authenticated_object,))
        
        return authenticated_object
    
    def get_user(self, user_id):
        """
        """
        
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
