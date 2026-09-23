from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReplicationMode(str, Enum):
    """Replication mode: "cdc" (change data capture with initial snapshot), "snapshot" (one-time snapshot only), or
    "cdc_only" (CDC without initial snapshot)."""

    CDC = "cdc"
    SNAPSHOT = "snapshot"
    CDC_ONLY = "cdc_only"

    __str__ = str.__str__


ReplicationModeOrStr: TypeAlias = Annotated[ReplicationMode | str, open_enum_validator(ReplicationMode)]
