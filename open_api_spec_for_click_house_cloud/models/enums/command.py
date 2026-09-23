from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Command(str, Enum):
    """Postgres status, which initiates a process."""

    RESTART = "restart"
    PROMOTE = "promote"
    SWITCHOVER = "switchover"

    __str__ = str.__str__


CommandOrStr: TypeAlias = Annotated[Command | str, open_enum_validator(Command)]
