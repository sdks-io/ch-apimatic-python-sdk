from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SandboxVersion(str, Enum):
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"

    __str__ = str.__str__


SandboxVersionOrStr: TypeAlias = Annotated[SandboxVersion | str, open_enum_validator(SandboxVersion)]
