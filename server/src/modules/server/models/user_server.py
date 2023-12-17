from datetime import datetime
from typing import Optional
from fastapi_users_db_sqlalchemy import UUID_ID
from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


class UserServer(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[UUID_ID] = mapped_column(
        ForeignKey("user.id", ondelete="SET NULL"), index=True
    )
    server_id: Mapped[UUID_ID] = mapped_column(
        ForeignKey("server.id", ondelete="SET NULL")
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow())

    user = relationship("User", back_populates="user_servers")
    server = relationship("Server", back_populates="user_servers")
