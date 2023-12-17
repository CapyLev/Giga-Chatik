from datetime import datetime
from typing import List
from bson import ObjectId

from config.mongo import Base


class Message(Base):
    _id: ObjectId
    user_id: str
    server_id: str
    content: str
    timestamp: datetime = datetime.utcnow()
    id_deleted: bool = False
    attachments: List[str] = []
