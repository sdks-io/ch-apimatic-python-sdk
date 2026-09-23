from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BucketProvider2(str, Enum):
    """Bucket provider"""

    AZURE = "AZURE"

    __str__ = str.__str__


BucketProvider2OrStr: TypeAlias = Annotated[BucketProvider2 | str, open_enum_validator(BucketProvider2)]
