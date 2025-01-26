from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)


from core.database import BaseModel
from core.types import UserIdType


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession  # noqa


class AccessToken(BaseModel, SQLAlchemyBaseAccessTokenTable[UserIdType]):

    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        ForeignKey("user_model.id", ondelete="CASCADE"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
