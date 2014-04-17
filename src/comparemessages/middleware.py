import logging

from comparemessages import SessionMessageDict


logger = logging.getLogger("middleware")


class CompareMessageMiddleware():
    
    def process_view(self, request, *args, **kwargs):
        
        setattr(request, "compare_messages", SessionMessageDict(request.session))
