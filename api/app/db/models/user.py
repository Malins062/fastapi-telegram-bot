from pydantic import BaseModel
from typing import TypeVar

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
