from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OwnerType(str, Enum):
    """Owner type of the Query API endpoint. Endpoints with a user owned query cannot be updated or deleted through this
    API."""

    USER = "user"
    QUERY_API_ENDPOINT = "queryApiEndpoint"

    __str__ = str.__str__


OwnerTypeOrStr: TypeAlias = Annotated[OwnerType | str, open_enum_validator(OwnerType)]
