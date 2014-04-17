from itertools import groupby

from django.conf import settings

from comparemessages.models import Message


def get_messages(messages):
    
    db_messages = Message.objects.filter(name__in=messages)
    if settings.DEBUG:
        db_messages = db_messages.exclude(type__in=Message.DEBUG_TYPES)
    db_messages = db_messages.order_by("type")
    
    return groupby(db_messages, lambda m: m.type)