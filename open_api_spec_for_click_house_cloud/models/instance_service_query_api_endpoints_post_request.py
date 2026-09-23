from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.role import RoleOrStr


class InstanceServiceQueryApiEndpointsPostRequest(SdkBaseModel):
    roles: Optional[list[RoleOrStr]] = UNSET
    """The roles"""

    open_api_keys: Optional[list[str]] = Field(default=UNSET, alias="openApiKeys")
    """The version of the service query endpoint"""

    allowed_origins: Optional[str] = Field(default=UNSET, alias="allowedOrigins")
    """The allowed origins as comma separated list of domains"""


class InstanceServiceQueryApiEndpointsPostRequestDict(TypedDict):
    roles: NotRequired[list[RoleOrStr]]
    open_api_keys: NotRequired[list[str]]
    allowed_origins: NotRequired[str]
