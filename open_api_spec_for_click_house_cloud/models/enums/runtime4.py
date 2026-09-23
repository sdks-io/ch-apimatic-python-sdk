from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Runtime4(str, Enum):
    """Runtime used to execute the UDF command."""

    PYTHON3_11 = "python3.11"
    NATIVE = "native"

    __str__ = str.__str__


Runtime4OrStr: TypeAlias = Annotated[Runtime4 | str, open_enum_validator(Runtime4)]
