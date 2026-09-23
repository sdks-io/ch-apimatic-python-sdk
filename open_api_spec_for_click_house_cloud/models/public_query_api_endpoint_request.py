from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PublicQueryApiEndpointRequest(SdkBaseModel):
    name: str
    """Name of the Query API endpoint."""

    sql: str
    """SQL executed by the endpoint."""

    database: str
    """Database used by the Query API endpoint."""

    parameters: Optional[dict[str, str]] = UNSET
    """Default query parameters."""

    api_key_ids: list[UUID] = Field(alias="apiKeyIds")
    """API key IDs allowed to call the endpoint."""

    roles: list[str]
    """Database roles used by the endpoint."""

    allowed_origins: Optional[list[str]] = Field(default=UNSET, alias="allowedOrigins")
    """Origins allowed by the endpoint CORS policy."""


class PublicQueryApiEndpointRequestDict(TypedDict):
    name: str
    sql: str
    database: str
    parameters: NotRequired[dict[str, str]]
    api_key_ids: list[UUID]
    roles: list[str]
    allowed_origins: NotRequired[list[str]]
