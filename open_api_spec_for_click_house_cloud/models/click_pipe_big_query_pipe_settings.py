from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickPipeBigQueryPipeSettings(SdkBaseModel):
    replication_mode: Literal["snapshot"] = Field(default="snapshot", alias="replicationMode")
    """Replication mode. BigQuery only supports snapshot mode."""

    allow_nullable_columns: Optional[bool] = Field(default=UNSET, alias="allowNullableColumns")
    """Allow nullable columns in the destination table."""

    initial_load_parallelism: Optional[float] = Field(default=UNSET, alias="initialLoadParallelism")
    """Number of parallel workers during initial load."""

    snapshot_num_rows_per_partition: Optional[float] = Field(default=UNSET, alias="snapshotNumRowsPerPartition")
    """Number of rows to snapshot per partition."""

    snapshot_number_of_parallel_tables: Optional[float] = Field(default=UNSET, alias="snapshotNumberOfParallelTables")
    """Number of parallel tables to snapshot."""


class ClickPipeBigQueryPipeSettingsDict(TypedDict):
    replication_mode: Literal["snapshot"]
    allow_nullable_columns: NotRequired[bool]
    initial_load_parallelism: NotRequired[float]
    snapshot_num_rows_per_partition: NotRequired[float]
    snapshot_number_of_parallel_tables: NotRequired[float]
