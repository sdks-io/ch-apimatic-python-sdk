from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_udfs_versions_version400_error1 import V1OrganizationsUdfsVersionsVersion400Error1
from ..models.v1_organizations_udfs_versions_version404_error1 import V1OrganizationsUdfsVersionsVersion404Error1
from ..models.v1_organizations_udfs_versions_version409_error1 import V1OrganizationsUdfsVersionsVersion409Error1
from ..models.v1_organizations_udfs_versions_version500_error1 import V1OrganizationsUdfsVersionsVersion500Error1

UdfVersionDeleteErrorBody: TypeAlias = (
    V1OrganizationsUdfsVersionsVersion400Error1
    | V1OrganizationsUdfsVersionsVersion404Error1
    | V1OrganizationsUdfsVersionsVersion409Error1
    | V1OrganizationsUdfsVersionsVersion500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _UdfVersionDeleteError:
    def map(self, response: HttpResponse) -> UdfVersionDeleteErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsUdfsVersionsVersion400Error1](response)
            case 404:
                return decode_json[V1OrganizationsUdfsVersionsVersion404Error1](response)
            case 409:
                return decode_json[V1OrganizationsUdfsVersionsVersion409Error1](response)
            case 500:
                return decode_json[V1OrganizationsUdfsVersionsVersion500Error1](response)
            case _:
                return RawError(response)


udf_version_delete_error_mapper: Final[ErrorMapper[UdfVersionDeleteErrorBody]] = _UdfVersionDeleteError()
