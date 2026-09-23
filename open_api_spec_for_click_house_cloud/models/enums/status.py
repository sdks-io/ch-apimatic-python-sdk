from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status(str, Enum):
    """Reverse private endpoint status."""

    UNKNOWN = "Unknown"
    PROVISIONING = "Provisioning"
    DELETING = "Deleting"
    READY = "Ready"
    FAILED = "Failed"
    PENDING_ACCEPTANCE = "PendingAcceptance"
    REJECTED = "Rejected"
    EXPIRED = "Expired"

    __str__ = str.__str__


StatusOrStr: TypeAlias = Annotated[Status | str, open_enum_validator(Status)]
