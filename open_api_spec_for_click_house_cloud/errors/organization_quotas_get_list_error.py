from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_quotas400_error1 import V1OrganizationsQuotas400Error1
from ..models.v1_organizations_quotas500_error1 import V1OrganizationsQuotas500Error1

OrganizationQuotasGetListErrorBody: TypeAlias = (
    V1OrganizationsQuotas400Error1 | V1OrganizationsQuotas500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _OrganizationQuotasGetListError:
    def map(self, response: HttpResponse) -> OrganizationQuotasGetListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsQuotas400Error1](response)
            case 500:
                return decode_json[V1OrganizationsQuotas500Error1](response)
            case _:
                return RawError(response)


organization_quotas_get_list_error_mapper: Final[
    ErrorMapper[OrganizationQuotasGetListErrorBody]
] = _OrganizationQuotasGetListError()
