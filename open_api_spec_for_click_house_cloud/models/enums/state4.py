from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State4(str, Enum):
    """State of the key: 'enabled', 'disabled'."""

    ENABLED = "enabled"
    DISABLED = "disabled"

    __str__ = str.__str__


State4OrStr: TypeAlias = Annotated[State4 | str, open_enum_validator(State4)]
