from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.protocol1 import Protocol1OrStr


class ServiceEndpointChange(SdkBaseModel):
    protocol: Optional[Protocol1OrStr] = UNSET
    """Endpoint protocol"""

    enabled: Optional[bool] = UNSET
    """Enable or disable the endpoint"""


class ServiceEndpointChangeDict(TypedDict):
    protocol: NotRequired[Protocol1OrStr]
    enabled: NotRequired[bool]
