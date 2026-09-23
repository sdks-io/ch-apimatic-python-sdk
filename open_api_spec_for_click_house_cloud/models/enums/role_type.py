from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoleType(str, Enum):
    """Type of role: system (predefined) or custom (organization-defined)"""

    SYSTEM = "system"
    CUSTOM = "custom"

    __str__ = str.__str__


RoleTypeOrStr: TypeAlias = Annotated[RoleType | str, open_enum_validator(RoleType)]
