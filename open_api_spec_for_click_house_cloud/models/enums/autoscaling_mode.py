from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoscalingMode(str, Enum):
    """Autoscaling mode for this entry. "vertical" runs a fixed replica count while memory scales; "horizontal" scales
    the replica count at a fixed per-replica memory. Defaults to "vertical" for entries persisted before the mode was
    exposed."""

    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

    __str__ = str.__str__


AutoscalingModeOrStr: TypeAlias = Annotated[AutoscalingMode | str, open_enum_validator(AutoscalingMode)]
