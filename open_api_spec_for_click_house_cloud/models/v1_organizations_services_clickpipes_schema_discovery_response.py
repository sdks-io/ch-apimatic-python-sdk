from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_schema_discovery_response import ClickPipeSchemaDiscoveryResponse, ClickPipeSchemaDiscoveryResponseDict


class V1OrganizationsServicesClickpipesSchemaDiscoveryResponse(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Optional[ClickPipeSchemaDiscoveryResponse] = UNSET


class V1OrganizationsServicesClickpipesSchemaDiscoveryResponseDict(TypedDict):
    status: NotRequired[float]
    request_id: NotRequired[UUID]
    result: NotRequired[ClickPipeSchemaDiscoveryResponseDict]
