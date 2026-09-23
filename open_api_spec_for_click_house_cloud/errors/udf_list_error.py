from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_udfs400_error1 import V1OrganizationsUdfs400Error1
from ..models.v1_organizations_udfs500_error1 import V1OrganizationsUdfs500Error1

UdfListErrorBody: TypeAlias = V1OrganizationsUdfs400Error1 | V1OrganizationsUdfs500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _UdfListError:
    def map(self, response: HttpResponse) -> UdfListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsUdfs400Error1](response)
            case 500:
                return decode_json[V1OrganizationsUdfs500Error1](response)
            case _:
                return RawError(response)


udf_list_error_mapper: Final[ErrorMapper[UdfListErrorBody]] = _UdfListError()
