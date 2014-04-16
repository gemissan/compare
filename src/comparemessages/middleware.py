import logging

from django.conf import settings


logger = logging.getLogger(__name__)


class ShowMessagesMiddleware:
    """
    """
    
    def process_response(self, request, response):
        
        response.content = response.content("generic message", "special message")
        
        return response
