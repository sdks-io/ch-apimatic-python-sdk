from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickStackTraceSourceMetadataMaterializedViews(SdkBaseModel):
    key_rollup_table: Optional[str] = Field(default=UNSET, alias="keyRollupTable")
    """ClickHouse table name for the key rollup (field discovery)."""

    kv_rollup_table: Optional[str] = Field(default=UNSET, alias="kvRollupTable")
    """ClickHouse table name for the key-value rollup (value autocomplete)."""

    granularity: Optional[str] = UNSET
    """The time granularity of the rollup tables."""


class ClickStackTraceSourceMetadataMaterializedViewsDict(TypedDict):
    key_rollup_table: NotRequired[str]
    kv_rollup_table: NotRequired[str]
    granularity: NotRequired[str]
