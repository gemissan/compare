from itertools import groupby

from django.conf import settings

from comparemessages.models import Message


def get_messages(messages):
    
    db_messages = Message.objects.filter(name__in=messages)
    if settings.DEBUG:
        db_messages = db_messages.exclude(type__in=Message.DEBUG_TYPES)
    db_messages = db_messages.order_by("type")
    
    return groupby(db_messages, lambda m: m.type)


class MessageDict(object):

    def __init__(self, debug_messages=None):
        self.clear()
        self._debug_messages = debug_messages if debug_messages is not None else settings.DEBUG

    @property
    def messages(self):
        if self._messages is None:
            self._fetch_messages()
        return self._messages

    @property
    def message_names(self):
        return self._message_names

    def _fetch_messages(self):
        if self.message_names:
            db_messages = Message.objects.filter(name__in=self.message_names)
            if self._debug_messages:
                db_messages = db_messages.exclude(type__in=Message.DEBUG_TYPES)
            db_messages = db_messages.order_by("type")
            self._messages = {k:list(v) for k, v in db_messages}
        else:
            self._messages = {}
        self._clear_message_names()

    def add(self, message_name):
        if message_name not in self.message_names:
            self.message_names.append(message_name)

    def _clear_message_names(self):
        self._message_names = []

    def _clear_messages(self):
        self._messages = None

    def clear(self):
        self._clear_message_names()
        self._clear_messages()


class SessionMessageDict(MessageDict):

    def __init__(self, session, debug_messages=None):
        self._session = session
        super(SessionMessageDict, self).__init__(debug_messages)

    @property
    def message_names(self):
        if "message_names" not in self._session:
            self._clear_message_names()
        return self._session["message_names"]

    @message_names.setter
    def message_names(self, value):
        self._session["message_names"] = value

    def _clear_message_names(self):
        self.message_names = []
