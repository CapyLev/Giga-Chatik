from datetime import datetime
from sqlalchemy import TIMESTAMP, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


class UserServer(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.id", ondelete="SET NULL"), index=True
    )
    server_id: Mapped[UUID] = mapped_column(
        ForeignKey("server.id", ondelete="SET NULL")
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now())

    user: Mapped["User"] = relationship(back_populates="user_servers")
    server: Mapped["Server"] = relationship(back_populates="user_servers")
