from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations400_error1 import V1Organizations400Error1
from ..models.v1_organizations500_error1 import V1Organizations500Error1

OrganizationGetErrorBody: TypeAlias = V1Organizations400Error1 | V1Organizations500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _OrganizationGetError:
    def map(self, response: HttpResponse) -> OrganizationGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1Organizations400Error1](response)
            case 500:
                return decode_json[V1Organizations500Error1](response)
            case _:
                return RawError(response)


organization_get_error_mapper: Final[ErrorMapper[OrganizationGetErrorBody]] = _OrganizationGetError()
