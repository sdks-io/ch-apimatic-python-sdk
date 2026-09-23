from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoscalingMode3(str, Enum):
    """Configured autoscaling mode. "vertical" runs a fixed replica count while memory scales between minReplicaMemoryGb
    and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas at a fixed
    per-replica memory. This is the baseline configuration; the mode currently applied (which may differ while a
    schedule entry is active) is currentScaling.effectiveAutoscalingMode."""

    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

    __str__ = str.__str__


AutoscalingMode3OrStr: TypeAlias = Annotated[AutoscalingMode3 | str, open_enum_validator(AutoscalingMode3)]
