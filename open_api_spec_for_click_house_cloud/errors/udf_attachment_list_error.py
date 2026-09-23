from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_udfs_attachments400_error1 import V1OrganizationsUdfsAttachments400Error1
from ..models.v1_organizations_udfs_attachments404_error1 import V1OrganizationsUdfsAttachments404Error1
from ..models.v1_organizations_udfs_attachments500_error1 import V1OrganizationsUdfsAttachments500Error1

UdfAttachmentListErrorBody: TypeAlias = (
    V1OrganizationsUdfsAttachments400Error1
    | V1OrganizationsUdfsAttachments404Error1
    | V1OrganizationsUdfsAttachments500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _UdfAttachmentListError:
    def map(self, response: HttpResponse) -> UdfAttachmentListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsUdfsAttachments400Error1](response)
            case 404:
                return decode_json[V1OrganizationsUdfsAttachments404Error1](response)
            case 500:
                return decode_json[V1OrganizationsUdfsAttachments500Error1](response)
            case _:
                return RawError(response)


udf_attachment_list_error_mapper: Final[ErrorMapper[UdfAttachmentListErrorBody]] = _UdfAttachmentListError()
