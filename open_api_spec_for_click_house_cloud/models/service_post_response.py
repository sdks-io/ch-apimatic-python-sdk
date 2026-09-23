from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .service import Service, ServiceDict


class ServicePostResponse(SdkBaseModel):
    service: Optional[Service] = UNSET
    password: Optional[str] = UNSET
    """Password for the newly created service."""


class ServicePostResponseDict(TypedDict):
    service: NotRequired[ServiceDict]
    password: NotRequired[str]
