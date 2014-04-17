import logging
from itertools import groupby

from django.conf import settings

from comparemessages.models import Message


logger = logging.getLogger(__name__)


def get_messages(messages):
    
    db_messages = Message.objects.filter(name__in=messages)
    if settings.DEBUG:
        db_messages = db_messages.exclude(type__in=Message.DEBUG_TYPES)
    db_messages = db_messages.order_by("type")
    
    return groupby(db_messages, lambda m: m.type)


class MessageDict(object):
    
    _message_names = None
    _messages = None

    def __init__(self, debug_messages=None):
        self._debug_messages = debug_messages if debug_messages is not None else settings.DEBUG

    @property
    def messages(self):
        if self._messages is None:
            self._fetch_messages()
        return self._messages

    @property
    def message_names(self):
        if self._message_names is None:
            self._message_names = []
        return self._message_names

    def _fetch_messages(self):
        if self.message_names:
            db_messages = Message.objects.filter(name__in=self.message_names)
            if not self._debug_messages:
                db_messages = db_messages.exclude(type__in=Message.DEBUG_TYPES)
            db_messages = db_messages.order_by("type")
            self._messages = {k:list(v) for k, v in groupby(db_messages, lambda x: x.type)}
            logger.debug("fetched messages = %s" % self._messages)
        else:
            self._messages = {}
        
        self._message_names[:] = []

    def add(self, message_name):
        if message_name not in self.message_names:
            self.message_names.append(message_name)
            
    def __str__(self):
        lst_str = "Empty"
        if self._message_names is not None:
            lst_str = str(self._message_names)
        elif self._messages is not None:
            lst_str = str(self._messages)
        
        return "%s[%s]" % (self.__class__.__name__, lst_str,) 


class SessionMessageDict(MessageDict):

    def __init__(self, session, debug_messages=None):
        self._session = session
        super(SessionMessageDict, self).__init__(debug_messages)

    @property
    def message_names(self):
        if "message_names" not in self._session:
            self._session["message_names"] = []
        if self._message_names is None:
            self._message_names = self._session["message_names"]
        return self._message_names
