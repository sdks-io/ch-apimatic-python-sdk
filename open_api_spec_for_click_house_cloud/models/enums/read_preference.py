from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReadPreference(str, Enum):
    """MongoDB read preference for replica set reads."""

    PRIMARY = "primary"
    PRIMARY_PREFERRED = "primaryPreferred"
    SECONDARY = "secondary"
    SECONDARY_PREFERRED = "secondaryPreferred"
    NEAREST = "nearest"

    __str__ = str.__str__


ReadPreferenceOrStr: TypeAlias = Annotated[ReadPreference | str, open_enum_validator(ReadPreference)]
