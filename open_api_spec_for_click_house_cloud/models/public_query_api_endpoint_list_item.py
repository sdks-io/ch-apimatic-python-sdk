from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.owner_type import OwnerTypeOrStr


class PublicQueryApiEndpointListItem(SdkBaseModel):
    id: UUID
    """Unique ID of the Query API endpoint."""

    name: str
    """Name of the Query API endpoint."""

    database: str
    """Database used by the Query API endpoint."""

    api_key_ids: list[UUID] = Field(alias="apiKeyIds")
    """API key IDs allowed to call the endpoint."""

    roles: list[str]
    """Database roles used by the endpoint."""

    allowed_origins: list[str] = Field(alias="allowedOrigins")
    """Origins allowed by the endpoint CORS policy."""

    url: str
    """Public URL used to execute the endpoint."""

    owner_type: OwnerTypeOrStr = Field(alias="ownerType")
    """Owner type of the Query API endpoint. Endpoints with a user owned query cannot be updated or deleted through this
    API."""


class PublicQueryApiEndpointListItemDict(TypedDict):
    id: UUID
    name: str
    database: str
    api_key_ids: list[UUID]
    roles: list[str]
    allowed_origins: list[str]
    url: str
    owner_type: OwnerTypeOrStr
