from datetime import datetime
from typing import Optional
import uuid

from fastapi_users_db_sqlalchemy import UUID_ID, SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.generics import GUID
from sqlalchemy import TIMESTAMP, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    id: Mapped[UUID_ID] = mapped_column(GUID, primary_key=True, default=uuid.uuid4)

    username: Mapped[str] = mapped_column(String(length=120), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(
        String(length=320), unique=True, index=True, nullable=True
    )

    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow())