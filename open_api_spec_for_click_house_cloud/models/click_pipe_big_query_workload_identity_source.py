from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_big_query_pipe_settings import ClickPipeBigQueryPipeSettings, ClickPipeBigQueryPipeSettingsDict
from .click_pipe_big_query_pipe_table_mapping import (
    ClickPipeBigQueryPipeTableMapping,
    ClickPipeBigQueryPipeTableMappingDict,
)


class ClickPipeBigQueryWorkloadIdentitySource(SdkBaseModel):
    snapshot_staging_path: str = Field(alias="snapshotStagingPath")
    """GCS bucket path for staging snapshot data (e.g., gs://my-bucket/staging/). Data will be automatically cleaned up
    after initial load."""

    settings: ClickPipeBigQueryPipeSettings
    table_mappings: list[ClickPipeBigQueryPipeTableMapping] = Field(alias="tableMappings")
    """Table mappings for BigQuery pipe."""

    authentication: Literal["SERVICE_ACCOUNT_WORKLOAD_IDENTITY"] = "SERVICE_ACCOUNT_WORKLOAD_IDENTITY"
    """Authenticated with the ClickPipes service tenant identity. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private
    Preview. ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with
    operationId clickPipesServiceContextGet; grant it access to the source resources."""

    project_id: Optional[str] = Field(default=UNSET, alias="projectId")
    """GCP project ID that owns the BigQuery resources. Older pipes created outside OpenAPI may omit this field."""


class ClickPipeBigQueryWorkloadIdentitySourceDict(TypedDict):
    snapshot_staging_path: str
    settings: ClickPipeBigQueryPipeSettingsDict
    table_mappings: list[ClickPipeBigQueryPipeTableMappingDict]
    authentication: Literal["SERVICE_ACCOUNT_WORKLOAD_IDENTITY"]
    project_id: NotRequired[str]
