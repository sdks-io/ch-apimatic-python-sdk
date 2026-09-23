from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .api_key import ApiKey, ApiKeyDict


class ApiKeyPostResponse(SdkBaseModel):
    key: Optional[ApiKey] = UNSET
    key_id: Optional[str] = Field(default=UNSET, alias="keyId")
    """Generated key ID. Provided only if there was no 'hashData' in the request."""

    key_secret: Optional[str] = Field(default=UNSET, alias="keySecret")
    """Generated key secret. Provided only if there was no 'hashData' in the request."""


class ApiKeyPostResponseDict(TypedDict):
    key: NotRequired[ApiKeyDict]
    key_id: NotRequired[str]
    key_secret: NotRequired[str]
