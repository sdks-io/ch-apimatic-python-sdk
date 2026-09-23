from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CloudProvider(str, Enum):
    """The cloud provider for a Postgres service."""

    AWS = "aws"
    GCP = "gcp"

    __str__ = str.__str__


CloudProviderOrStr: TypeAlias = Annotated[CloudProvider | str, open_enum_validator(CloudProvider)]
