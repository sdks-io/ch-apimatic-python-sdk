from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BucketProvider(str, Enum):
    """Bucket provider"""

    AWS = "AWS"

    __str__ = str.__str__


BucketProviderOrStr: TypeAlias = Annotated[BucketProvider | str, open_enum_validator(BucketProvider)]
