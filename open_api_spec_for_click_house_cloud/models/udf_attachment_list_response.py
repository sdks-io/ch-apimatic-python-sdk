from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pagination import Pagination, PaginationDict
from .udf_attachment import UdfAttachment, UdfAttachmentDict


class UdfAttachmentListResponse(SdkBaseModel):
    items: list[UdfAttachment]
    pagination: Pagination


class UdfAttachmentListResponseDict(TypedDict):
    items: list[UdfAttachmentDict]
    pagination: PaginationDict
