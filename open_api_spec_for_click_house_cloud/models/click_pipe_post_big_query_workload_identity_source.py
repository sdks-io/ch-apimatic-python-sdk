from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .click_pipe_big_query_pipe_settings import ClickPipeBigQueryPipeSettings, ClickPipeBigQueryPipeSettingsDict
from .click_pipe_big_query_pipe_table_mapping import (
    ClickPipeBigQueryPipeTableMapping,
    ClickPipeBigQueryPipeTableMappingDict,
)


class ClickPipePostBigQueryWorkloadIdentitySource(SdkBaseModel):
    snapshot_staging_path: str = Field(alias="snapshotStagingPath")
    """GCS bucket path for staging snapshot data (e.g., gs://my-bucket/staging/). Data will be automatically cleaned up
    after initial load."""

    settings: ClickPipeBigQueryPipeSettings
    table_mappings: list[ClickPipeBigQueryPipeTableMapping] = Field(alias="tableMappings")
    """Table mappings for BigQuery pipe."""

    authentication: Literal["SERVICE_ACCOUNT_WORKLOAD_IDENTITY"] = "SERVICE_ACCOUNT_WORKLOAD_IDENTITY"
    """Authenticate with the ClickPipes service tenant identity. Customer credentials must not be provided.
    SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in
    gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the
    source resources."""

    project_id: str = Field(alias="projectId")
    """GCP project ID that owns the BigQuery resources."""


class ClickPipePostBigQueryWorkloadIdentitySourceDict(TypedDict):
    snapshot_staging_path: str
    settings: ClickPipeBigQueryPipeSettingsDict
    table_mappings: list[ClickPipeBigQueryPipeTableMappingDict]
    authentication: Literal["SERVICE_ACCOUNT_WORKLOAD_IDENTITY"]
    project_id: str
