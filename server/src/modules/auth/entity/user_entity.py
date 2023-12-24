from datetime import datetime
from pydantic.dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UserEntity:
    id: str
    username: str
    email: str
    created_at: datetime
