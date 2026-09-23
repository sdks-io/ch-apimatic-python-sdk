from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ActorType(str, Enum):
    """Type of the actor: 'user', 'support', 'system', 'api'."""

    USER = "user"
    SUPPORT = "support"
    SYSTEM = "system"
    API = "api"

    __str__ = str.__str__


ActorTypeOrStr: TypeAlias = Annotated[ActorType | str, open_enum_validator(ActorType)]
