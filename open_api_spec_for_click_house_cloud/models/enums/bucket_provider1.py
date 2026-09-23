from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BucketProvider1(str, Enum):
    """Bucket provider"""

    GCP = "GCP"

    __str__ = str.__str__


BucketProvider1OrStr: TypeAlias = Annotated[BucketProvider1 | str, open_enum_validator(BucketProvider1)]
