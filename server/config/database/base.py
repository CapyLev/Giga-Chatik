from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from .mixins import BaseRepositoryMixin


class Base(DeclarativeBase, BaseRepositoryMixin):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"

    id: Mapped[int] = mapped_column(primary_key=True)
