from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Role2(str, Enum):
    """DEPRECATED. Use ``assignedRoles`` instead. Role of the invited user in the organization. For organizations that
    have migrated to custom roles, this field is frozen at the pre-migration value and does not reflect the role
    assignment that will be applied."""

    ADMIN = "admin"
    DEVELOPER = "developer"

    __str__ = str.__str__


Role2OrStr: TypeAlias = Annotated[Role2 | str, open_enum_validator(Role2)]
