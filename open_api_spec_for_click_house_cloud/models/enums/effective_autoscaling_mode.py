from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EffectiveAutoscalingMode(str, Enum):
    """Autoscaling mode currently in effect on the running service. May diverge from the configured baseline mode while
    a schedule entry is active."""

    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

    __str__ = str.__str__


EffectiveAutoscalingModeOrStr: TypeAlias = Annotated[
    EffectiveAutoscalingMode | str, open_enum_validator(EffectiveAutoscalingMode)
]
