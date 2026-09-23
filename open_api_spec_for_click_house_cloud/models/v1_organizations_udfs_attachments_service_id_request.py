from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1OrganizationsUdfsAttachmentsServiceIdRequest(SdkBaseModel):
    version: Optional[int] = UNSET
    """Version to attach. When omitted, the latest ready version is attached."""


class V1OrganizationsUdfsAttachmentsServiceIdRequestDict(TypedDict):
    version: NotRequired[int]
