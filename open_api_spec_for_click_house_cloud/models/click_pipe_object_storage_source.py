from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.authentication8 import Authentication8OrStr
from .enums.compression import CompressionOrStr
from .enums.format4 import Format4OrStr
from .enums.type5 import Type5OrStr


class ClickPipeObjectStorageSource(SdkBaseModel):
    type_: Optional[Type5OrStr] = Field(default=UNSET, alias="type")
    """Type of the ObjectStorage source."""

    format: Optional[Format4OrStr] = UNSET
    """Format of the files."""

    url: Optional[str] = UNSET
    """Provide a path to the file(s) you want to ingest. You can specify multiple files using bash-like wildcards. For
    more information, see the documentation on using wildcards in path:
    https://clickhouse.com/docs/en/integrations/clickpipes/object-storage#limitations"""

    delimiter: OptionalNullable[str] = UNSET
    """Delimiter used in the files."""

    compression: OptionalNullable[CompressionOrStr] = UNSET
    """Compression algorithm used for the files."""

    is_continuous: OptionalNullable[bool] = Field(default=UNSET, alias="isContinuous")
    """If set to true, the pipe will continuously read new files from the source. If set to false, the pipe will read
    the files only once. New files have to be uploaded lexically order."""

    queue_url: OptionalNullable[str] = Field(default=UNSET, alias="queueUrl")
    """Queue URL for event-based continuous ingestion. For S3, provide an SQS queue URL. For GCS, provide a Pub/Sub
    subscription (e.g. projects/{project}/subscriptions/{name}). When provided, files are ingested based on event
    notifications rather than lexicographical order. Only applicable when isContinuous is true and authentication is not
    public."""

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


class ClickPipeObjectStorageSourceDict(TypedDict):
    type_: NotRequired[Type5OrStr]
    format: NotRequired[Format4OrStr]
    url: NotRequired[str]
    delimiter: NotRequired[str | None]
    compression: NotRequired[CompressionOrStr | None]
    is_continuous: NotRequired[bool | None]
    queue_url: NotRequired[str | None]
    skip_initial_load: NotRequired[bool | None]
    start_after: NotRequired[str | None]
    authentication: NotRequired[Authentication8OrStr | None]
    iam_role: NotRequired[str | None]
    connection_string: NotRequired[str | None]
    path: NotRequired[str | None]
    azure_container_name: NotRequired[str | None]
