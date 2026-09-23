from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type9(str, Enum):
    """Type of the MySQL source. Defaults to "mysql" if not specified."""

    MYSQL = "mysql"
    RDSMYSQL = "rdsmysql"
    AURORAMYSQL = "auroramysql"
    MARIADB = "mariadb"
    RDSMARIADB = "rdsmariadb"

    __str__ = str.__str__


Type9OrStr: TypeAlias = Annotated[Type9 | str, open_enum_validator(Type9)]
