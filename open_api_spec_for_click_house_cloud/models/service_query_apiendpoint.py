from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.role import RoleOrStr


class ServiceQueryApiendpoint(SdkBaseModel):
    id: Optional[str] = UNSET
    """The id of the service query endpoint"""

    open_api_keys: Optional[list[str]] = Field(default=UNSET, alias="openApiKeys")
    """List of OpenAPI keys that can access the service query endpoint"""

    roles: Optional[list[RoleOrStr]] = UNSET
    """List of roles that can access the service query endpoint"""

    allowed_origins: Optional[str] = Field(default=UNSET, alias="allowedOrigins")
    """The allowed origins as comma separated list of domains"""


class ServiceQueryApiendpointDict(TypedDict):
    id: NotRequired[str]
    open_api_keys: NotRequired[list[str]]
    roles: NotRequired[list[RoleOrStr]]
    allowed_origins: NotRequired[str]
