from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State(str, Enum):
    """Current state of the service."""

    STARTING = "starting"
    STOPPING = "stopping"
    TERMINATING = "terminating"
    SOFTDELETING = "softdeleting"
    AWAKING = "awaking"
    PARTIALLY_RUNNING = "partially_running"
    PROVISIONING = "provisioning"
    RUNNING = "running"
    STOPPED = "stopped"
    TERMINATED = "terminated"
    SOFTDELETED = "softdeleted"
    DEGRADED = "degraded"
    FAILED = "failed"
    IDLE = "idle"

    __str__ = str.__str__


StateOrStr: TypeAlias = Annotated[State | str, open_enum_validator(State)]
