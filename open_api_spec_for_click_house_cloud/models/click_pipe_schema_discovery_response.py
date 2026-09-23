from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_schema_discovery_field import ClickPipeSchemaDiscoveryField, ClickPipeSchemaDiscoveryFieldDict


class ClickPipeSchemaDiscoveryResponse(SdkBaseModel):
    fields: Optional[list[ClickPipeSchemaDiscoveryField]] = UNSET
    """Inferred schema fields with their ClickHouse data types."""

    meta: Optional[dict[str, str | None]] = UNSET


class ClickPipeSchemaDiscoveryResponseDict(TypedDict):
    fields: NotRequired[list[ClickPipeSchemaDiscoveryFieldDict]]
    meta: NotRequired[dict[str, str | None]]
