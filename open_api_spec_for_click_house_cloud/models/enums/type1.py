from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type1(str, Enum):
    """Reverse private endpoint type."""

    VPC_ENDPOINT_SERVICE = "VPC_ENDPOINT_SERVICE"
    VPC_RESOURCE = "VPC_RESOURCE"
    MSK_MULTI_VPC = "MSK_MULTI_VPC"
    GCP_PSC_SERVICE_ATTACHMENT = "GCP_PSC_SERVICE_ATTACHMENT"

    __str__ = str.__str__


Type1OrStr: TypeAlias = Annotated[Type1 | str, open_enum_validator(Type1)]
