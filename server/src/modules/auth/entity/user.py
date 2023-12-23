from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True, slots=True)
class UserEntity:
    id: str
    username: str
    email: str
    created_at: datetime
