from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_saved_search import ClickStackSavedSearch, ClickStackSavedSearchDict


class V1OrganizationsServicesClickstackSavedSearchesResponse(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Optional[list[ClickStackSavedSearch]] = UNSET


class V1OrganizationsServicesClickstackSavedSearchesResponseDict(TypedDict):
    status: NotRequired[float]
    request_id: NotRequired[UUID]
    result: NotRequired[list[ClickStackSavedSearchDict]]
