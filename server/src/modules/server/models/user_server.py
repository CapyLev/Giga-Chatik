from datetime import datetime

from sqlalchemy import TIMESTAMP, UUID, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


class UserServer(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.id", ondelete="SET NULL"), index=True
    )
    server_id: Mapped[UUID] = mapped_column(ForeignKey("server.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now())

    user: Mapped["User"] = relationship(back_populates="user_servers")
    server: Mapped["Server"] = relationship(back_populates="user_servers")

    __table_args__ = (UniqueConstraint("user_id", "server_id", name="_user_server_uc"),)
