from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Role7(str, Enum):
    """DEPRECATED. Use ``assignedRoleIds`` instead. Role of the member in the organization."""

    ADMIN = "admin"
    DEVELOPER = "developer"

    __str__ = str.__str__


Role7OrStr: TypeAlias = Annotated[Role7 | str, open_enum_validator(Role7)]
