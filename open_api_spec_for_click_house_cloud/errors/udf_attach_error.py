from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_udfs_attachments_service_id400_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId400Error1,
)
from ..models.v1_organizations_udfs_attachments_service_id404_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId404Error1,
)
from ..models.v1_organizations_udfs_attachments_service_id409_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId409Error1,
)
from ..models.v1_organizations_udfs_attachments_service_id422_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId422Error1,
)
from ..models.v1_organizations_udfs_attachments_service_id424_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId424Error1,
)
from ..models.v1_organizations_udfs_attachments_service_id500_error1 import (
    V1OrganizationsUdfsAttachmentsServiceId500Error1,
)

UdfAttachErrorBody: TypeAlias = (
    V1OrganizationsUdfsAttachmentsServiceId400Error1
    | V1OrganizationsUdfsAttachmentsServiceId404Error1
    | V1OrganizationsUdfsAttachmentsServiceId409Error1
    | V1OrganizationsUdfsAttachmentsServiceId422Error1
    | V1OrganizationsUdfsAttachmentsServiceId424Error1
    | V1OrganizationsUdfsAttachmentsServiceId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _UdfAttachError:
    def map(self, response: HttpResponse) -> UdfAttachErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId400Error1](response)
            case 404:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId404Error1](response)
            case 409:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId409Error1](response)
            case 422:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId422Error1](response)
            case 424:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId424Error1](response)
            case 500:
                return decode_json[V1OrganizationsUdfsAttachmentsServiceId500Error1](response)
            case _:
                return RawError(response)


udf_attach_error_mapper: Final[ErrorMapper[UdfAttachErrorBody]] = _UdfAttachError()
