from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CloudProvider2(str, Enum):
    """Cloud provider of the region"""

    GCP = "gcp"
    AWS = "aws"
    AZURE = "azure"

    __str__ = str.__str__


CloudProvider2OrStr: TypeAlias = Annotated[CloudProvider2 | str, open_enum_validator(CloudProvider2)]
