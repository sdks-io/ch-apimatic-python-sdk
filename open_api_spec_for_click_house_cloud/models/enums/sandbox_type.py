from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SandboxType(str, Enum):
    BASIC = "basic"
    NETENABLE = "netenable"

    __str__ = str.__str__


SandboxTypeOrStr: TypeAlias = Annotated[SandboxType | str, open_enum_validator(SandboxType)]
