from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Role(str, Enum):
    SQL_CONSOLE_READ_ONLY = "sql_console_read_only"
    SQL_CONSOLE_ADMIN = "sql_console_admin"

    __str__ = str.__str__


RoleOrStr: TypeAlias = Annotated[Role | str, open_enum_validator(Role)]
