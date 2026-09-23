from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SandboxType4(str, Enum):
    """Sandbox isolation level."""

    BASIC = "basic"
    NETENABLE = "netenable"

    __str__ = str.__str__


SandboxType4OrStr: TypeAlias = Annotated[SandboxType4 | str, open_enum_validator(SandboxType4)]
