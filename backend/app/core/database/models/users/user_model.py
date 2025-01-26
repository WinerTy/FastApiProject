from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from typing import TYPE_CHECKING

from core.database import BaseModel
from core.database.mixins import IntegerPkMixin
from core.types import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class UserModel(
    BaseModel,
    IntegerPkMixin,
    SQLAlchemyBaseUserTable[UserIdType],
):

    @classmethod
    def get_user_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, UserModel)
