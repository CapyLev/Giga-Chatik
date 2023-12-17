from typing import Optional
from fastapi_users_db_sqlalchemy import UUID_ID
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from config.database import Base


class UserProfile(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[Optional[UUID_ID]] = mapped_column(
        ForeignKey("user.id", ondelete="SET NULL"),
        index=True,
    )
    status: Mapped[Optional[str]] = mapped_column(String(length=250), nullable=True)
