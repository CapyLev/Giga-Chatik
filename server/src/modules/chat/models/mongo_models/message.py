from datetime import datetime
from typing import List
from bson import ObjectId

from config.mongo.base import Base


class Message(Base):
    _id: ObjectId
    user_id: ObjectId
    content: str  # TODO: implement multiple uploading content, Union[str[msg], list[file]]


class MessageStorage(Base):
    _id: ObjectId
    messages: List[Message]
