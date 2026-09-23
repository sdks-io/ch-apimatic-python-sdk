from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State1(str, Enum):
    """State of the infrastructure"""

    INFRA_READY = "infra-ready"
    INFRA_PROVISIONING = "infra-provisioning"
    INFRA_TERMINATED = "infra-terminated"

    __str__ = str.__str__


State1OrStr: TypeAlias = Annotated[State1 | str, open_enum_validator(State1)]
