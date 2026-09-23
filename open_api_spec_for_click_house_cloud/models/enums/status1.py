from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status1(str, Enum):
    """Status of the backup: 'done', 'error', 'in_progress'."""

    DONE = "done"
    ERROR = "error"
    IN_PROGRESS = "in_progress"

    __str__ = str.__str__


Status1OrStr: TypeAlias = Annotated[Status1 | str, open_enum_validator(Status1)]
