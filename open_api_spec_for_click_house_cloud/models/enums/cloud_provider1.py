from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CloudProvider1(str, Enum):
    """Cloud provider in which the private endpoint is lcoated"""

    GCP = "gcp"
    AWS = "aws"
    AZURE = "azure"

    __str__ = str.__str__


CloudProvider1OrStr: TypeAlias = Annotated[CloudProvider1 | str, open_enum_validator(CloudProvider1)]
