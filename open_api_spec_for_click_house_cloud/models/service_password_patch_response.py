from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServicePasswordPatchResponse(SdkBaseModel):
    password: Optional[str] = UNSET
    """New service password. Provided only if there was no 'newPasswordHash' in the request"""


class ServicePasswordPatchResponseDict(TypedDict):
    password: NotRequired[str]
