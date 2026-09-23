from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_saved_searches400_error1 import (
    V1OrganizationsServicesClickstackSavedSearches400Error1,
)
from ..models.v1_organizations_services_clickstack_saved_searches500_error1 import (
    V1OrganizationsServicesClickstackSavedSearches500Error1,
)

ClickStackCreateSavedSearchErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackSavedSearches400Error1
    | V1OrganizationsServicesClickstackSavedSearches500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackCreateSavedSearchError:
    def map(self, response: HttpResponse) -> ClickStackCreateSavedSearchErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackSavedSearches400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackSavedSearches500Error1](response)
            case _:
                return RawError(response)


click_stack_create_saved_search_error_mapper: Final[
    ErrorMapper[ClickStackCreateSavedSearchErrorBody]
] = _ClickStackCreateSavedSearchError()
