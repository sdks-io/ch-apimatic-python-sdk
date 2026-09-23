from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_udfs400_error1 import V1OrganizationsUdfs400Error1
from ..models.v1_organizations_udfs403_error1 import V1OrganizationsUdfs403Error1
from ..models.v1_organizations_udfs409_error1 import V1OrganizationsUdfs409Error1
from ..models.v1_organizations_udfs410_error1 import V1OrganizationsUdfs410Error1
from ..models.v1_organizations_udfs500_error1 import V1OrganizationsUdfs500Error1

UdfCreateErrorBody: TypeAlias = (
    V1OrganizationsUdfs400Error1
    | V1OrganizationsUdfs403Error1
    | V1OrganizationsUdfs409Error1
    | V1OrganizationsUdfs410Error1
    | V1OrganizationsUdfs500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _UdfCreateError:
    def map(self, response: HttpResponse) -> UdfCreateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsUdfs400Error1](response)
            case 403:
                return decode_json[V1OrganizationsUdfs403Error1](response)
            case 409:
                return decode_json[V1OrganizationsUdfs409Error1](response)
            case 410:
                return decode_json[V1OrganizationsUdfs410Error1](response)
            case 500:
                return decode_json[V1OrganizationsUdfs500Error1](response)
            case _:
                return RawError(response)


udf_create_error_mapper: Final[ErrorMapper[UdfCreateErrorBody]] = _UdfCreateError()
