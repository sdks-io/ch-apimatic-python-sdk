from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.authentication8 import Authentication8OrStr
from .msk_iam_user import MskIamUser, MskIamUserDict


class ClickPipePatchObjectStorageSource(SdkBaseModel):
    skip_initial_load: OptionalNullable[bool] = Field(default=UNSET, alias="skipInitialLoad")
    """If set to true, skips the initial load and only ingests files delivered by queue notifications. Only applicable
    when queueUrl is provided."""

    start_after: OptionalNullable[str] = Field(default=UNSET, alias="startAfter")
    """Skip all files up to and including this object key during the initial load. Cannot be provided when
    skipInitialLoad is true."""

    authentication: OptionalNullable[Authentication8OrStr] = UNSET
    """Authentication method. IAM_USER is for S3, GCS, and DigitalOcean Spaces. IAM_ROLE is for S3 only. SERVICE_ACCOUNT
    is for GCS only. For GCS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service
    account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet;
    grant it access to the source resources. CONNECTION_STRING is for Azure Blob Storage. PUBLIC uses no
    authentication."""

    iam_role: OptionalNullable[str] = Field(default=UNSET, alias="iamRole")
    """IAM role to be used with IAM role authentication. Read more in ClickPipes documentation:
    https://clickhouse.com/docs/en/integrations/clickpipes/object-storage#authentication"""

    connection_string: OptionalNullable[str] = Field(default=UNSET, alias="connectionString")
    """Connection string for Azure Blob Storage authentication. Required when authentication is CONNECTION_STRING."""

    path: OptionalNullable[str] = UNSET
    """Path to the file(s) within the Azure container. Used for Azure Blob Storage sources. You can specify multiple
    files using bash-like wildcards. For more information, see the documentation on using wildcards in path:
    https://clickhouse.com/docs/en/integrations/clickpipes/object-storage#limitations"""

    azure_container_name: OptionalNullable[str] = Field(default=UNSET, alias="azureContainerName")
    """Container name for Azure Blob Storage. Required when type is azureblobstorage."""

    access_key: OptionalNullable[MskIamUser] = Field(default=UNSET, alias="accessKey")
    service_account_key: OptionalNullable[str] = Field(default=UNSET, alias="serviceAccountKey")
    """Base64-encoded GCP service account JSON key. Required when authentication is SERVICE_ACCOUNT."""


class ClickPipePatchObjectStorageSourceDict(TypedDict):
    skip_initial_load: NotRequired[bool | None]
    start_after: NotRequired[str | None]
    authentication: NotRequired[Authentication8OrStr | None]
    iam_role: NotRequired[str | None]
    connection_string: NotRequired[str | None]
    path: NotRequired[str | None]
    azure_container_name: NotRequired[str | None]
    access_key: NotRequired[MskIamUserDict | None]
    service_account_key: NotRequired[str | None]
