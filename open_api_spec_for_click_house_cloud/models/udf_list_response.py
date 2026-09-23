from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pagination import Pagination, PaginationDict
from .udf import Udf, UdfDict


class UdfListResponse(SdkBaseModel):
    items: list[Udf]
    """Latest version of each UDF in the organization."""

    pagination: Pagination


class UdfListResponseDict(TypedDict):
    items: list[UdfDict]
    pagination: PaginationDict
