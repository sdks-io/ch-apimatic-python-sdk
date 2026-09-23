from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Authentication8(str, Enum):
    """Authentication method. IAM_USER is for S3, GCS, and DigitalOcean Spaces. IAM_ROLE is for S3 only. SERVICE_ACCOUNT
    is for GCS only. For GCS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service
    account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet;
    grant it access to the source resources. CONNECTION_STRING is for Azure Blob Storage. PUBLIC uses no
    authentication."""

    IAM_ROLE = "IAM_ROLE"
    IAM_USER = "IAM_USER"
    CONNECTION_STRING = "CONNECTION_STRING"
    SERVICE_ACCOUNT = "SERVICE_ACCOUNT"
    SERVICE_ACCOUNT_WORKLOAD_IDENTITY = "SERVICE_ACCOUNT_WORKLOAD_IDENTITY"

    __str__ = str.__str__


Authentication8OrStr: TypeAlias = Annotated[Authentication8 | str, open_enum_validator(Authentication8)]
