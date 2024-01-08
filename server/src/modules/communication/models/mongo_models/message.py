from datetime import datetime

from mongoengine import (
    StringField,
    DateTimeField,
    BooleanField,
    ListField,
    ObjectIdField,
    UUIDField,
    URLField,
)
from config.mongo import BaseDocument


class MessageDocument(BaseDocument):
    _id = ObjectIdField()
    user_id = UUIDField(required=True, binary=True)
    server_id = UUIDField(required=True, binary=True)
    content = StringField(required=True)
    timestamp = DateTimeField(required=True, default=datetime.now())
    id_deleted = BooleanField(default=False)
    attachments = ListField(URLField())

    meta = {
        "indexes": [
            {"fields": ["chat_id", "timestamp"]},
            {"fields": ["chat_id", "user_id"]},
        ]
    }
