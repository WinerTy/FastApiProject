from core.database.base import BaseModel

from sqlalchemy.orm import mapped_column, Mapped

from core.database.mixins import IntegerPkMixin


class TagModel(BaseModel, IntegerPkMixin):
    name: Mapped[str] = mapped_column(unique=True)
