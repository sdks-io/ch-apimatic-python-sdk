from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServicPrivateEndpointePostRequest(SdkBaseModel):
    id: Optional[str] = UNSET
    """Private endpoint identifier"""

    description: Optional[str] = UNSET
    """Description of private endpoint"""


class ServicPrivateEndpointePostRequestDict(TypedDict):
    id: NotRequired[str]
    description: NotRequired[str]
