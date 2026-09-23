from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ClickPipePatchPostgresPipeSettings(SdkBaseModel):
    sync_interval_seconds: OptionalNullable[int] = Field(default=UNSET, alias="syncIntervalSeconds")
    """Interval in seconds to sync data from Postgres during CDC replication."""

    pull_batch_size: OptionalNullable[int] = Field(default=UNSET, alias="pullBatchSize")
    """Number of rows to pull in each batch during CDC replication."""


class ClickPipePatchPostgresPipeSettingsDict(TypedDict):
    sync_interval_seconds: NotRequired[int | None]
    pull_batch_size: NotRequired[int | None]
