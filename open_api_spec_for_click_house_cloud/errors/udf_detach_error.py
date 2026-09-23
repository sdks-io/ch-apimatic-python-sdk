from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_udfs_attachments_service_id400_error21 import (
    V1OrganizationsUdfsAttachmentsServiceId400Error21,
)
from ..models.v1_organizations_udfs_attachments_service_id404_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId404Error1,
)
from ..models.v1_organizations_udfs_attachments_service_id409_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId409Error1,
)
from ..models.v1_organizations_udfs_attachments_service_id500_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId500Error1,
)

UdfDetachErrorBody: TypeAlias = (
    V1OrganizationsUdfsAttachmentsServiceId400Error21
    | V1OrganizationsUdfsAttachmentsServiceId404Error1
    | V1OrganizationsUdfsAttachmentsServiceId409Error1
    | V1OrganizationsUdfsAttachmentsServiceId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _UdfDetachError:
    def map(self, response: HttpResponse) -> UdfDetachErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId400Error21](response)
            case 404:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId404Error1](response)
            case 409:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId409Error1](response)
            case 500:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId500Error1](response)
            case _:
                return RawError(response)


udf_detach_error_mapper: Final[ErrorMapper[UdfDetachErrorBody]] = _UdfDetachError()
