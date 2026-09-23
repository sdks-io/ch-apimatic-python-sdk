from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_udfs_versions400_error1 import V1OrganizationsUdfsVersions400Error1
from ..models.v1_organizations_udfs_versions403_error1 import V1OrganizationsUdfsVersions403Error1
from ..models.v1_organizations_udfs_versions404_error1 import V1OrganizationsUdfsVersions404Error1
from ..models.v1_organizations_udfs_versions409_error1 import V1OrganizationsUdfsVersions409Error1
from ..models.v1_organizations_udfs_versions410_error1 import V1OrganizationsUdfsVersions410Error1
from ..models.v1_organizations_udfs_versions500_error1 import V1OrganizationsUdfsVersions500Error1

UdfVersionCreateErrorBody: TypeAlias = (
    V1OrganizationsUdfsVersions400Error1
    | V1OrganizationsUdfsVersions403Error1
    | V1OrganizationsUdfsVersions404Error1
    | V1OrganizationsUdfsVersions409Error1
    | V1OrganizationsUdfsVersions410Error1
    | V1OrganizationsUdfsVersions500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _UdfVersionCreateError:
    def map(self, response: HttpResponse) -> UdfVersionCreateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsUdfsVersions400Error1](response)
            case 403:
                return decode_json[V1OrganizationsUdfsVersions403Error1](response)
            case 404:
                return decode_json[V1OrganizationsUdfsVersions404Error1](response)
            case 409:
                return decode_json[V1OrganizationsUdfsVersions409Error1](response)
            case 410:
                return decode_json[V1OrganizationsUdfsVersions410Error1](response)
            case 500:
                return decode_json[V1OrganizationsUdfsVersions500Error1](response)
            case _:
                return RawError(response)


udf_version_create_error_mapper: Final[ErrorMapper[UdfVersionCreateErrorBody]] = _UdfVersionCreateError()
