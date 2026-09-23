from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State2(str, Enum):
    """Current lifecycle state of the ClickPipe. For database pipes: "Provisioning" (initial setup), "Setup"
    (configuring replication), "Snapshot" (initial data load), "Running" (actively replicating), "Pausing"
    (transitioning to paused state), "Paused" (temporarily paused), "Modifying" (applying configuration updates),
    "Resync" (swapping resync tables with original tables), "Failed" (error occurred), "Unknown". For streaming/object
    storage pipes (Kafka, Kinesis, S3): "Unknown" (initial state), "Provisioning" (setting up resources), "Running"
    (actively ingesting data), "Stopping" (transitioning to stopped state), "Stopped" (manually stopped, can be
    restarted), "Completed" (batch ingestion finished for object storage), "Failed" (error occurred, pipe stopped),
    "InternalError" (internal system error)."""

    UNKNOWN = "Unknown"
    PROVISIONING = "Provisioning"
    RUNNING = "Running"
    DEGRADED = "Degraded"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    FAILED = "Failed"
    COMPLETED = "Completed"
    INTERNAL_ERROR = "InternalError"
    SETUP = "Setup"
    SNAPSHOT = "Snapshot"
    PAUSED = "Paused"
    PAUSING = "Pausing"
    MODIFYING = "Modifying"
    RESYNC = "Resync"

    __str__ = str.__str__


State2OrStr: TypeAlias = Annotated[State2 | str, open_enum_validator(State2)]
