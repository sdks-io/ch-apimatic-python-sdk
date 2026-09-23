from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_sources_click_stack_source_id400_error1 import (
    V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1,
)
from ..models.v1_organizations_services_clickstack_sources_click_stack_source_id500_error1 import (
    V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1,
)

ClickStackGetSourceErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1
    | V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackGetSourceError:
    def map(self, response: HttpResponse) -> ClickStackGetSourceErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1](response)
            case _:
                return RawError(response)


click_stack_get_source_error_mapper: Final[ErrorMapper[ClickStackGetSourceErrorBody]] = _ClickStackGetSourceError()
