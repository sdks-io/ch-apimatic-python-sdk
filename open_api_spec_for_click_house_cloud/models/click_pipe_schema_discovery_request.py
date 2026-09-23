from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_schema_discovery_source import ClickPipeSchemaDiscoverySource, ClickPipeSchemaDiscoverySourceDict


class ClickPipeSchemaDiscoveryRequest(SdkBaseModel):
    source: Optional[ClickPipeSchemaDiscoverySource] = UNSET


class ClickPipeSchemaDiscoveryRequestDict(TypedDict):
    source: NotRequired[ClickPipeSchemaDiscoverySourceDict]
