import logging

from django.conf import settings


logger = logging.getLogger(__name__)


class DisableDebugSiteMiddleware:
    """
    """
    
    def process_request(self, request):
        
        if settings.DEBUG:
            pass
        
        return None
