import uuid
from datetime import datetime
from typing import List

from sqlalchemy import TIMESTAMP, UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


class Server(Base):
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(length=70))
    image: Mapped[str] = mapped_column(String(length=500), nullable=True)
    is_public: Mapped[bool] = mapped_column(default=False, index=True)
    password: Mapped[str] = mapped_column(String(length=250), nullable=True)
    admin_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.id", ondelete="SET NULL"),
        index=True,
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now())

    admin: Mapped["User"] = relationship(
        back_populates="admined_servers", uselist=False
    )
    user_servers: Mapped[List["UserServer"]] = relationship(back_populates="server")
