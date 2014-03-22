from django.conf import settings


class DisableDebugSiteMiddleware():
    """
    """
    
    def process_view(self, request, callback, callback_args, callback_kwargs):
        
        if settings.DEBUG:
            pass
        
        return None
    
    def process_response(self, request, response):
        
        return response