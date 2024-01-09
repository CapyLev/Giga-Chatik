from datetime import datetime

from mongoengine import (
    StringField,
    DateTimeField,
    BooleanField,
    ListField,
    UUIDField,
    URLField,
)
from config.mongo import BaseDocument


class MessageDocument(BaseDocument):
    user_id = UUIDField(verbose_name="User uuid", binary=True, required=True)
    server_id = UUIDField(verbose_name="Server uuid", binary=True, required=True)
    content = StringField(verbose_name="Message content", required=True)
    timestamp = DateTimeField(
        verbose_name="Timestamp", default=datetime.now, required=True
    )
    id_deleted = BooleanField(verbose_name="Message is deleted", default=False)
    attachments = ListField(URLField(verbose_name="Images/Audio/... urls"))

    meta = {
        "indexes": [
            {"fields": ["chat_id", "timestamp"]},
            {"fields": ["chat_id", "user_id"]},
        ]
    }
