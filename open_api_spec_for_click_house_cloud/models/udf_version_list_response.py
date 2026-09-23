from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pagination import Pagination, PaginationDict
from .udf import Udf, UdfDict


class UdfVersionListResponse(SdkBaseModel):
    items: list[Udf]
    pagination: Pagination


class UdfVersionListResponseDict(TypedDict):
    items: list[UdfDict]
    pagination: PaginationDict
