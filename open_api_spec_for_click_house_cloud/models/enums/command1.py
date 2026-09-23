from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Command1(str, Enum):
    """Command to change the state: 'start', 'stop', 'awake'."""

    START = "start"
    STOP = "stop"
    AWAKE = "awake"

    __str__ = str.__str__


Command1OrStr: TypeAlias = Annotated[Command1 | str, open_enum_validator(Command1)]
