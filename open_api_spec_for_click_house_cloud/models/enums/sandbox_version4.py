from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SandboxVersion4(str, Enum):
    """Sandbox runtime version."""

    V1 = "v1"
    V2 = "v2"
    V3 = "v3"

    __str__ = str.__str__


SandboxVersion4OrStr: TypeAlias = Annotated[SandboxVersion4 | str, open_enum_validator(SandboxVersion4)]
