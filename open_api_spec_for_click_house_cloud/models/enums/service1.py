from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Service1(str, Enum):
    """Webhook service type."""

    SLACK = "slack"
    INCIDENTIO = "incidentio"
    GENERIC = "generic"

    __str__ = str.__str__


Service1OrStr: TypeAlias = Annotated[Service1 | str, open_enum_validator(Service1)]
