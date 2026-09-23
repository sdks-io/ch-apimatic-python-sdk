from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.protocol import ProtocolOrStr


class ServiceEndpoint(SdkBaseModel):
    protocol: Optional[ProtocolOrStr] = UNSET
    """Endpoint protocol: 'https', 'nativesecure', 'mysql'."""

    host: Optional[str] = UNSET
    """Service host name"""

    port: Optional[float] = UNSET
    """Numeric port"""

    username: OptionalNullable[str] = UNSET
    """Optional username for the endpoint"""


class ServiceEndpointDict(TypedDict):
    protocol: NotRequired[ProtocolOrStr]
    host: NotRequired[str]
    port: NotRequired[float]
    username: NotRequired[str | None]
