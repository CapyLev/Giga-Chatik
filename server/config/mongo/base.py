from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    created_at: datetime = datetime.utcnow()
