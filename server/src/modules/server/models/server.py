from datetime import datetime
from fastapi_users_db_sqlalchemy import UUID_ID
from sqlalchemy import TIMESTAMP, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


class Server(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=70), nullable=False)
    image: Mapped[str] = mapped_column(String(length=500))
    is_public: Mapped[bool] = mapped_column(default=False, index=True)
    password: Mapped[str] = mapped_column(String(length=250), nullable=True)
    admin_id: Mapped[UUID_ID] = mapped_column(
        ForeignKey("user.id", ondelete="SET NULL"),
        index=True,
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow())

    admin: Mapped[UUID_ID] = relationship(
        "User", back_populates="server", uselist=False
    )
