from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type5(str, Enum):
    """Type of the ObjectStorage source."""

    S3 = "s3"
    GCS = "gcs"
    DOSPACES = "dospaces"
    AZUREBLOBSTORAGE = "azureblobstorage"
    CLOUDFLARER2 = "cloudflarer2"
    OVHOBJECTSTORAGE = "ovhobjectstorage"

    __str__ = str.__str__


Type5OrStr: TypeAlias = Annotated[Type5 | str, open_enum_validator(Type5)]
