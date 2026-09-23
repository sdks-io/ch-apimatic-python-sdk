from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoscalingMode4(str, Enum):
    """Autoscaling mode. "vertical" (the default when omitted) runs a fixed replica count while memory scales between
    minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas
    at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb). Horizontal requires the feature to
    be enabled for the organization."""

    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

    __str__ = str.__str__


AutoscalingMode4OrStr: TypeAlias = Annotated[AutoscalingMode4 | str, open_enum_validator(AutoscalingMode4)]
