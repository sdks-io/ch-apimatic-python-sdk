from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MutualTls(SdkBaseModel):
    certificate: Optional[str] = UNSET
    """PEM encoded client certificate for mTLS authentication."""

    private_key: Optional[str] = Field(default=UNSET, alias="privateKey")
    """PEM encoded client private key for mTLS authentication."""


class MutualTlsDict(TypedDict):
    certificate: NotRequired[str]
    private_key: NotRequired[str]
