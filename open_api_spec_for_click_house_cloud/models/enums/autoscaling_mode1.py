from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoscalingMode1(str, Enum):
    """Autoscaling mode applied when no schedule entry is active. "vertical" runs a fixed replica count while memory
    scales; "horizontal" scales the replica count at a fixed per-replica memory."""

    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

    __str__ = str.__str__


AutoscalingMode1OrStr: TypeAlias = Annotated[AutoscalingMode1 | str, open_enum_validator(AutoscalingMode1)]
