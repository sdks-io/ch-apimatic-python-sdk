from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ByocInfrastructurePatchRequest(SdkBaseModel):
    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """Human readable name for infrastructure object"""


class ByocInfrastructurePatchRequestDict(TypedDict):
    display_name: NotRequired[str]
