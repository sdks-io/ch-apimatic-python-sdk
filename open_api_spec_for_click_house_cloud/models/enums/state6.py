from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State6(str, Enum):
    """Initial state of the key: 'enabled', 'disabled'. If not provided the new key will be 'enabled'."""

    ENABLED = "enabled"
    DISABLED = "disabled"

    __str__ = str.__str__


State6OrStr: TypeAlias = Annotated[State6 | str, open_enum_validator(State6)]
