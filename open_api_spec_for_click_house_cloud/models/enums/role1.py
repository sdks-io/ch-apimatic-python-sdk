from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Role1(str, Enum):
    """DEPRECATED. Use ``assignedRoles`` instead. Role of the member in the organization. For organizations that have
    migrated to custom roles, this field is frozen at the pre-migration value and does not reflect current role
    assignments."""

    ADMIN = "admin"
    DEVELOPER = "developer"

    __str__ = str.__str__


Role1OrStr: TypeAlias = Annotated[Role1 | str, open_enum_validator(Role1)]
