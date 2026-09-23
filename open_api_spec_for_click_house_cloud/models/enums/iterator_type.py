from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IteratorType(str, Enum):
    """Type of iterator to use when reading from the Kinesis stream. If AT_TIMESTAMP is used, the timestamp field must
    be provided."""

    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"

    __str__ = str.__str__


IteratorTypeOrStr: TypeAlias = Annotated[IteratorType | str, open_enum_validator(IteratorType)]
