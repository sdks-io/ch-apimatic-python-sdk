from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Authentication17(str, Enum):
    """Authentication method to use with GCP Pub/Sub. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview.
    ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId
    clickPipesServiceContextGet; grant it access to the source resources."""

    SERVICE_ACCOUNT = "SERVICE_ACCOUNT"
    SERVICE_ACCOUNT_WORKLOAD_IDENTITY = "SERVICE_ACCOUNT_WORKLOAD_IDENTITY"

    __str__ = str.__str__


Authentication17OrStr: TypeAlias = Annotated[Authentication17 | str, open_enum_validator(Authentication17)]
