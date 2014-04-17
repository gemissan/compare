import logging

from comparemessages import SessionMessageDict


logger = logging.getLogger(__name__)


class CompareMessageMiddleware():
    
    def process_request(self, request):
        
        setattr(request, "messages", SessionMessageDict(request.session))
