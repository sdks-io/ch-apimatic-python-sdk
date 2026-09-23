from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MskAuthentication(str, Enum):
    """MSK cluster authentication type. Required for MSK_MULTI_VPC type."""

    SASL_IAM = "SASL_IAM"
    SASL_SCRAM = "SASL_SCRAM"

    __str__ = str.__str__


MskAuthenticationOrStr: TypeAlias = Annotated[MskAuthentication | str, open_enum_validator(MskAuthentication)]
