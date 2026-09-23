from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Runtime(str, Enum):
    PYTHON3_11 = "python3.11"
    NATIVE = "native"

    __str__ = str.__str__


RuntimeOrStr: TypeAlias = Annotated[Runtime | str, open_enum_validator(Runtime)]
