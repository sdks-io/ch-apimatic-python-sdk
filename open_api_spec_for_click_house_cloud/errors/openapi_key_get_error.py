from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_keys400_error1 import V1OrganizationsKeys400Error1
from ..models.v1_organizations_keys500_error1 import V1OrganizationsKeys500Error1

OpenapiKeyGetErrorBody: TypeAlias = V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _OpenapiKeyGetError:
    def map(self, response: HttpResponse) -> OpenapiKeyGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsKeys400Error1](response)
            case 500:
                return decode_json[V1OrganizationsKeys500Error1](response)
            case _:
                return RawError(response)


openapi_key_get_error_mapper: Final[ErrorMapper[OpenapiKeyGetErrorBody]] = _OpenapiKeyGetError()
