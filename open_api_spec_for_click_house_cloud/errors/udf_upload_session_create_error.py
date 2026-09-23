from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_udf_uploads_url400_error1 import V1OrganizationsUdfUploadsUrl400Error1
from ..models.v1_organizations_udf_uploads_url500_error1 import V1OrganizationsUdfUploadsUrl500Error1

UdfUploadSessionCreateErrorBody: TypeAlias = (
    V1OrganizationsUdfUploadsUrl400Error1 | V1OrganizationsUdfUploadsUrl500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _UdfUploadSessionCreateError:
    def map(self, response: HttpResponse) -> UdfUploadSessionCreateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsUdfUploadsUrl400Error1](response)
            case 500:
                return decode_json[V1OrganizationsUdfUploadsUrl500Error1](response)
            case _:
                return RawError(response)


udf_upload_session_create_error_mapper: Final[
    ErrorMapper[UdfUploadSessionCreateErrorBody]
] = _UdfUploadSessionCreateError()
