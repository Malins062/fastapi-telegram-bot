from typing import TypeVar

from pydantic import BaseModel

StrType = TypeVar("StrType", str, None)


class User(BaseModel):
    """
    Mongo model table for user
    """

    id: int
    full_name: StrType

    class ConfigDict:
        table_name = "users"
        from_attributes = True
