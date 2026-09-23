from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_big_query_pipe_settings import ClickPipeBigQueryPipeSettings, ClickPipeBigQueryPipeSettingsDict
from .click_pipe_big_query_pipe_table_mapping import (
    ClickPipeBigQueryPipeTableMapping,
    ClickPipeBigQueryPipeTableMappingDict,
)
from .enums.authentication16 import Authentication16OrStr
from .service_account import ServiceAccount, ServiceAccountDict


class ClickPipePostBigQueryServiceAccountSource(SdkBaseModel):
    snapshot_staging_path: str = Field(alias="snapshotStagingPath")
    """GCS bucket path for staging snapshot data (e.g., gs://my-bucket/staging/). Data will be automatically cleaned up
    after initial load."""

    settings: ClickPipeBigQueryPipeSettings
    table_mappings: list[ClickPipeBigQueryPipeTableMapping] = Field(alias="tableMappings")
    """Table mappings for BigQuery pipe."""

    authentication: Optional[Authentication16OrStr] = UNSET
    """Authenticate with a Google Cloud service account JSON key. Defaults to SERVICE_ACCOUNT when omitted."""

    project_id: Optional[str] = Field(default=UNSET, alias="projectId")
    """GCP project ID that owns the BigQuery resources."""

    credentials: ServiceAccount


class ClickPipePostBigQueryServiceAccountSourceDict(TypedDict):
    snapshot_staging_path: str
    settings: ClickPipeBigQueryPipeSettingsDict
    table_mappings: list[ClickPipeBigQueryPipeTableMappingDict]
    authentication: NotRequired[Authentication16OrStr]
    project_id: NotRequired[str]
    credentials: ServiceAccountDict
