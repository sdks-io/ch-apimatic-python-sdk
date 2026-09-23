from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id400_error1 import (
    V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1,
)
from ..models.v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id500_error1 import (
    V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1,
)

ClickStackGetSavedSearchErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1
    | V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackGetSavedSearchError:
    def map(self, response: HttpResponse) -> ClickStackGetSavedSearchErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1](
                    response
                )
            case 500:
                return decode_json[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1](
                    response
                )
            case _:
                return RawError(response)


click_stack_get_saved_search_error_mapper: Final[
    ErrorMapper[ClickStackGetSavedSearchErrorBody]
] = _ClickStackGetSavedSearchError()
