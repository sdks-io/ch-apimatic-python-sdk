from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Code(str, Enum):
    """Reason the attachment could not be started."""

    SERVICE_IDLE = "SERVICE_IDLE"
    SERVICE_NOT_RUNNING = "SERVICE_NOT_RUNNING"
    SERVICE_STOPPED = "SERVICE_STOPPED"

    __str__ = str.__str__


CodeOrStr: TypeAlias = Annotated[Code | str, open_enum_validator(Code)]
