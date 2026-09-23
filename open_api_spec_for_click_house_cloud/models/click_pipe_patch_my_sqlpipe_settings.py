from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ClickPipePatchMySqlpipeSettings(SdkBaseModel):
    sync_interval_seconds: OptionalNullable[int] = Field(default=UNSET, alias="syncIntervalSeconds")
    """Interval in seconds to sync data from MySQL during CDC replication."""

    pull_batch_size: OptionalNullable[int] = Field(default=UNSET, alias="pullBatchSize")
    """Number of rows to pull in each batch during CDC replication."""

    use_compression: OptionalNullable[bool] = Field(default=UNSET, alias="useCompression")
    """Enable compression for the MySQL connection."""


class ClickPipePatchMySqlpipeSettingsDict(TypedDict):
    sync_interval_seconds: NotRequired[int | None]
    pull_batch_size: NotRequired[int | None]
    use_compression: NotRequired[bool | None]
