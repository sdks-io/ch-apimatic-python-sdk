from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimX509Certificate(SdkBaseModel):
    value: Optional[str] = UNSET
    """The value of a X.509 certificate."""


class ScimX509CertificateDict(TypedDict):
    value: NotRequired[str]
