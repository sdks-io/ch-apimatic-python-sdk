from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoscalingMode6(str, Enum):
    """Target autoscaling mode. Omit to keep the service on its current mode. "vertical" runs a fixed replica count
    while memory scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between
    minReplicas and maxReplicas at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb).
    Switching to horizontal requires the feature to be enabled for the organization."""

    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

    __str__ = str.__str__


AutoscalingMode6OrStr: TypeAlias = Annotated[AutoscalingMode6 | str, open_enum_validator(AutoscalingMode6)]
