from typing import List, Optional

from pydantic import Field, BaseModel

from src.modules.auth.dto import UserShortDTO


class MessageDTO(BaseModel):
    id: str
    user: UserShortDTO
    server_id: str
    content: str
    timestamp: int
    id_deleted: bool = False
    attachments: List[Optional[str]] = Field(default_factory=list)
