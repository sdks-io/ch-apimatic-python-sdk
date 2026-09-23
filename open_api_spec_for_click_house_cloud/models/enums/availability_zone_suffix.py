from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AvailabilityZoneSuffix(str, Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"

    __str__ = str.__str__


AvailabilityZoneSuffixOrStr: TypeAlias = Annotated[
    AvailabilityZoneSuffix | str, open_enum_validator(AvailabilityZoneSuffix)
]
