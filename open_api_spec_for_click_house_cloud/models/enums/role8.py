from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Role8(str, Enum):
    """DEPRECATED. Use ``assignedRoleIds`` instead. Role to assign to the invited user in the organization."""

    ADMIN = "admin"
    DEVELOPER = "developer"

    __str__ = str.__str__


Role8OrStr: TypeAlias = Annotated[Role8 | str, open_enum_validator(Role8)]
