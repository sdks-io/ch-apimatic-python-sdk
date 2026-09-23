from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Command2(str, Enum):
    """Command to change the state: 'start', 'stop', 'resync'."""

    START = "start"
    STOP = "stop"
    RESYNC = "resync"

    __str__ = str.__str__


Command2OrStr: TypeAlias = Annotated[Command2 | str, open_enum_validator(Command2)]
