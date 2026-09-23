from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pagination import Pagination, PaginationDict
from .public_query_api_endpoint_list_item import PublicQueryApiEndpointListItem, PublicQueryApiEndpointListItemDict


class QueryApiEndpointListResponse(SdkBaseModel):
    items: list[PublicQueryApiEndpointListItem]
    """Active Query API endpoints for the service, including both owner types."""

    pagination: Pagination


class QueryApiEndpointListResponseDict(TypedDict):
    items: list[PublicQueryApiEndpointListItemDict]
    pagination: PaginationDict
