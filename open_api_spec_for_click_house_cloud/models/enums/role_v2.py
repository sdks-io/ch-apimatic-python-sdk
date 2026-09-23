from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoleV2(str, Enum):
    """Optional SQL console role type"""

    SQL_CONSOLE_READONLY = "sql-console-readonly"
    SQL_CONSOLE_ADMIN = "sql-console-admin"

    __str__ = str.__str__


RoleV2OrStr: TypeAlias = Annotated[RoleV2 | str, open_enum_validator(RoleV2)]
